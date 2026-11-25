---
name: voice-dna
description: "Capture how a specific creator actually talks, as a reusable persona brief: behavioural voice traits, sentence mechanics, vocabulary, banned words, reference passages, and delivery constraints such as a flat or monotone voice. Built from the creator's own transcripts rather than described in adjectives. Use when the user says the writing doesn't sound like them, wants a brand voice, tone of voice, style guide, persona, or 'sound like me', or before writing a batch of scripts so every video sounds like the same person."
---

# Voice DNA

"Write in a conversational tone" is a mood, not an instruction. Every model already
believes it is conversational. What reproduces a person is a set of **observable
habits**: how they open a sentence, what they do with a caveat, which words they
refuse, how long their sentences run, and how they end.

This skill produces two layers:

- **The floor** — patterns that are wrong for everyone. That lives in
  `video-script-writing/references/banned-words.md` and does not change per
  creator.
- **The ceiling** — how *this* creator writes. That is the brief this skill builds.
  Where the two disagree, the brief wins; it is tuned to a real person, the floor
  is tuned to what models do on autopilot.

## Where the evidence comes from

Never ask a creator to describe their own voice. They will say "casual but
professional" and mean nothing. Use artefacts:

1. **Unscripted recordings** — a call, a stream, a voice memo. Best evidence,
   because it captures speech rather than writing.
2. **Past video transcripts** — `.srt`/`.txt` beside their footage. The timing
   gaps even show where they pause.
3. **Their writing** — posts, docs, messages. Good for vocabulary, weak for rhythm.
4. **Creators they like** — name traits from them, never copy phrasing.

Two or three transcripts of 300+ words is enough. With nothing available, ask for
one voice memo answering: *"explain what you do to someone who just asked at a
party"* — that prompt produces natural speech with no performance.

## Extracting traits

Look for **repeated behaviour**, not one-offs. A trait needs three appearances to
be a trait.

| Look at | Example finding |
|---|---|
| Sentence openings | "So", "Okay so", "Look" — never "Furthermore" |
| Sentence length | varies with the thought; never turn an observed range into a cap |
| Caveats | stated plainly ("this isn't free") instead of hedged |
| Technical words | "box" not "server"; "it just works" not "seamless" |
| Person | talks to "you", not about "users" |
| Humour | dry, one line, self-deprecating, never at the viewer's expense |
| Numbers | rounded and spoken ("about twenty minutes") |
| Endings | stops on a concrete line, never summarises |
| Fillers | what they actually say when thinking ("um", "okay", "right") — cut from scripts, but they show the rhythm |

Write each trait as **a behaviour plus a counter-example**. The counter-example is
what makes it usable:

> Opens with a discourse marker ("so", "look") rather than a subject.
> Yes: "So the first thing that broke was Docker."
> No: "Docker was the first component to fail."

Five to eight traits. More than that and none of them are load-bearing.

## Delivery constraints

Voice is not only word choice. Capture how the person actually sounds, because it
changes what the words can do:

- **Energy level.** Flat and even, or animated? A flat narrator needs complete
  sentences that carry their own shape and understatement; an animated one can
  lean more on delivery. Length is not the lever in either case, and a fragment
  is still a fragment.
- **Range.** Can they do emphasis, sarcasm, warmth on demand? If not, nothing in
  the script may depend on it.
- **Pace.** Do they rush, or leave gaps? Gaps are cut points.
- **Accent and pronunciation.** Record every product name the way *they* say it,
  and use that spelling in the script.

If the voice is flat, write `delivery: flat` in the brief and read
`video-script-writing/references/delivery.md` before writing anything.

## The brief

`references/template.md` is the full layout. The structure:

```markdown
# <Name> — voice
## Who is talking          — role, audience, what they have actually done
## Delivery                — energy, range, pace, pronunciation
## Voice traits            — 5-8 behaviours, each with yes/no examples
## Sentence mechanics      — length, openers, person, tense, contractions
## Vocabulary              — words and phrases that are genuinely theirs
## Never uses              — personal additions to the ban list
## Structures              — the shape their best material takes
## Reference passages      — 3-5 verbatim excerpts, each with the move it shows
```

The reference passages are the highest-leverage part. A model imitates rhythm from
an example far more reliably than from an adjective.

An example of a completed brief for a flat, monotone narrator:
`references/bhavesh-singhal.md`.

## Applying it

The sentence rule comes before voice: write in complete, connected sentences and
never in a stack of fragments. `references/continuous-prose.md` holds the rule and
the before-and-after examples, and it applies to every skill that produces prose.

1. Draft without looking at the brief — over-consulting produces parody.
2. Re-read the draft against the traits one at a time. Which lines could not have
   been written by this person? Those are the rewrites.
3. Run `video-script-writing/scripts/check_script.py`.
4. Read the first and last line aloud. The opening should sound like them starting
   to talk; the ending like them stopping.

## Keeping it honest

- **Update from deletions.** Every phrase the creator cuts belongs on their banned
  list. The brief should drift toward their edits, not toward your taste.
- **Review quarterly.** Traits that stop being true become mannerisms.
- **One brief per channel.** Two channels with different voices is two briefs.
- **Borrow structure, never sentences.** A borrowed rhythm is homage; a borrowed
  line is theft.
