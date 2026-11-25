---
name: video-music
description: "Write original background music for a narrated video from its script and the tone of the voiceover, then fit it under the narration. Use when the user asks for background music, BGM, an underscore, a soundtrack bed, music that matches the script or the voice, or says their video feels flat and needs music. Covers reading the project's transcript and voice tone, writing the brief, composing with the music-production skill, and placing and ducking the track in Slatey."
---

# Video music

Background music under narration has one job: carry the energy the voice does not, without
competing with it. The script decides where the music changes. The voice decides how much room it
gets.

This skill is the bridge between three things: the video's script and word timings, the measured
tone of the voiceover, and the `music-production` skill that writes the notes. Do not skip the
measurement and guess the mood from the title.

## 1. Read the project

For a Slatey project (`~/Videos/Projects/<Video>/`):

1. `project_files` to find the polished voiceover in `Media/Voiceover/`.
2. `transcript` for timed phrases: pause before each phrase, loudness against the speaker's median,
   words per second. Read the whole script before choosing anything.
3. `music_brief` on the same file. It returns:
   - the voice's delivery and pace, median loudness, spread and longest gap;
   - sections with start/end, mood, intensity and why;
   - tempo, key, instrumentation and a prompt for `music-production`.

`music_brief` is a starting point, not a verdict. Its moods come from word cues and relative
energy. Overrule it when the script says something it cannot hear: sarcasm, a deliberate pause, a
joke that needs silence.

If the project has a written script instead of a recording, use the script for structure and the
recording (or a sample) for tone. A script alone cannot tell you how loud or fast the voice is.

## 2. Turn tone into decisions

Match the arrangement to the delivery, not to the subject.

| Voice cue | What it means | Music response |
|---|---|---|
| Flat, even, little loudness change | The voice will not supply energy | Steady pulse, warm low-mid bed, clear but simple motif. Energy comes from arrangement and texture, not a busy melody. |
| Quiet, close-mic, low median | There is little headroom | Low-mid bed, soft highs, sparse notes. Leave 300 Hz–4 kHz to the voice. |
| Fast delivery, many words per second | The voice already fills the time | Do not match the tempo. Sustained figures, fewer notes, a beat below the speaking rhythm. |
| Wide loudness range | The voice already has a shape | Hold the arrangement steady. Save swells for section ends and the payoff, or they fight the voice. |
| Long pauses | The pause is doing work | Leave them open. Do not fill every gap with a fill or a new section. |
| Rising pitch or volume over a sentence | The sentence is building | A swell that peaks on its last stressed word, not earlier. |
| Questions | The viewer is being asked to think | Open voicings, suspended chords, no downbeat resolution. |
| Lists | The viewer is counting | One steady pulse or a light recurring figure. Do not introduce a new theme per item. |
| Reveal or payoff | The one place to spend energy | Drop out before it, or swell into it. One hit, then get out of the way. |

Pace and key:

- Keep the tempo below the speaking rhythm. A bed at the speaker's words-per-second rate sounds
  like it is racing the voice.
- Minor for tension and reflection; major for explanation, wonder and payoff. Relative major and
  minor are enough; do not modulate per section.
- One palette for the whole video. The same motif returning matters more than a new sound per
  section.

## 3. Structure from the script

- Sections of 15–60 s. Change only where the narration turns: a new question, a problem, a
  reveal, a payoff, a look back.
- Put every boundary on the first word of a phrase, never mid-sentence. `music_brief` already
  places them on phrase starts.
- If the video opens on a cold open, run it dry for the first line. Start the music on the cut or
  the title, not on black.
- End under the outro, or stop before the last line and let it land dry. Do not fade out over the
  final sentence.
- One energy peak. If everything swells, nothing does.

## 4. Compose with music-production

Use the `music-production` skill for the notes, sounds and render. Read its `SKILL.md` and the
`film-score.md` reference for underscore; use `electronic.md` or `beats.md` only when the video
really is that style.

Put the piece inside the video project so it travels with it:

```
<Video>/Media/Music/<piece>/
  song.json
  brief.md            the brief you were given, with any changes and why
  final/              the render you place in the mix
```

Start from the `music_brief` prompt. Keep its duration, section times, tempo and loudness target;
change the palette only when the tone table says so. Render with:

- instrumental only, no vocals;
- `target_lufs` around −18 (Slatey levels the bed again when it places it);
- true peak at or below −2 dBTP;
- 48 kHz, 24-bit WAV for the master you hand to Slatey.

Follow `music-production`'s own workflow: `studio.py doctor`, `validate`, `round` for revisions,
then `render` for the final. Do not deliver a draft. Pass the configuration the setup wrote; on
this machine that is `~/.music-skill/local-config.json`.

If the user has no `music-production` setup, say what it installs and how long it takes before
starting. Do not substitute a generated audio model without asking.

## 5. Place and duck it in Slatey

Call `place_music` with the mix and the rendered master:

```
place_music(
  name="main",
  project="<Video>",
  source="Media/Music/<piece>/final/master.wav",
  loop=true,
  start=0,
  fade_in=1.5,
  fade_out=2.5,
  target_lufs=-18,
  duck=true
)
```

- `place_music` loops with crossfades, trims to the mix length, levels the bed and puts it on the
  music track. The mix ducks it under the voice and lets it back up in pauses.
- Set `start` after a dry cold open. Leave `gain_db` alone unless the voice is unusually quiet or
  loud.
- Use `edit_mix` for a later change: clip gain, a shorter span, a different start. Do not re-render
  the whole piece for a level change.
- `render_mix` writes `Media/Mix/<name>-mix.wav` and stems. The music stem is the one to check if
  the bed is too busy.

## 6. Check before calling it done

- Music is instrumental, one palette, and changes only at phrase starts.
- Nothing new starts under the first line or the last line.
- The bed does not cover the voice: in the music stem, the loudest part should still sit under
  the voice's median. If the mix has a `problems` list, fix it before delivering.
- Mix loudness is around −16 to −14 LUFS with true peak at or below −1 dBTP.
- Sections in the finished piece match the brief's times. If they drifted, fix the piece, not the
  brief.
- You cannot hear the result. Report the measurements and ask the user to listen; do not describe
  how it sounds as if you had heard it.

## Checklist

- [ ] Transcript read end to end before choosing moods
- [ ] `music_brief` run and its tone numbers used
- [ ] Tempo below the speaking rhythm
- [ ] One palette, one energy peak
- [ ] Boundaries on phrase starts, never mid-sentence
- [ ] Cold open and final line left dry where they should be
- [ ] Master −18 LUFS, true peak ≤ −2 dBTP, 48 kHz
- [ ] `place_music` loops and levels the bed, ducking on
- [ ] Mix rendered, loudness and stems reported
- [ ] User asked to listen

Related: `music-production` for writing and rendering the piece, `video-sound-branding` for stings
and transition sounds, `video-script-writing` for the script's structure, `voice-dna` when the
delivery needs describing rather than measuring.
