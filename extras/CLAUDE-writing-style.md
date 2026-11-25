# Writing style block

Append this block to `~/.claude/CLAUDE.md` (or to your global `AGENTS.md`) once
the skills are installed. It points at the three source-of-truth files in this
collection and states the non-negotiable continuous-sentence rule.

<!-- writing-style:start -->
## Writing style

This applies to everything I write with an agent — scripts, narration, titles,
descriptions, docs, commit messages, replies. Not just video work.

Three files are the source of truth, read them before writing anything long:

- `~/.agents/skills/voice-dna/references/continuous-prose.md` — the non-negotiable sentence rule: complete, connected sentences whose length follows the thought, no fragment stacks, no label stacks.
- `~/.agents/skills/video-script-writing/references/banned-words.md` — the ban list: AI tells, marketing speak, hedges, vague authority, structural repetition.
- `~/.agents/skills/voice-dna/references/bhavesh-singhal.md` — my voice. Flat delivery, continuous sentences, understatement, real specifics.

Rules that hold without being asked:

- **No AI tells.** No "not just X but Y", "here's the thing", "in today's fast-paced world", "let's dive in", "ultimately", or a closing paragraph that restates. If a sentence has a negated half, delete that half and check the sentence still works.
- **Plain nouns, real numbers.** Folder names, ports, minutes, gigabytes. Never seamless, robust, comprehensive, cutting-edge, leverage, elevate, unlock, empower.
- **Continuous sentences, always.** Every sentence carries a complete thought and connects to the next, and closely related facts join into one sentence instead of a fragment per line. Length follows the thought, not a word count or a breath. Never write a fact per line, never stack labels like "Problem: / Solution: / Tech:", and never let a fragment stand in for a sentence. Split only when the sentence becomes a run-on or the reader loses the thread.
- **Hedge only when it is true.** "Usually" about other people's setups is honest. Never hedge about what I did or saw.
- **End on a fact or an action, never a summary.**
- **Write for a flat voice.** No hype words (exciting, amazing, insane, incredible), no rhetorical questions, nothing that depends on vocal emphasis. A dry fact lands harder than an enthusiastic adjective.
- **Do not invent specifics.** If a number, name or quote is not in the source, leave it out or mark it `[need: …]`.

For anything longer than a paragraph, run the gate and fix the hits:

```
python3 ~/.agents/skills/video-script-writing/scripts/check_script.py <file>
```

Video work has a skill chain: `video-outline` → `video-hooks` → `video-script-writing` → `video-qc` → `youtube-packaging`, with `video-sound-branding` for the intro sting and `voice-dna` for the persona brief.
<!-- writing-style:end -->
