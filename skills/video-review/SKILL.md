---
name: video-review
description: "Critique a finished video, a rough cut, or a script against a fixed rubric: promise, first 15 seconds, pacing, clarity, AI tells, visuals and audio, with the five highest-impact fixes ranked. Use when the user asks to review, critique, audit, or give feedback on a video, cut, edit, script, or voiceover, or asks why a video is boring, confusing, too long, or not getting watched."
---

# Video review

A review that lists twelve problems is a review nobody acts on. The output is
**five ranked fixes**, each one specific enough to do in an afternoon, plus a
verdict on whether the video keeps its promise.

Judge the video for the audience it was made for, not for taste. "I would have
shot it differently" is not a finding.

## The rubric

Score each axis 1–5, then spend the words on the fixes, not the scores.

**1. Promise.** Is there one claim, and does the video deliver it?
- 5: title, opening, and ending make the same claim, and the claim is specific.
- 3: the claim exists but drifts; the middle covers something adjacent.
- 1: the video is about a topic, not a claim.

**2. First 15 seconds.** Does the viewer know what they are getting?
Result on screen, stake stated, no throat-clearing. A greeting costs 2 points.

**3. Pacing.** Narrated words per minute, dead air, and time-to-first-payoff.
- Over ~150 wpm or under ~100 wpm is usually wrong.
- More than 8 seconds with nothing changing on screen is a cut.
- The first payoff should arrive inside the first 20% of the runtime.

**4. Clarity.** Can a viewer who half-watched still follow the steps?
Every on-screen action named; no "as you can see"; numbers spoken the way they
are written; one connected idea per sentence, in complete sentences. A stack of
fragments is the first thing to flag here. The rule is in
`../voice-dna/references/continuous-prose.md`.

**5. AI tells.** Run `video-script-writing/scripts/check_script.py` on the
transcript. Hedges, closing summaries and "not just X but Y" are the ones that
hurt spoken narration most. Em-dash and tricolon density matter in the
description and on-screen text too.

**6. Picture.** Does every claim have something to look at?
Screens that are legible at 1080p on a phone, no 40-second stretches of one
static window, cuts on action not on breath, speed ramps that stay readable.

**7. Audio.** Levels, room tone, plosives, consistency between takes, and whether
the music sits under the voice or fights it.

## How to actually watch

Do not review from memory or from the script. Watch once at 1×, without pausing,
taking only timestamps of where attention drops. Then go back to those timestamps.
Reviewing frame by frame first is how you end up polishing a minute nobody
watches.

For a script-only review, read it aloud at the intended pace with a stopwatch.
Every stumble is a finding; every second over the target runtime is a beat to cut.

## Diagnostics

A few symptoms with non-obvious causes:

| Symptom | Usual cause |
|---|---|
| Retention cliff in the first 30 s | the promise is stated but not shown |
| Steady drip-off through the middle | no announced length, no open loops |
| Comments asking "what tool is that?" | the picture was never named by the VO |
| "Too long" comments on a 7-minute video | the map was missing, not the runtime |
| Views but no subscribers | the video stands alone with no next step |
| Good video, no clicks | title promises a topic; thumbnail shows a screenshot |

## Output format

```markdown
## Verdict
<one sentence: does it deliver the promise, and for whom>

## Scores
promise 3/5 · hook 2/5 · pacing 4/5 · clarity 5/5 · AI tells 2/5 · picture 3/5 · audio 4/5

## Five fixes, in order
1. **<fix>** — <what is wrong now, at <timestamp>, and the concrete change>
2. …

## Keep
<two or three things the edit already does well, so the next cut keeps them>
```

Rules for the fixes:

- **Ranked by impact**, not by how easy they are. A weak opening outranks a stray
  um.
- **Timestamped or line-numbered.** "The middle drags" is not a finding; "3:10 to
  3:48 is one static screen while the VO reads config aloud" is.
- **One sentence of cause, one of change.** No essays.
- **Do not propose a fix you cannot execute in a single pass.** "Reshoot the
  install" is not a fix; "cut 3:10–3:48 and keep the last four seconds" is.

## Honesty rules

- If the video is good, say so in the first line and stop. Padding a review with
  invented problems teaches the creator to distrust reviews.
- Never score the creator's personality, accent, or on-camera presence.
- If the review requires watching something you cannot access, say what you could
  and could not evaluate. Guessing at audio quality from a transcript is worse
  than admitting you did not hear it.

Related: `video-script-writing` for the write-up of any script fixes,
`video-hooks` for an opening rewrite, `youtube-packaging` if the problem is
upstream of the video.
