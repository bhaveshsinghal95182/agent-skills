---
name: video-qc
description: "Run a pass/fail quality check on a script artefact before it goes further: outline, hook, intro, or body section. Each mode has hard checks (leak test, title-sequence test, cold-open test, word counts, anti-slop gate) and returns a fixed report with fixes, not opinions. Use when the user asks to check, QC, review, audit, validate, or sign off on an outline, hook, intro, or section, or before recording/animating anything so defects are caught on text rather than in the edit."
---

# Video QC

Reviewing your own draft is unreliable: you read what you meant. QC is a fixed
list of checks applied in a fixed order, so the defects that survive are the ones
that were chosen.

Four modes. Read the section you need; they share the mechanics and anti-slop
checks at the end.

**Always run the anti-slop gate**, in every mode:

```bash
python ../video-script-writing/scripts/check_script.py <file>
```

**Continuous sentences are a check in every mode.** A hook, roadmap or payoff
made of fragments fails, however short the line looks. The rule and examples are
in `../voice-dna/references/continuous-prose.md`.

## Mode 1 — Outline

Source: `video-outline`.

1. **Question chain.** Read the point titles in order. Does each one raise a
   question the next answers? A list of topics fails.
2. **Core claim audit.** Write the single claim of each point in one line. Any two
   lines that are the same claim = merge.
3. **Title sequence test.** The titles alone should tell the story. If they read
   like "Introduction / Overview / Setup", the points are topics.
4. **Unique jobs.** Assign Setup / Mechanism / Proof / Reframe / Fix / Close. Two
   points with the same job are one point.
5. **Vagueness.** A point that cannot be filmed ("understand the philosophy") gets
   cut or made concrete.
6. **Count.** 7–10. Under 6 is thin; over 10 is two videos.

## Mode 2 — Hook (a body-section hook)

1. **Length.** One sentence, two at most.
2. **Leak test — the most important check.** Could a viewer read the hook and
   guess the section's lesson? If yes, rewrite. The hook sells the result, never
   the mechanism.
3. **Real curiosity.** The gap must be one only the section closes — not a vague
   tease.
4. **Specific enough to be real.** A number, a screen, a moment. "It got weird"
   fails; "it asked for a password it printed three lines earlier" passes.
5. **Cold open test.** Remove "so", "but", "and then". Does it still stand?
6. **Transition.** Does it flow from the previous section's last line without
   restarting the video?
7. **No repetition** of a tease already used earlier in the script.

## Mode 3 — Intro

1. **Title congruence.** The intro's promise is the title's promise. If not, one of
   them is wrong.
2. **Specific opening moment.** A scene, a number, a failure — not a description of
   the topic.
3. **Credibility shown, not claimed.** No "as a 10-year expert". The specifics do
   the work.
4. **Invalidation present.** Some default belief or advice gets named and
   contradicted. Without it the video is optional viewing.
5. **Concrete stakes.** What it costs to not know this. Money, an afternoon, a
   broken setup.
6. **Roadmap last, 2–3 items**, written as spoken clauses ("First, X. Then, Y."),
   not fragments.
7. **No fluff lines.** Every sentence either advances the promise or gets cut.
8. **Length.** Hook + invalidate 50–80 words; roadmap 2–3 lines.
9. **Flat-voice test** (if the narrator is low-affect): could this be read in the
   most bored voice imaginable and still land?

## Mode 4 — Body section

1. **One idea.** If you can summarise the section in two unrelated sentences, it is
   two sections.
2. **First person.** What happened, not what generally happens.
3. **Story or observation before the lesson.** The lesson lands after the evidence.
4. **The problem gets space.** At least as much as the fix.
5. **Tease → tension → reveal.** The reveal must not arrive in the first two lines.
6. **No closing recap, no bridge to the next section.** Both belong to other
   components.
7. **No repetitive list structure.** Three parallel beats with the same shape is a
   list wearing prose.
8. **Specific detail present.** A port, a number, a folder, a failure.
9. **Continuous sentences.** Every line is complete and connected. A fragment
   stack ("Four runtimes. Fifty runs. One bug.") is a fail, and so is a "Problem:
   / Solution:" stack outside a real list. A long sentence is not a fail by
   itself. See `../voice-dna/references/continuous-prose.md`.
10. **Paragraph format**, not bullets, unless the format is a deliberate framework.
11. **Word count.** 200 typical, 300 max.

## Report format

```
## <artefact> — <mode>
verdict: pass / pass with fixes / fail

### Failed checks
- <check number and name> — <what is wrong, quoted> → <the fix>

### Passed
<one line listing check numbers that passed, so the creator knows what not to touch>
```

Rules for the report:

- **Quote the offending line.** "The hook leaks" is not a finding.
- **One fix per failure**, not a rewrite of the whole piece.
- **Verdict first.** The creator should know in one word whether to proceed.
- **Never fail something for taste.** If the voice file allows dryness, a dry line
  is not a defect. This is why the anti-slop list is a floor and the voice brief is
  the ceiling.
- **If everything passes, say so and stop.** Invented notes teach the creator to
  ignore reviews.

Related: `video-script-writing` to apply the fixes, `video-review` for a whole
finished video rather than one artefact.
