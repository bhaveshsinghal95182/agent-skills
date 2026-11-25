---
name: meme-sounds
description: "Find and download meme and reaction sounds from myinstants.com, checking the local Sound Library (~/Videos/Sound Library) first so nothing is downloaded twice. Use whenever the user asks for a meme sound, sound effect, reaction sound, bruh/vine boom/bonk-style sting, or says to fetch sounds from myinstants; when they describe a situation ('a sound for when something embarrassing happens', 'something for the fail moment'); and when editing or mixing a video and a beat needs a sound the library doesn't have yet. Built for the Slatey pipeline: downloads land in ~/Videos/Sound Library/Memes where Slatey's sound placement picks them up."
---

# Meme sounds

One script does everything:

```
python3 ~/.agents/skills/meme-sounds/scripts/myinstants.py get "vine boom" --json
```

`get` is local-first. It scans `~/Videos/Sound Library` (every subfolder, not
just Memes) for a file whose name matches the query. On a hit it returns that
path and downloads nothing. On a miss it searches myinstants and downloads the
best match. Use `--json` when another tool or agent consumes the output; the
record always has a `status` field:

| status | meaning | exit |
|---|---|---|
| `local` | found in the library, nothing downloaded | 0 |
| `downloaded` | fetched from myinstants and saved | 0 |
| `already-have` | the exact target file already exists | 0 |
| `no-good-match` | nothing local and only fuzzy noise online; candidates listed | 1 |
| `error` | network or download failure | 1 |

Other commands: `list` (local library with durations), `search QUERY`
(myinstants results, no download), `download QUERY --index N` (pick a specific
search result), `download --url /media/sounds/x.mp3 --title "Name"` (a direct
path). See the script's docstring.

## Behavior by request shape

**Named sound** ("get me a bruh sound", "add the windows xp error noise"):
run `get` with the name as the query. Done.

**Described situation** ("a sound for when the code finally compiles",
"something for the fail montage"): translate the situation into concrete
search terms first, using `references/situations.md`. Search myinstants with
`search`, show the user the top few titles, download the one they confirm. If
they gave a clear situation and you're mid-edit on their behalf, pick the
strongest term yourself, run `get`, and say which one you chose and why.

**Bulk fill before an edit**: read the transcript or beat sheet, list the
moments that need sounds, map each to a term from the reference, then `get`
each term once. The local-first check makes repeat terms free.

## Choosing the term

myinstants search is literal and fuzzy. It returns something for any query,
and the script's scoring rejects weak matches rather than saving junk (a
wrong meme is worse than no meme). To get a real hit:

- Search the meme's common name, not a description: `vine boom`, not `deep
  bass hit sound`. The reference file maps situations to names that work.
- One concept per query. `sad violin` works; `sad violin for when he loses
  again` gets noise.
- If `get` returns `no-good-match`, look at the candidates. Either pick one
  with `download QUERY --index N`, or try a shorter synonym. The canonical
  name runs 1-3 words.
- Prefer the classic version of a meme over fan edits. The first result with
  a high score is the original in most cases.

## Placing sounds in a video (Slatey)

Downloads land in `~/Videos/Sound Library/Memes`, which Slatey reads. When
mixing, follow Slatey's own placement rules (in its MCP instructions):
memes with speech go in pauses at least as long as the meme, effects sit
quieter than the voice, every clip gets a label. The `duration_s` in the
script's output is what you check a pause against.

If the Slatey MCP is connected, its `get_sound` tool does the same local-first
flow (library match, else myinstants download) and returns a `library:` path
ready for `edit_mix`. When mixing through Slatey, prefer it. Use this
script when Slatey isn't connected, and use `references/situations.md` for
the situation-to-name translation either way. Slatey's `list_sounds` shows
the same library this script scans, so the two never disagree about what
exists.

## Library hygiene

- Files are saved as `<slugified-name>.mp3` under `Memes/`. Sounds that
  belong with effects rather than memes (whooshes, clicks) can go to
  `SFX/` with `--out ~/Videos/Sound\ Library/SFX`; `get` scans both.
- Nothing is ever overwritten. If a name collides, the existing file is
  returned as `already-have`.
- Downloads under 512 bytes are rejected; myinstants serves those for dead
  links.
