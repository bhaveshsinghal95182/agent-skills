# Recording-ready script layout

Use this when the narration is going to be read by a person (or a voice actor).
It is deliberately boring: the narrator should never have to parse formatting
while talking.

```markdown
# <Video title> — voiceover

<One line: what this is, and what version of the cut it belongs to.>

**Format:** WAV, 48 kHz, mono or stereo.
**Where:** save into <folder>, named exactly `s1.wav`, `s2.wav`, ...
**Pace:** normal talking pace, ~135 words per minute.
**Pauses:** leave a beat between paragraphs, ~1 s of silence top and tail.
**Mistakes:** don't restart the take. Pause, repeat the sentence from the top.
Send a message when the files are in place.

---

## s1 — <beat name>
`s1.wav` · 84 words · ≈ 38 s

<Narration, one paragraph per block. Normal prose, not bullets.>

---

## s2 — <beat name>
`s2.wav` · 174 words · ≈ 77 s

<Narration.>

---

## Say it like this

| Written | Say |
|---|---|
| ProductName | “product-name” |
| 4040 | “four oh four oh” |
| API | “ay-pee-eye” |

**Not in this script:** <anything the narrator might expect but must not invent>
```

## Conventions

- **Section ids** (`s1`, `s3b`) so the edit survives re-recording one section.
- **Word count and length** beside every section: a take that runs 40% over is
  visible at a glance without playing it.
- **One paragraph per block.** Paragraphs are the natural cut points and the
  natural places for a breath.
- **Spell numbers and acronyms the way they are spoken.** The narrator should not
  be translating while reading.
- **State the retake policy.** Without it, narrators restart the whole take, and
  the one good sentence in the middle is lost.
- **End with what is deliberately missing.** A promised beat that never arrives
  gets improvised by the narrator, which is the one thing harder to edit than a
  long pause.
