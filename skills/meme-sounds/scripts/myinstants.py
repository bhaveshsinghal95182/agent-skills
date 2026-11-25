#!/usr/bin/env python3
"""Search and download sounds from myinstants.com, checking the local
Sound Library first.

Stdlib only. Outputs JSON so agents can consume it directly.

Usage:
  myinstants.py get "vine boom" [--json]        # local match first, else download
  myinstants.py search "vine boom" [--page 2] [--limit 10] [--json]
  myinstants.py download "vine boom" [--index 1] [--out DIR] [--name NAME] [--json]
  myinstants.py download --url /media/sounds/xyz.mp3 --title "Vine Boom" [--out DIR] [--json]
  myinstants.py list [--json]                   # list local library with durations

get: the command agents should use. It scans ~/Videos/Sound Library for a
file whose name matches the query; on a hit it returns that path and nothing
is downloaded. Only when nothing matches does it search myinstants and
download the best match.

download always goes to the network (skipping the local check). search never
downloads. --index N picks the Nth ranked search result (1-based, matching
the numbering printed by search).
"""

import argparse
import html
import json
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path

BASE = "https://www.myinstants.com"
LIBRARY = Path.home() / "Videos" / "Sound Library"
DEFAULT_OUT = LIBRARY / "Memes"

# Minimum search score for `get` to auto-download the top result (see score()).
# 40 = the query appears as a substring of the title, or 2+ query words hit
# the file name. Below that, myinstants' fuzzy search is returning noise.
MIN_SCORE = 40

# The play button precedes the instant link inside each result block:
#   <button class="small-button" onclick="play('/media/sounds/x.mp3', 'loader-N', 'slug')" ...>
#   <a href="/en/instant/slug/" class="instant-link link-secondary">TITLE</a>
INSTANT_RE = re.compile(
    r"play\('(/media/sounds/[^']+)',\s*'loader-\d+'\s*,\s*'[^']*'\)"
    r"(?:(?!play\().){0,2000}?"
    r'<a\s+href="(/en/instant/[^"]+)"[^>]*>([^<]+)</a>',
    re.S,
)


def fetch(url: str) -> bytes:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) meme-sounds-skill/1.0",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


# ---------- myinstants search ----------

def search(query: str, page: int = 1) -> list[dict]:
    url = BASE + "/en/search/?" + urllib.parse.urlencode({"name": query})
    if page > 1:
        url += f"&page={page}"
    body = fetch(url).decode("utf-8", "replace")
    seen = set()
    results = []
    for mp3_path, instant_path, title in INSTANT_RE.findall(body):
        if mp3_path in seen:
            continue
        seen.add(mp3_path)
        results.append(
            {
                "title": html.unescape(title).strip(),
                "mp3_path": mp3_path,
                "mp3_url": BASE + mp3_path,
                "instant_url": BASE + instant_path,
            }
        )
    return results


def score(result: dict, query: str) -> int:
    """Higher is better. Fuzzy search on myinstants returns noise, so title
    similarity to the query is the strongest signal."""
    q = query.lower().strip()
    t = result["title"].lower().strip()
    slug = result["mp3_path"].rsplit("/", 1)[-1].lower()
    if t == q:
        return 100
    if t.startswith(q):
        return 80
    if q in t:
        return 60
    # File name often matches the query even when the title is decorated
    # ("BRUH sound effect!" vs "bruh-sound-effect_WstdzdM.mp3").
    q_words = [w for w in re.split(r"[\s-]+", q) if w]
    slug_words = set(re.split(r"[\s_-]+", slug))
    hits = sum(1 for w in q_words if w in slug_words)
    return 20 * hits


def ranked(query: str, page: int = 1) -> list[dict]:
    results = search(query, page)
    for r in results:
        r["score"] = score(r, query)
    results.sort(key=lambda r: -r["score"])
    return results


# ---------- local library ----------

def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or "sound"


def duration_of(path: Path) -> float | None:
    try:
        out = subprocess.run(
            [
                "ffprobe", "-v", "quiet",
                "-show_entries", "format=duration",
                "-of", "csv=p=0", str(path),
            ],
            capture_output=True, text=True, timeout=15,
        )
        return round(float(out.stdout.strip()), 2)
    except Exception:
        return None


def local_files() -> list[Path]:
    """Every sound in the library. Memes/ and SFX/ are Slatey's two
    subfolders, but scan any folder so user-made ones work too."""
    if not LIBRARY.is_dir():
        return []
    return sorted(
        p for p in LIBRARY.rglob("*")
        if p.is_file() and p.suffix.lower() in (".mp3", ".wav", ".ogg", ".m4a", ".flac")
    )


def local_match(query: str) -> Path | None:
    """A file matches when every word of the query appears as a word in its
    filename. Strict on purpose: a wrong local match is worse than a download,
    because the agent never looks at the alternatives."""
    q_words = [w for w in re.split(r"[\s-]+", query.lower()) if w]
    if not q_words:
        return None
    for p in local_files():
        name = re.sub(r"\.[a-z0-9]+$", "", p.name.lower())
        f_words = set(re.split(r"[\s_-]+", name))
        if all(w in f_words for w in q_words):
            return p
    return None


# ---------- commands ----------

def cmd_list(as_json: bool) -> int:
    files = local_files()
    items = [
        {"file": str(p), "name": p.stem, "duration_s": duration_of(p)}
        for p in files
    ]
    if as_json:
        print(json.dumps({"library": str(LIBRARY), "count": len(items), "sounds": items}, indent=2))
    else:
        print(f"{LIBRARY} — {len(items)} sounds")
        for it in items:
            d = f"{it['duration_s']}s" if it["duration_s"] is not None else "?"
            print(f"  {it['name']}  ({d})")
    return 0


