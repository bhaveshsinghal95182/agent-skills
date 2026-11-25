# Agent skills

A personal collection of 166 agent skills: Markdown instructions for Claude Code,
OpenCode and other harnesses that read a skills folder. The writing skills share
one rule, continuous sentences, defined in
[`skills/voice-dna/references/continuous-prose.md`](skills/voice-dna/references/continuous-prose.md).

## Install

```bash
git clone https://github.com/bhaveshsinghal95182/agent-skills.git
cd agent-skills
./install.sh
```

The installer symlinks every skill into `~/.agents/skills` and `~/.claude/skills`,
which is the layout this collection uses. It skips anything that already exists,
so running it on a machine with skills installed is safe.

Options:

- `--dry-run` prints what would be linked without changing anything.
- `--force` replaces an existing symlink. It refuses to replace a real directory,
  because that would delete local work.
- `--uninstall` removes only the symlinks that point into this checkout.
- `--help` prints the usage.

Set `AGENTS_SKILLS_DIR` or `CLAUDE_SKILLS_DIR` to install somewhere else.

## Layout

```
skills/<name>/SKILL.md
```

Some skills have references, scripts and assets beside `SKILL.md`. The whole
folder is linked, so those keep working.

## Find a skill

[`SKILLS.md`](SKILLS.md) lists all 166 skills with a one-line description and a
link to each `SKILL.md`.

## Updating

Run `git pull` in the checkout. The installed entries are symlinks, so new content
is live immediately. A skill added upstream needs `./install.sh` again to get a
link.

## Global writing rule

The skills work on their own. To make every agent in the account follow the same
writing rule outside a skill, append
[`extras/CLAUDE-writing-style.md`](extras/CLAUDE-writing-style.md) to
`~/.claude/CLAUDE.md` or to your global `AGENTS.md` once. It points at the three
source-of-truth files and states the continuous-sentence rule.

## Attribution

This is a personal collection, not a single-author project. Many skills come from
public packs and keep their original author metadata in the frontmatter, including
GSAP, Vercel, Neon, Remotion and Matt Pocock's skill packs. Where a skill carries
attribution, that attribution governs. Check the frontmatter before
redistributing a skill outside this repo.

Three Omarchy system skills (`diagnose-crash`, `omarchy`, `omarchy-app`) are
excluded because they live in `/usr/share/omarchy` and are symlinked into place by
the OS.
