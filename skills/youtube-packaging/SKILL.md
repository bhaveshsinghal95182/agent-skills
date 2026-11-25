---
name: youtube-packaging
description: "Title, thumbnail concept, description, chapters, pinned comment and end screen for a video, written as one consistent promise. Use when the user asks for a YouTube title, thumbnail idea, video description, tags, chapters, or says a video isn't getting clicks, or asks why views are low, or wants to upload/publish a video. Packaging decides whether the video gets watched at all, so use it before scripting when the promise is still changeable."
---

# YouTube packaging

The script decides whether people finish. The packaging decides whether they
start. They are the same promise seen from two sides, and the most common failure
is a good video wearing a title nobody clicks, or a clickbait title attached to a
video that never delivers it.

## The one rule

Title, thumbnail and first 15 seconds must make **the same claim in three
different registers**. If they diverge, the viewer feels cheated at the exact
moment the video diverges — and that is where retention dies.

Practically: write the title, then the thumbnail text, then check that the cold
open delivers both within 15 seconds. If it cannot, the promise is wrong, not the
packaging.

## Titles

A title is a **promise in a noun phrase**, plus a reason to believe it. It is not
a summary and not a question the video never answers. The noun phrase is the one
deliberate exception to the continuous-sentence rule; everything else on this page
is written in complete, connected sentences.

Patterns that hold up:

| Pattern | Example | Why it works |
|---|---|---|
| Result + constraint | `A full media server on one laptop` | concrete noun, surprising limit |
| Cost / time | `My whole stack, set up in 40 minutes` | a number the viewer can price |
| Replacement | `This replaced my NAS` | implies a decision, not a tutorial |
| The objection | `Yes, you can run this without a server` | answers the doubt in the title |
| Numbered proof | `7 apps, one machine, zero subscriptions` | tricolon risk — use once |
| Named thing | `The media stack I actually keep running` | "actually" carries the honesty |

Rules that matter more than the pattern:

- **Concrete noun over abstraction.** "laptop" beats "solution". "40 minutes"
  beats "quickly".
- **No question the video doesn't answer.** "Is this the best media stack?" is a
  lie unless the video concludes it.
- **Front-load the searchable noun**, because the title gets truncated at ~60
  characters on mobile.
- **No emoji, no ALL CAPS words**, unless the channel already does that.
- **Do not repeat the thumbnail text.** Title and thumbnail are two halves of one
  sentence; together they should say more than either alone.

## Thumbnails

Judge a thumbnail at 120 px wide, because that is how most people will see it.

- **One subject.** A face, a logo, a screen, a device. Two subjects is a collage.
- **Three words maximum.** Often zero is better — the title carries the words.
- **Contrast by brightness, not by colour.** Phone screens are dim and outdoor
  viewers are half-blind; a dark thumbnail disappears.
- **The subject should be doing something**, not sitting in a screenshot. Play
  bars, cursors, red error text, an arrow — motion cues survive shrinking.
- **Keep text out of the bottom-right** (duration badge) and the top-right
  (progress bar on hover).

A useful test: put the thumbnail on a phone, look at it for one second, look away,
and say what it showed. If the answer is "a computer screen", it is not a
thumbnail yet.

## Descriptions

Two audiences read this: humans in the first two lines, and search engines in the
rest. Write for the human, and the rest follows.

```markdown
<Line 1: the promise, restated as a sentence. Same claim as the title.>
<Line 2: what the viewer will be able to do after watching.>

<2-4 sentence paragraph: what is in the video, what it cost, what broke, what you
would do differently. First person. No marketing language.>

Chapters
0:00 <beat name>
1:12 <beat name>

<Links: repo, docs, the thing mentioned. One line each, labelled.>

<Attribution / gear / "recorded on" line, if the channel does that>
```

- **Chapters from the script's beats**, not from the edit timeline. They should
  describe the viewer's progress, not your file names. Minimum four, each at least
  ten seconds long, starting at 0:00.
- **First 100 characters are what shows in search results.** Put the promise
  there.
- **Tags are near-worthless** for discovery. Three to five, no keyword stuffing.
- **No "in today's video we…"** — same rules as the script: see
  `video-script-writing/references/banned-words.md`.
- **Write prose, not clipped lines.** The description paragraph is complete,
  connected sentences with the facts joined, not a stack of one-line brags. Same
  rule as everywhere: `../voice-dna/references/continuous-prose.md`.

## Pinned comment and end screen

- **Pinned comment**: one concrete resource (repo, config, article) plus one
  question that invites a specific answer ("what did you point it at first?").
  Not "let me know what you think".
- **End screen**: point at one video, and it should be the *next step* of this
  one, not the most popular video on the channel. Sequence beats popularity.
- **Cards**: at most two, at the moment the viewer's question changes.

## Packaging pass

Before upload, check in this order:

1. **Does the title state a noun phrase the video actually delivers?**
2. **Would the thumbnail be legible at 120 px, in one second?**
3. **Do title, thumbnail and cold open all claim the same thing?**
4. **Do the chapters match what a viewer would look for, in their words?**
5. **Is there exactly one next step offered at the end?**
6. Run the description through `video-script-writing/scripts/check_script.py`.

## Chapters

Chapters are navigation, not a table of contents. A viewer scans them to decide
whether the part they need is in this video.

- **One title per section of the script**, in the viewer's words, not yours. "Add
  the download client", not "Section 3 — configuration".
- **Minimum four, each at least 10 seconds**, first one at `0:00`.
- **Read them in order**: they should describe the journey. If two consecutive
  titles could swap places, they are too vague.
- **Front-load the concrete noun** so the useful half survives truncation.
- **No numbering** unless the video is explicitly a numbered list.
- **No jokes.** Humour in a chapter title costs a second of comprehension for a
  half-second of amusement.

## Calls to action

Two placements, different jobs:

**Midroll (one, around 30–40% in).** Where the viewer has just got something
working and is feeling good. Never in the first minute, never during the payoff.
Four beats, in this order: *problem → solution → benefit → where*. Write them as
bullets; the creator freestyles the transition.

**End screen.** Not a CTA, a next step: what was just taught (one line), the bridge
to the next video, what they will see if they watch it, and a point at the card.
One video only. It should be the *next step* of this one, not the most popular
video on the channel.

No "smash the like button" in either. If the video earned it, they will.

## Thumbnail prompts for image generators

When the thumbnail has to be generated rather than photographed:

1. Start from a proven thumbnail in the niche, not from imagination.
2. List each element and its job (subject, expression, text, background, contrast).
3. Swap one element at a time — the subject or the text, never everything.
4. Write the prompt as a description of the **composition**, not a mood: "a laptop
   on a desk, screen glowing, dark room, one hand on the lid, shot from above,
   high contrast" beats "cinematic tech vibe".
5. When it comes back fake-looking, the usual cause is too many subjects or a
   face doing too much. Remove one.

If the thumbnail shows a screen, use a real screenshot composited in. Generated
screens are always wrong in a way viewers feel without being able to name.

## Deliverable

Return a block like:

```markdown
## Title
<primary>
<one alternate, different angle, not a rewording>

## Thumbnail
subject: <what is visible>
text: <0-3 words, or "none">
composition: <where the subject sits, what the eye hits first>

## Description
<as it would be pasted>

## Pinned comment
<one line>
```

Two title options maximum. More than two means the promise is not decided yet.

Related: `video-hooks` for the 15 seconds that must match this promise,
`video-outline` for the beats the chapters are cut from.