def emit(record: dict, as_json: bool) -> int:
    status = record["status"]
    code = 1 if status in ("error", "no-results", "no-good-match") else 0
    if as_json:
        print(json.dumps(record, indent=2))
        return code
    if status in ("local", "already-have"):
        print(f"{status}: {record['file']} ({record['duration_s']}s) — {record.get('title', record.get('name', ''))}")
    elif status == "downloaded":
        print(f"downloaded: {record['file']} ({record['duration_s']}s) — {record['title']}")
    elif status in ("no-results", "no-good-match"):
        print(record["error"], file=sys.stderr)
        if record.get("candidates"):
            for i, c in enumerate(record["candidates"], 1):
                print(f"  {i}. {c['title']}  (score {c['score']})", file=sys.stderr)
    return code


def do_download(result: dict, out_dir: Path, name: str | None) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / (slugify(name or result["title"]) + ".mp3")
    if dest.exists() and dest.stat().st_size > 0:
        return {
            "status": "already-have",
            "title": result["title"],
            "file": str(dest),
            "duration_s": duration_of(dest),
            "url": result["mp3_url"],
        }
    data = fetch(result["mp3_url"])
    if len(data) < 512:
        return {"status": "error", "error": f"file too small ({len(data)} bytes), probably not a real sound"}
    dest.write_bytes(data)
    return {
        "status": "downloaded",
        "title": result["title"],
        "file": str(dest),
        "duration_s": duration_of(dest),
        "url": result["mp3_url"],
    }


def cmd_get(query: str, out_dir: Path, as_json: bool) -> int:
    hit = local_match(query)
    if hit is not None:
        return emit(
            {
                "status": "local",
                "file": str(hit),
                "name": hit.stem,
                "duration_s": duration_of(hit),
            },
            as_json,
        )
    results = ranked(query)
    # Below this, the "match" is fuzzy-search noise (myinstants returns
    # something for any query). Downloading it would put a wrong, often
    # minutes-long file in the library. Hand back candidates instead.
    if not results or results[0]["score"] < MIN_SCORE:
        cands = [
            {"title": r["title"], "url": r["mp3_url"], "score": r["score"]}
            for r in results[:5]
        ]
        return emit(
            {
                "status": "no-good-match",
                "error": f"nothing in the local library and no close myinstants match for: {query!r}",
                "hint": "try another search term, or pick a candidate with: download <query> --index N",
                "candidates": cands,
            },
            as_json,
        )
    try:
        record = do_download(results[0], out_dir, None)
    except Exception as e:
        return emit({"status": "error", "error": f"download failed: {e}"}, as_json)
    return emit(record, as_json)


def cmd_download(a) -> int:
    out_dir = Path(a.out).expanduser()

    if a.url:
        if not a.url.startswith("/media/sounds/"):
            print("--url must be a /media/sounds/... path", file=sys.stderr)
            return 1
        result = {"title": a.title, "mp3_url": BASE + a.url}
    else:
        if not a.query:
            print("download needs a query or --url", file=sys.stderr)
            return 1
        results = ranked(a.query, a.page)
        if not results:
            return emit({"status": "no-results", "error": f"no results for: {a.query!r}"}, a.json)
        if a.index > len(results):
            print(f"--index {a.index} out of range ({len(results)} results)", file=sys.stderr)
            return 1
        result = results[a.index - 1]

    try:
        record = do_download(result, out_dir, a.name)
    except Exception as e:
        return emit({"status": "error", "error": f"download failed: {e}"}, a.json)
    return emit(record, a.json)


def main() -> int:
    p = argparse.ArgumentParser(description="Search and download meme sounds from myinstants.com")
    sub = p.add_subparsers(dest="cmd", required=True)

    pg = sub.add_parser("get", help="local library first, download only on a miss")
    pg.add_argument("query")
    pg.add_argument("--out", default=str(DEFAULT_OUT))
    pg.add_argument("--json", action="store_true")

    pl = sub.add_parser("list", help="list the local Sound Library with durations")
    pl.add_argument("--json", action="store_true")

    ps = sub.add_parser("search", help="list matching sounds on myinstants")
    ps.add_argument("query")
    ps.add_argument("--page", type=int, default=1)
    ps.add_argument("--limit", type=int, default=10)
    ps.add_argument("--json", action="store_true")

    pd = sub.add_parser("download", help="download from myinstants (skips the local check)")
    pd.add_argument("query", nargs="?", help="search query; best match is downloaded")
    pd.add_argument("--index", type=int, default=1,
                    help="1-based index into the ranked search results")
    pd.add_argument("--page", type=int, default=1)
    pd.add_argument("--url", help="direct /media/sounds/... path (skips search)")
    pd.add_argument("--title", default="sound", help="title when using --url")
    pd.add_argument("--name", help="file name (without extension) for the saved file")
    pd.add_argument("--out", default=str(DEFAULT_OUT))
    pd.add_argument("--json", action="store_true")

    a = p.parse_args()

    if a.cmd == "list":
        return cmd_list(a.json)
    if a.cmd == "get":
        return cmd_get(a.query, Path(a.out).expanduser(), a.json)
    if a.cmd == "search":
        results = ranked(a.query, a.page)[: a.limit]
        if not results:
            print(json.dumps({"results": []}) if a.json
                  else f"no results for: {a.query!r}", file=sys.stderr)
            return 1
        if a.json:
            print(json.dumps({"query": a.query, "page": a.page, "results": results}, indent=2))
        else:
            for i, r in enumerate(results, 1):
                print(f"{i}. {r['title']}  [{r['mp3_url']}]")
        return 0
    return cmd_download(a)


if __name__ == "__main__":
    sys.exit(main())
