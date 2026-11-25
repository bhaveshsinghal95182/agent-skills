#!/usr/bin/env python3
"""Gate a script against the AI-tell ban list.

    python check_script.py script.md
    python check_script.py --strict script.md    # exit 1 if anything is flagged
    python check_script.py --list

Three layers, cheapest first:

  1. words    — the vocabulary models reach for (pompous verbs, inflated
                adjectives, hedges, marketing speak, vague authority)
  2. shapes   — sentence patterns: "not X, it's Y", "here's the thing",
                teacher-mode, reflex analogies, phantom futures, fake counters
  3. rhythm   — density caps (em-dash, tricolon) plus sentence-length and
                same-opener monotony, which is what makes a script sound machine
                read even when every individual line is clean

Markdown scaffolding (headings, tables, rules, code) is skipped: formatting
punctuation is not narration.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

WORDS: dict[str, list[str]] = {
    "opener": [
        "in a world where", "in today's fast-paced world", "in today's digital age",
        "in an age where", "in the ever-evolving landscape", "more than ever before",
        "in recent years", "at its core", "welcome to", "hey guys", "what's up guys",
        "welcome back", "in this video i'm going to", "in this video, i'm going to",
        "let's dive in", "let's get started",
    ],
    "closer": [
        "in conclusion", "ultimately", "to summarise", "to summarize",
        "at the end of the day", "final thoughts", "to sum up", "in summary",
        "all in all", "taking everything into account", "so what does this all mean",
    ],
    "pompous verb": [
        "delve", "unpack", "navigate", "harness", "leverage", "utilize", "utilise",
        "optimize", "optimise", "facilitate", "foster", "cultivate", "embark",
        "revolutionize", "revolutionise", "elevate", "empower", "unlock", "streamline",
        "spearhead", "grapple", "showcase", "underscore", "illuminate", "amplify",
        "galvanize", "catalyze", "transcend", "embody", "epitomize", "curate",
        "alleviate", "supercharge", "turbocharge", "maximize", "maximise",
    ],
    "is-family": [
        "serves as", "stands as", "represents", "embodies", "constitutes",
        "functions as", "operates as", "emerges as",
    ],
    "inflated adjective": [
        "robust", "pivotal", "crucial", "vital", "essential", "significant",
        "comprehensive", "meticulous", "innovative", "transformative", "groundbreaking",
        "seamless", "multifaceted", "intricate", "vibrant", "ever-evolving",
        "cutting-edge", "paramount", "unparalleled", "profound", "staggering",
        "breathtaking", "game-changing", "game-changer", "best-in-class",
        "world-class", "industry-leading", "next-level", "frictionless",
        "state-of-the-art", "holistic", "state of the art",
    ],
    "magic adverb": [
        "quietly", "deeply", "fundamentally", "remarkably", "arguably", "notably",
        "significantly", "profoundly", "inherently", "undoubtedly", "invariably",
        "seamlessly", "effortlessly",
    ],
    "showy noun": [
        "tapestry", "landscape", "realm", "ecosystem", "paradigm", "journey",
        "odyssey", "testament", "cornerstone", "hallmark", "pillar", "beacon",
        "frontier", "fabric", "mosaic", "treasure trove", "flywheel", "north star",
    ],
    "hedge": [
        "it is worth noting that", "one could argue", "broadly speaking",
        "generally speaking", "in many cases", "tends to", "can sometimes",
        "may often", "often considered", "is typically", "is usually",
        "is generally", "is largely", "might be", "could potentially",
        "is essentially",
    ],
    "vague authority": [
        "studies show", "research suggests", "experts agree", "data confirms",
        "it is well known that", "it is widely accepted that", "it is no secret that",
        "many believe", "most agree", "industry consensus is", "common wisdom says",
        "conventional thinking suggests",
    ],
    "bridge": [
        "furthermore", "moreover", "in addition", "on top of that", "beyond that",
        "in essence", "when it comes to", "as we explore", "as we examine",
        "as we consider", "this is more than just", "what makes this special",
    ],
    "delivery": [
        "exciting", "amazing", "insane", "crazy", "incredible", "awesome",
        "unbelievable", "mind-blowing",
    ],
}

SHAPES: dict[str, list[str]] = {
    "reframe (not X, it's Y)": [
        r"\b(?:it|this|that|they|we)\s+(?:isn'?t|is not|wasn'?t|was not|aren'?t|are not)\b[^.!?]{2,70}?\b(?:it'?s|it is|they'?re|they are|but)\b",
        r"\bnot just\b[^.!?]{2,60}?\bbut\b",
        r"\b(?:was|were)\s+never\s+\w+[^.!?]{0,40}?\b(?:it|they)\s+(?:was|were)\b",
        r"\bthe question isn'?t\b[^.!?]{0,60}?\bthe (?:real )?question is\b",
    ],
    "promised payoff": [
        r"\bhere'?s the thing\b", r"\bhere'?s the kicker\b",
        r"\bhere'?s where it gets\b", r"\bwhat nobody tells you\b",
        r"\bhere'?s what nobody\b",
    ],
    "teacher mode": [
        r"\blet'?s break (?:this|it) down\b", r"\blet'?s unpack\b",
        r"\blet me explain\b", r"\blet'?s dive in\b", r"\blet'?s get into it\b",
    ],
    "reflex analogy": [
        r"\bthink of it as\b", r"\bimagine it like\b", r"\bit'?s basically\b",
        r"\bthink of (?:it|this) like\b",
    ],
    "future projection": [
        r"\bimagine a world where\b", r"\ba year from (?:today|now)\b",
        r"\bfive years (?:from now|on)\b", r"\bby the time you reali[sz]e\b",
        r"\byou'?ll wish you\b",
    ],
    "real-story claim": [
        r"\bthe truth is\b", r"\bwhat'?s actually happening\b",
        r"\bthe reality is\b", r"\bhistory is clear\b",
    ],
    "stacked negation": [
        r"\bnot\s+\w+\.\s*not\s+\w+\.",
    ],
    "algorithmic empathy": [
        r"\byou'?re not alone\b", r"\bfeeling (?:stuck|lost|overwhelmed) is\b",
        r"\bit'?s okay to feel\b", r"\bit'?s completely normal\b",
    ],
    "self-awareness costume": [
        r"\blook, i'?ll admit\b", r"\bsince we'?re being real\b",
        r"\bi'?ll be honest with you\b",
    ],
    "self-asked question": [
        r"\?\s*(?:brutal|everything|nothing|nobody|no one|simple|the answer)\b",
    ],
    "fake spectrum": [
        r"\bfrom\s+\w+\s+to\s+\w+\s+to\s+\w+\b",
    ],
}

EM_DASH_PER = 300
TRICOLON_PER = 500
SENTENCE_RE = re.compile(r"[^.!?]+[.!?]")
TRICOLON_RE = re.compile(
    r"\b[\w'-]+,\s+[\w'-]+(?:\s+[\w'-]+)?,?\s+(?:and|or)\s+[\w'-]+", re.IGNORECASE
)


def prose(lines: list[str]) -> list[tuple[int, str]]:
    kept, fenced = [], False
    for number, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("```"):
            fenced = not fenced
            continue
        if fenced or not stripped:
            continue
        if stripped.startswith(("#", "|", ">", "`")):
            continue
        if "·" in stripped and stripped.count("·") >= 2:  # metadata line, not prose
            continue
        if re.fullmatch(r"[-*_]{3,}", stripped):
            continue
        kept.append((number, stripped))
    return kept


def word_hits(lines: list[tuple[int, str]], phrase: str) -> list[tuple[int, str]]:
    pattern = re.compile(r"(?<![a-z])" + re.escape(phrase) + r"(?![a-z])", re.IGNORECASE)
    return [(n, line) for n, line in lines if pattern.search(line)]


def shape_hits(lines: list[tuple[int, str]], pattern: str) -> list[tuple[int, str, str]]:
    compiled = re.compile(pattern, re.IGNORECASE)
    out = []
    for number, line in lines:
        match = compiled.search(line)
        if match:
            out.append((number, match.group(0).strip(), line))
    return out


def rhythm(text: str) -> list[str]:
    findings = []
    # inline code and bold markers aren't spoken; they also break sentence splitting
    text = re.sub(r"`[^`]*`", " ", text)
    text = text.replace("**", " ").replace("…", " ")
    sentences = [s.strip() for s in SENTENCE_RE.findall(text) if s.strip()]
    lengths = [len(s.split()) for s in sentences]

    for i in range(len(lengths) - 2):
        window = lengths[i:i + 3]
        if max(window) - min(window) <= 2 and 8 <= window[0] <= 22:
            findings.append(
                f"sentences {i + 1}-{i + 3} are {window[0]}/{window[1]}/{window[2]} words — "
                "uniform length reads as machine rhythm"
            )
            break

    openers = []
    for s in sentences:
        words = s.split()
        openers.append(words[0].lower().strip(",.") if words else "")
    for i in range(len(openers) - 2):
        if openers[i] and openers[i] == openers[i + 1] == openers[i + 2]:
            findings.append(
                f"three sentences in a row open with '{openers[i]}' — vary the opener"
            )
            break
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--strict", action="store_true", help="exit 1 if anything is flagged")
    parser.add_argument("--wpm", type=float, default=135.0, help="reading pace (default 135)")
    parser.add_argument("--list", action="store_true", help="print the word lists and exit")
    args = parser.parse_args()

    if args.list:
        for category, phrases in WORDS.items():
            print(f"\n{category} ({len(phrases)})")
            for phrase in phrases:
                print(f"  {phrase}")
        print("\nshapes")
        for category in SHAPES:
            print(f"  {category}")
        return 0

    if not args.path:
        parser.error("a script path is required unless --list is used")

    lines = prose(args.path.read_text(encoding="utf-8").splitlines())
    text = "\n".join(line for _, line in lines)
    total_words = len(text.split())
    duration = total_words / args.wpm * 60
    em_dashes = text.count("—")
    tricolons = len(TRICOLON_RE.findall(text))

    print(f"{args.path}  ·  {total_words} words  ·  ≈{duration:.0f}s at {args.wpm:.0f} wpm")

    hard = 0
    for category, phrases in WORDS.items():
        rows = []
        for phrase in phrases:
            for number, line in word_hits(lines, phrase):
                rows.append((number, phrase, line))
        if rows:
            rows.sort()
            print(f"\n{category}: {len(rows)}")
            for number, phrase, line in rows:
                print(f"  line {number:>4}  [{phrase}]  {line[:96]}")
            hard += len(rows)

    for category, patterns in SHAPES.items():
        rows = []
        for pattern in patterns:
            rows.extend(shape_hits(lines, pattern))
        if rows:
            rows.sort()
            print(f"\n{category}: {len(rows)}")
            for number, found, line in rows[:6]:
                print(f"  line {number:>4}  «{found[:60]}»  {line[:80]}")
            hard += len(rows)

    print("\nrhythm")
    em_limit = max(1, round(total_words / EM_DASH_PER))
    tri_limit = max(1, round(total_words / TRICOLON_PER))
    print(f"  em-dashes  {em_dashes:3}   cap {em_limit} (1 per {EM_DASH_PER} words)"
          f"{'  OVER' if em_dashes > em_limit else ''}")
    print(f"  tricolons  {tricolons:3}   cap {tri_limit} (1 per {TRICOLON_PER} words, heuristic")
    print(f"             — folder paths and real lists count as hits; judge by eye)")
    monotony = rhythm(text)
    for finding in monotony:
        print(f"  {finding}")
    over = em_dashes > em_limit or bool(monotony)

    if hard:
        print("\njudgement required: a literal use can be correct — 'enable Docker', "
              "'two hundred overall',\n'data-driven cache'. The tell is the abstraction, "
              "not the word.")
    if hard or over:
        print(f"\n{hard} pattern hit(s)" + (", rhythm over cap" if over else "") +
              ". Replace, do not just delete — see references/banned-words.md.")
        return 1 if args.strict else 0
    print("\nclean.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
