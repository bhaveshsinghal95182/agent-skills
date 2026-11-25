---
name: video-sound-branding
description: "Design the sonic identity of a channel: an intro sting (including late-90s rock/guitar stings), transition sounds, and how music sits under narration. Covers placement against the cold open, writing a 4-8 second sting, mixing and ducking rules, and when to use silence instead. Use when the user asks for an intro sound, theme, sting, bumper, sonic logo, background music plan, or says their videos feel flat or lack energy — especially when the narration is monotone and the energy has to come from somewhere else."
---

# Video sound branding

For a narrator with a flat or quiet delivery, sound is not decoration. It is where
the energy that the voice doesn't supply comes from. A 6-second guitar sting does
more for perceived production value than any amount of editing polish elsewhere,
because it is the one moment in the video that is allowed to be loud.

The rule that governs everything below: **sound marks structure, not mood.** A
sting says "section starts here". It does not say "be excited". That is why it
works under a monotone voice and fails under a hype one.

## The late-90s rock sting

What makes it recognisable, in order of importance:

1. **A single distorted guitar riff, 2–3 seconds**, low register, played on the
   lower strings. Drop-D or standard E, root-fifth-octave power chords only.
2. **A gated snare or a crash on the downbeat**, huge and short. The reverb is
   cut off rather than decaying — that gated sound is the era's fingerprint.
3. **A tape stop or a hard cut at the end**, not a fade. The era ended on a
   button press.
4. **No vocals, no melody above the third.** It is a texture, not a song.
5. **Loud, then silence.** The contrast with the following VO is the whole effect.

Modern equivalents (2010s+): sub bass drop, whoosh, single piano note. Those are
cheaper and quieter. A guitar sting is a deliberate throwback and it is the only
one that reads as "band" rather than "template".

## Structure of a 6-second sting

```
0.0 – 0.3   pickup: muted chug, or a single reverse-cymbal swell
0.3 – 3.5   the riff: 4 or 8 bars, tempo 110–140, ends on a held chord
3.5 – 4.2   crash + tape stop, or a hard gate to silence
4.2 – 6.0   silence, or a very low room tone
```

The silence at the end is not padding. It is the handoff back to the voice — if
the music is still ringing when the narrator starts, the first sentence gets
buried and the sting reads as amateur.

## Where it goes

```
0:00  cold open — picture, no music, one dry line
0:06  HARD CUT to sting + title card
0:12  sting ends, VO resumes
```

- **After the cold open, never before.** Opening on a sting delays the only thing
  that earns attention.
- **Once per video**, at the top. Reusing it mid-video makes the opening ordinary.
- **Hard cut in and out.** Fades belong to montages.
- **Land it on picture**, not on black. Title over the working result.
- **Duck it to −18 dB or lower** under any VO that overlaps, or don't overlap at
  all. Non-overlap is better.

## Transition sounds

At most two, used consistently, 0.2–0.5 s each:

- **A soft whoosh** for a section change, on the cut, not before it.
- **A click or tick** for a list item appearing on screen.

Consistency is the branding. A different sound for every transition is noise.

## Music under narration

- **Instrumental only.** Vocals fight speech for the same frequencies and the same
  attention.
- **−18 to −24 LUFS under speech**, ducked a further 3–6 dB on every syllable if
  the track has movement. If you can hear the melody while someone talks, it is
  too loud.
- **Silence is a tool.** Drop the music for the payoff line; the drop does more
  than any swell.
- **Match tempo to cut rhythm** if the edit is fast. Nothing exposes a slow edit
  like a fast track.

## Making one

Three routes, cheapest first:

**1. Synthesised.** Power chords are easy to fake: two or three detuned sawtooth
oscillators a fifth apart, hard-clipped, low-passed at ~4 kHz, gated at the end. A
snare hit is noise burst + short pitched body, gated to 120 ms. This sounds
convincingly like a 90s sting at 6 seconds and costs nothing. See
`scripts/make_sting.py` in this skill for a working generator.

**2. Sampled.** A royalty-free guitar loop, pitch-shifted to the key and cut to
the downbeat. Faster than recording, but check the licence — a sting is the most
recognisable 6 seconds in the video.

**3. Recorded.** DI guitar into an amp sim with a noise gate and a cab IR, one
take, doubled left and right. Best result; needs a guitar and an afternoon.

Whatever the route: **mono-compatible**. Check the mix in mono — half of viewers
are on a phone speaker, and wide doubled guitars collapse to a phasey mess.

## Checklist

- [ ] 4–8 seconds, no longer
- [ ] Starts and ends on a hard cut, not a fade
- [ ] Ends with ≥1 s of silence before the VO
- [ ] Loud enough to be the loudest moment in the video, short enough not to
      fatigue
- [ ] Mono-compatible
- [ ] Lands on picture, not black
- [ ] Used exactly once, at the same place, in every video
- [ ] No vocals, no melody that competes with speech

Related: `video-hooks` for the cold open that precedes it, `youtube-packaging` for
the title that lands over it, `video-music` for a full music bed under the narration.
