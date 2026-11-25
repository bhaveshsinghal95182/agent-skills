---
name: video-script-writing
description: "Write narration for videos (demo, tutorial, review, launch, explainer) that a person can read aloud and an editor can cut to. Covers beat structure, body sections, the bullet/riff script format, writing to the clock, spoken-prose rules, delivery-aware writing for flat or monotone voices, a recording-ready handoff, and a banned-phrase gate. Use whenever the user asks for a video script, voiceover script, narration, VO, YouTube/Shorts/Reel script, or asks to rewrite, trim or punch up an existing script. Also use before recording a voiceover, because spoken prose needs a different edit than written prose."
---

# Video script writing

A script is instructions for two people: a voice that has to say it out loud, and
an editor who has to cut picture to it. Every rule here serves those two.

The failure mode is text that reads fine on a page and collapses when spoken:
sentences that run out of breath, abstract nouns nobody can picture, and
transitions nobody would say ("moreover, this underscores the importance of…").
If a line cannot be said in one breath, it is not a line yet.

**Continuous sentences are non-negotiable.** A script is still prose: every
sentence is complete and connected, and related facts join into one sentence
instead of a fragment per line. The breath rule splits run-ons; it is not a
licence to write fragments. The full rule, with examples, is in
`../voice-dna/references/continuous-prose.md`.

## Workflow

**1. Get the brief.** Who is watching, what they already know, the one promise, the
runtime, and **who is reading it**. The last one is the most often skipped and the
most expensive to ignore: writing for an expressive presenter and writing for a
flat, even delivery produce different sentences.

**2. Outline in beats, not paragraphs.** One line per beat: what the viewer learns
and what is on screen. Unpaired beats get cut here, which is cheaper than after a
VO is recorded. See `video-outline`.

**3. Write to the clock.** ~135 wpm for a relaxed explainer, ~150 for confident
marketing, ~110 for technical walkthroughs where the viewer needs to read the
screen. Multiply out before drafting.

**4. Say it out loud.** Read the draft aloud. Every stumble, stop, or re-read is a
place the narrator will stumble. Fix it in the text; never leave a note for the
talent.

**5. Run the gate.** `python scripts/check_script.py script.md`. Fix the flags,
re-run, ship. The list is in `references/banned-words.md`.

**6. Hand off record-ready.** One file per section, word count and estimated
length beside it, pronunciation table, retake policy. See
`references/script-template.md`.

## Structure

| Beat | Job | Typical length |
|---|---|---|
| Cold open | Show the finished result. No introduction. | 5–15 s |
| Promise | One sentence, stated as a noun. | 5 s |
| Map | The shape, before any detail. | 30–90 s (skip on shorts) |
| Body | The content, in the order a person would do it. | bulk |
| Payoff | The result again, now understood. | 10–20 s |
| Close | One concrete line. Callback, next action, provocation. | 5 s |

Two habits carry most of the quality:

- **Open on the result, not the setup.** First frame is the thing working.
- **Name the map early.** Viewers tolerate complexity when they know how much is
  left.

## Body sections

Every section is **hook → content → payoff**, and every section should survive as
a standalone clip once the transition words are removed.

**Hook (one sentence).** Sells the result of what is coming, never the mechanism.
If a viewer could read it and guess the lesson, it has leaked and needs rewriting.

**Content — pick the format that fits, not the default:**
- *Story* — setup → conflict → resolution → what it means
- *Analogy* — only when the idea genuinely has no concrete description
- *Framework* — name it, walk each part with one example, show the result
- *Combo* — story plus framework is the usual best answer

**Let the problem breathe.** If the section is about a problem, the problem gets at
least as much space as the fix. The fix is the least interesting part of any story
and the part viewers skip to.

**Payoff (1–2 lines).** Lands the lesson or opens a loop. Never summarises the
section, never hands off to the next one — that is the next section's hook's job.

**Length:** 200 words typical, 300 absolute for a section. Past that, it is two
sections wearing a coat.

## Writing for the mouth

**One connected idea per sentence.** Two clauses joined by "and" are usually two
sentences, but a fragment is never one of them. Keep the subject and the verb,
and join facts that describe the same action or decision. A breath is the limit,
not a target.

**Subject first.** "Claude pulled every image" not "Every image was pulled".

**Say numbers the way they are said.** "port seven eight seven eight",
"ten eighty p", "two hundred". Never make the narrator translate.

**Name what is on screen.** The words should name the window being shown. This is
what stops a screen recording from feeling like b-roll.

**Second person, present for facts, past for events.** "You ask for a movie" for
the general flow; "I had this running on Windows" for something that happened.
Model-default present tense throughout is the single most robotic narration tic —
diagnostic: would you say it that way out loud?

**No relative-clause stacking.** "The folder that the downloads land in, which is
also the one the library reads from" is three rewrites from "downloads and the
library share one folder".

**Front-load the point.** Spoken text cannot be re-read; the first four words
carry the meaning.

**Keep the mistakes.** If a step was messy, say so. Clean confidence about a messy
process is the fastest way to lose a technical audience.

## Delivery-aware writing

If the narrator is flat, monotone, or uncomfortable performing, read
`references/delivery.md` before drafting. The short version: no line may depend on
vocal emphasis, hype words read as sarcasm, and short, complete sentences do the work that
intonation would do.

If the narrator would rather riff than read, write the **bullet script** instead —
see `references/bullet-script.md`. Only the first line is word-for-word; the rest
is scannable bullets. It exists because word-for-word scripts come out stiff on
camera, and the stiffness lives in the joins between ideas.

## Writing to the clock

```
seconds ≈ words ÷ (wpm ÷ 60)        135 wpm → 2.25 words/second
```

Leave room: picture needs a beat at the start and end of each section, so a 90 s VO
sits inside a ~95 s section. If the target is 6 minutes and the draft is 9, **cut
beats** — never speed up the read. Fast narration is the most common reason a
video feels cheap.

## No fake examples

Never invent a case study, a quote, a number, or a client. If the source material
doesn't supply it, leave it out or mark it `[need: real number]` for the creator.
Fabricated specificity is the easiest thing for a viewer to catch and the most
expensive to recover from.

## On-screen cues

When a section will be filmed as a screen share, put the cue in the script:

```
**Beat 1 — the failure**
- I said the port was right. It wasn't.
- *(On-screen: settings page, port field showing 8080)*
```

## Handoff to recording

Deliver so the narrator thinks about nothing except talking:

- One block per section, with a suggested filename
- Word count and estimated length per section
- Format, sample rate, destination folder — once, at the top
- Pronunciation table for products, ports, initialisms
- Retake policy: pause, then repeat the sentence. Pauses are cut points.
- Anything deliberately absent, marked as absent

`references/script-template.md` has the layout.

## Self-check

1. Does the first sentence show the result or the setup?
2. Count sentences over 25 words. Split them.
3. Is every line a complete sentence, with related facts joined rather than
   scattered one per line?
4. Every number and acronym written the way it is spoken?
5. Any paragraph restating what the viewer just watched? Delete it.
6. `check_script.py` clean, or every hit consciously kept?
7. Word count ÷ 2.25 — is that the runtime asked for?
8. Could a stranger record this without asking a question?

## Related skills

`video-outline` for beats and the footage audit · `video-hooks` for the first 15
seconds · `voice-dna` for the persona brief · `video-qc` for a pass/fail review ·
`youtube-packaging` for the title and thumbnail · `video-sound-branding` for the
stinger.
