#!/usr/bin/env bash
# Regenerate .codex/skills/ from .claude/skills/.
#
# .claude/skills/ is the editing source of truth for skill text. This script copies each skill
# into .codex/skills/ and applies the Codex-specific rewrites, so the two copies cannot drift:
#
#   .claude/skills   -> .codex/skills        (script paths inside the prose)
#   CLAUDE.md        -> AGENTS.md            (section cross-references)
#   `/skill-name`    -> `$skill-name`        (Claude slash command -> Codex skill invocation)
#   slot A1          -> slot A2              (thematic-analysis writes to the Codex slot)
#
# Run it after any edit to .claude/skills/. Nothing else writes .codex/skills/; hand edits there
# are overwritten on the next run.
#
# Usage:  bash .codex/sync-skills.sh [--check]
#   --check  regenerate into a temp dir and diff, exit 1 if .codex/skills is stale

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$ROOT/.claude/skills"
DST="$ROOT/.codex/skills"
CHECK=0
[ "${1:-}" = "--check" ] && { CHECK=1; DST="$(mktemp -d)/skills"; }

SKILL_NAMES=(plan-section draft revise polish grill thematic-analysis latex \
             chi-evidence-matrix chi-literature-scout chi-litreview-writer chi-introduction)

[ -d "$SRC" ] || { echo "[ERROR] no source skills at $SRC" >&2; exit 1; }

rm -rf "$DST"
mkdir -p "$DST"
cp -R "$SRC"/. "$DST"/

# --- rewrite markdown prose -------------------------------------------------
while IFS= read -r f; do
  perl -0pi -e 's{\.claude/skills}{.codex/skills}g;
                 s{CLAUDE\.md}{AGENTS.md}g;' "$f"
  for s in "${SKILL_NAMES[@]}"; do
    perl -0pi -e "s{\`/\Q$s\E\`}{\`\\\$$s\`}g; s{\`/\Q$s\E }{\`\\\$$s }g;" "$f"
  done
done < <(find "$DST" -name '*.md')

# --- rewrite scripts (path comments only; logic is agent-neutral) -----------
while IFS= read -r f; do
  perl -0pi -e 's{\.claude/skills}{.codex/skills}g;
                 s{CLAUDE\.md}{AGENTS.md}g;' "$f"
done < <(find "$DST" \( -name '*.py' -o -name '*.sh' \))

# --- Codex slot: thematic-analysis writes A2, not A1 ------------------------
TA="$DST/thematic-analysis/SKILL.md"
if [ -f "$TA" ]; then
  perl -0pi -e '
    s{\| Claude Code \| \*\*A1\*\* \| `/output/codes/A1/` \|\n\| Any other analysing agent \| \*\*A2\*\*, \*\*A3\*\*, \.\.\. \| `/output/codes/A2/`, \.\.\. \|}
     {| Codex | **A2** | `/output/codes/A2/` |\n| Claude Code | **A1** | `/output/codes/A1/` |\n| Any further analysing agent | **A3**, **A4**, ... | `/output/codes/A3/`, ... |}g;
    s{when you are Claude Code}{when you are Codex}g;
    s{`/output/codes/A1/study1/OA03/02-coding-table\.md`}{`/output/codes/A2/study1/OA03/02-coding-table.md`}g;
    s{`/output/codes/A1/FINAL-CODEBOOK\.md`}{`/output/codes/A2/FINAL-CODEBOOK.md`}g;
    s{Reading A2.s themes before writing A1.s}{Reading A1\x27s themes before writing A2\x27s}g;
    s{An explicit `--slot A2` in}{An explicit `--slot A1` in}g;
    s{quote_check\.py \. A1}{quote_check.py . A2}g;
    s{table_check\.py \. A1}{table_check.py . A2}g;
    s{anon_scan\.sh \. A1}{anon_scan.sh . A2}g;
    s{  A1/                    Claude Code.s analysis          }{  A2/                    Codex\x27s analysis                }g;
    s{  A2/                    another agent.s analysis        }{  A1/                    Claude Code\x27s analysis          }g;
    s{`/output/codes/A2/` knows}{`/output/codes/A1/` knows}g;
    s{\(A1 for Claude Code, A2 for others\)}{(A2 for Codex, A1 for Claude Code)}g;
    s{\[--slot A1\|A2\]}{[--slot A2|A1]}g;
  ' "$TA"
fi
perl -0pi -e "s{<!-- slot: A1 \|}{<!-- slot: A2 |}g;" "$TA"
CTM="$DST/thematic-analysis/references/code-theme-matrix.md"
[ -f "$CTM" ] && perl -0pi -e "s{\`A1/\` for Claude Code and \`A2/\` and beyond for other analysing agents}{\`A2/\` for Codex, \`A1/\` for Claude Code, and \`A3/\` and beyond for other analysing agents}g;" "$CTM"
SLOT="$DST/thematic-analysis/scripts/slot.sh"
[ -f "$SLOT" ] && perl -0pi -e "s{The skill exists as parallel copies in \.codex/skills \(Claude Code\) and \.codex/skills \(Codex\)}{The skill exists as parallel copies in .claude/skills (Claude Code) and .codex/skills (Codex)}g;
                                 s{SLOT=\\\$\(bash \.codex/skills/thematic-analysis/scripts/slot\.sh\)}{SLOT=\\\$(bash .codex/skills/thematic-analysis/scripts/slot.sh)}g;" "$SLOT"
RT="$DST/thematic-analysis/references/report-template.md"
[ -f "$RT" ] && perl -0pi -e "s{\`A1/\` for Claude Code and \`A2/\` and beyond for other analysing agents}{\`A2/\` for Codex, \`A1/\` for Claude Code, and \`A3/\` and beyond for other analysing agents}g;" "$RT"
TC="$DST/thematic-analysis/references/theme-construction.md"
[ -f "$TC" ] && perl -0pi -e "s{<!-- slot: A1 \|}{<!-- slot: A2 |}g;" "$TC"

find "$DST" -name '*.sh' -exec chmod +x {} \;

if [ "$CHECK" = "1" ]; then
  if diff -r -q "$ROOT/.codex/skills" "$DST" >/dev/null 2>&1; then
    echo "[OK] .codex/skills is in sync with .claude/skills"
  else
    echo "[STALE] .codex/skills differs from a fresh sync. Run: bash .codex/sync-skills.sh" >&2
    diff -r -q "$ROOT/.codex/skills" "$DST" || true
    exit 1
  fi
  exit 0
fi

echo "[OK] regenerated $(find "$DST" -name SKILL.md | wc -l | tr -d ' ') skills into .codex/skills"
