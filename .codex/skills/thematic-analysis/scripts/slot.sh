#!/usr/bin/env bash
# Print the analysis slot this agent writes to: A1 for Claude Code, A2 for Codex.
#
# The skill exists as parallel copies in .claude/skills (Claude Code) and .codex/skills (Codex); the slot is
# resolved at run time rather than hard-coded in two divergent copies.
#
# Resolution order:
#   1. TA_SLOT environment variable, if set (A1, A2, A3, ...)
#   2. first argument, if it looks like a slot
#   3. environment fingerprint: CLAUDECODE / CLAUDE_CODE_* / AI_AGENT=claude*  -> A1
#                               CODEX_* / AI_AGENT=codex*                     -> A2
#   4. unknown, prints nothing and exits 1, so the caller asks rather than guessing
#
# Usage:  SLOT=$(bash .codex/skills/thematic-analysis/scripts/slot.sh) || SLOT=ASK

set -uo pipefail

norm() { printf '%s' "$1" | tr '[:lower:]' '[:upper:]'; }

if [ -n "${TA_SLOT:-}" ]; then
  norm "$TA_SLOT"; echo; exit 0
fi

if [ "${1:-}" != "" ] && printf '%s' "${1:-}" | grep -qiE '^A[0-9]+$'; then
  norm "$1"; echo; exit 0
fi

agent="$(printf '%s' "${AI_AGENT:-}" | tr '[:upper:]' '[:lower:]')"

case "$agent" in
  claude*) echo A1; exit 0 ;;
  codex*)  echo A2; exit 0 ;;
esac

if [ "${CLAUDECODE:-}" = "1" ] || [ -n "${CLAUDE_CODE_SESSION_ID:-}" ] || [ -n "${CLAUDE_CODE_ENTRYPOINT:-}" ]; then
  echo A1; exit 0
fi

if [ -n "${CODEX_SANDBOX:-}" ] || [ -n "${CODEX_HOME:-}" ] || [ -n "${CODEX_SESSION_ID:-}" ]; then
  echo A2; exit 0
fi

exit 1
