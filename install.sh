#!/usr/bin/env bash
#
# grok-sdlc-skills installer
# Copies the skills/ suite into a target agent's skills directory.
#
# Usage:
#   ./install.sh <target-skills-dir>
#
# Common target locations:
#   Claude Code : .claude/skills        (project) or ~/.claude/skills     (user)
#   Cursor      : .cursor/skills        (project) or ~/.cursor/skills     (user)
#   Grok        : .grok/skills          (project) or ~/.grok/skills       (user)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_SRC="$SCRIPT_DIR/skills"

TARGET="${1:-}"

if [ -z "$TARGET" ]; then
  cat >&2 <<'EOF'
Usage: ./install.sh <target-skills-dir>

Example:
  ./install.sh .claude/skills      # project-level Claude Code
  ./install.sh ~/.claude/skills     # user-level Claude Code
  ./install.sh ~/.cursor/skills     # Cursor
  ./install.sh ~/.grok/skills       # Grok
EOF
  exit 1
fi

if [ ! -d "$SKILLS_SRC" ]; then
  echo "Error: skills/ directory not found next to this script." >&2
  exit 1
fi

mkdir -p "$TARGET"
count=0
for d in "$SKILLS_SRC"/*/; do
  [ -d "$d" ] || continue
  name="$(basename "$d")"
  cp -R "$d" "$TARGET/$name"
  count=$((count + 1))
done

if [ "$count" -eq 0 ]; then
  echo "Warning: no skills found in $SKILLS_SRC" >&2
  exit 1
fi

echo "Installed $count skills into $TARGET"
