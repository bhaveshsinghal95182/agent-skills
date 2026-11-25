#!/usr/bin/env bash
# Link every skill in this checkout into ~/.agents/skills and ~/.claude/skills.
set -euo pipefail

REPO_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
SRC="$REPO_DIR/skills"
AGENTS_DIR="${AGENTS_SKILLS_DIR:-$HOME/.agents/skills}"
CLAUDE_DIR="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"

force=0
dry=0
uninstall=0

usage() {
  cat <<'EOF'
Usage: ./install.sh [--dry-run] [--force] [--uninstall]

  --dry-run    print what would happen, change nothing
  --force      replace an existing symlink; real directories are never replaced
  --uninstall  remove symlinks that point into this checkout

Environment:
  AGENTS_SKILLS_DIR   default: ~/.agents/skills
  CLAUDE_SKILLS_DIR   default: ~/.claude/skills
EOF
}

for arg in "$@"; do
  case "$arg" in
    --dry-run) dry=1 ;;
    --force) force=1 ;;
    --uninstall) uninstall=1 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "unknown option: $arg" >&2; usage >&2; exit 2 ;;
  esac
done

resolve() {
  (cd -- "$1" 2>/dev/null && pwd -P)
}

remove_link() {
  local target="$1" source="$2" raw="${3:-}"
  [ -L "$target" ] || return 1
  local text resolved base
  text="$(readlink -- "$target")"
  resolved="$(resolve "$target" || true)"
  base="$(resolve "$source" || true)"
  if [ "$text" = "${raw:-$source}" ] || { [ -n "$resolved" ] && [ "$resolved" = "$base" ]; }; then
    if [ "$dry" -eq 1 ]; then
      echo "remove $target"
    else
      rm -- "$target"
      echo "removed $target"
    fi
    return 0
  fi
  return 1
}

if [ "$uninstall" -eq 1 ]; then
  for dir in "$SRC"/*/; do
    name="$(basename "$dir")"
    remove_link "$CLAUDE_DIR/$name" "$dir" "$AGENTS_DIR/$name" || true
    remove_link "$AGENTS_DIR/$name" "$dir" "$dir" || true
  done
  exit 0
fi

mkdir -p -- "$AGENTS_DIR" "$CLAUDE_DIR"

linked=0
skipped=0

for dir in "$SRC"/*/; do
  name="$(basename "$dir")"
  agents_target="$AGENTS_DIR/$name"
  claude_target="$CLAUDE_DIR/$name"

  if [ -e "$agents_target" ] || [ -L "$agents_target" ]; then
    if [ -L "$agents_target" ] && [ "$force" -eq 1 ]; then
      [ "$dry" -eq 1 ] || rm -- "$agents_target"
      echo "replace $agents_target"
    elif [ -L "$agents_target" ]; then
      echo "skip  $agents_target (symlink exists; use --force to replace)"
      skipped=$((skipped + 1))
      continue
    else
      echo "skip  $agents_target (real directory exists; move it first)"
      skipped=$((skipped + 1))
      continue
    fi
  fi

  if [ "$dry" -eq 0 ]; then
    ln -s -- "$dir" "$agents_target"
  fi
  linked=$((linked + 1))

  if [ -e "$claude_target" ] || [ -L "$claude_target" ]; then
    if [ -L "$claude_target" ] && [ "$force" -eq 1 ]; then
      [ "$dry" -eq 1 ] || rm -- "$claude_target"
      echo "replace $claude_target"
    elif [ -L "$claude_target" ]; then
      echo "skip  $claude_target (symlink exists; use --force to replace)"
      continue
    else
      echo "skip  $claude_target (real path exists; move it first)"
      continue
    fi
  fi

  if [ "$dry" -eq 0 ]; then
    ln -s -- "$AGENTS_DIR/$name" "$claude_target"
  fi
done

echo "linked $linked skill(s), skipped $skipped"
[ "$dry" -eq 1 ] && echo "dry run: nothing changed"
