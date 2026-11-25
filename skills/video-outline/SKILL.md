---
name: video-outline
description: "Plan a video before any narration is written: the single promise, the audience, the runtime, and a 7-10 point beat sheet where every point does a unique job and every point has a picture attached. Produces a footage audit so missing shots are found before the script exists. Use whenever the user says they want to make a video, asks what a video should cover, wants an outline, structure, beat sheet, storyboard, shot list, or is planning a tutorial/demo/explainer and has not written the script yet."
---

# Video outline

The outline is where a video is won or lost — not the edit, not the thumbnail.
Every hour spent here is three hours not spent discovering, mid-edit, that the
middle has nothing to show.

An outline is finished when someone else could record the footage from it without
asking you a question.

## The four decisions

Settle these first. Cheap to change now, expensive later.

**1. The promise.** One sentence, stated as a noun, that the viewer gets by the
end. "A media server that runs off one laptop." Not "how to set up a media
server" — that is a topic, and topics produce videos that wander.

**2. The starting point.** What does the viewer already have, and what have they
probably tried? A tutorial that explains Docker to someone running Docker wastes
their time; one that skips it loses the person who doesn't. Pick one and say which.

**3. The runtime.** Decide in minutes, now. This is the budget every point spends.
A video with no runtime always comes in at twice the length it should be.

**4. The proof.** What is on screen at the end that proves the promise was kept?
It should be footage that exists. If the payoff cannot be filmed, the video cannot
be made yet.

## The points

7–10, not more. Rules, in order of how much they matter:

- **One idea per point.** If two points are the same idea, cut one. This is the
  single most common failure of AI-assisted outlines.
- **Every point does a different job.** Assign one: *Setup, Mechanism, Proof,
  Reframe, Fix, Close*. Two points with the same job are one point.
- **Narrative arc, not a list.** Each point opens a question or tension the next
  one answers. The outline is a chain, not a menu.
- **Every point carries a story, a framework, or an analogy** — plus the insight
  in one or two sentences.
- **Write the insight as a sentence, not a label.** "The token check passed while
  the session was already dead" is an insight; "Auth: broken token" is a note to
  self. The "viewer learns" column should hold a complete thought the narrator can
  say out loud. The shared prose rule is in
  `../voice-dna/references/continuous-prose.md`.
- **The title-sequence test.** Read only the point titles, in order. They should
  tell the whole story on their own. If they read like a table of contents
  ("Introduction, Overview, Setup, Configuration"), the points are topics, not
  beats.
- **No filler points to hit a number.** Six strong points beat nine with three
  repeats.

State the real angle first, in one sentence, if the brain dump's surface topic
isn't what the video is actually about. Then build the points.

## The beat sheet

One row per point, four columns:

| # | Point | Viewer learns | On screen |
|---|-------|---------------|-----------|
| 1 | Cold open | that this already works | the finished result, moving |
| 2 | Promise | what they get, and how long it takes | one static frame + title card |
| 3 | Map | how many parts, in what order | the whole thing, labelled |
| 4 | … | … | … |

**"On screen" is not optional.** A point with no picture becomes a talking head, a
stock clip, or a text card. That is fine once. Three times and the video is a
podcast.

**Order by what the viewer needs, not what you did.** Your build took six hours;
the viewer needs the four decisions that mattered and a speed-ramp for the rest.

## The footage audit

Walk the beat sheet and mark every shot:

- `HAVE` — already recorded, with timecode
- `TODO` — needs recording, with what must be on screen
- `CUT` — cannot be recorded for a sane cost; the beat dies here

Do this **before** writing narration, and give the user the `TODO` list as a
blocking checklist. This is the most valuable thing the skill does: a script
written against footage that does not exist is a script that gets rewritten, or
ships with placeholders.

Writing the script first feels like progress. It is borrowing against a loan you
repay at 3am before upload.

## Runtime math

```
words ≈ minutes × 135            technical walkthrough: 110–125 wpm
```

Then add ~10% for beats that need a pause to land — a result appearing on screen
needs a second of silence, not narration over it.

If the sheet overshoots, **cut points**. Removing a point costs one line in a
document; speeding up the narration costs the whole video's feel.

## Shape patterns worth stealing

- **Result → map → steps → result again.** Default for tutorials. The second
  appearance lands differently once the parts are understood.
- **Problem → false fix → real fix.** For anything where the obvious answer fails.
  Viewers stay because they already tried the false fix.
- **One install, one decision at a time.** Every point is "app opens, one setting
  changes, here's why". Keeps momentum without a map.
- **Build in public, compressed.** Three moments, not ten, with the boring middle
  collapsed into a speed ramp and one honest sentence.

## Deliverable

One markdown file:

1. The four decisions
2. The real angle, if you had to reframe
3. The points with jobs and on-screen notes
4. The footage audit, with `TODO` items written as instructions
5. At most three open questions, each with the default you would pick

Keep the sheet to one screen. If it needs scrolling, there are too many points or
the points are too small.

Next: `video-hooks` for the opening, `video-script-writing` for the narration,
`video-qc` for the review pass.
