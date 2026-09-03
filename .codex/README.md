# Codex configuration for this repository

Codex and Claude Code both work this repository. They read parallel instruction files and parallel
skill trees, carry identical research substance, and write into separate analysis slots so two
independent analyses never mix.

| | Codex | Claude Code |
|---|---|---|
| Instructions | `AGENTS.md` (`AGENT.md` symlinks to it) | `CLAUDE.md` |
| Skills | `.codex/skills/` | `.claude/skills/` |
| Skill invocation | `$draft Findings` | `/draft Findings` |
| Analysis slot | `A2`, at `/output/codes/A2/` | `A1`, at `/output/codes/A1/` |

## First-time setup

1. **Trust the project.** Already applied to `~/.codex/config.toml`:

   ```toml
   [projects."/Users/roomeyrahman/Documents/Research/CHI27/Older-Adult-A11ly"]
   trust_level = "trusted"
   ```

2. **Apply the project posture.** `.codex/config.toml` records the model, reasoning effort, and
   sandbox settings this work expects. Codex reads only `~/.codex/config.toml`, so either merge that
   block in or pass the values per run:

   ```bash
   codex -c model_reasoning_effort="high" -c sandbox_mode="workspace-write"
   ```

3. **Set up the style benchmark** once, before the first `$polish` run:

   ```bash
   python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
   ```

4. **Verify skill discovery.** Start Codex in the repository root and ask it to list its available
   skills. Eleven should appear: `plan-section`, `draft`, `revise`, `polish`, `grill`,
   `thematic-analysis`, `latex`, `chi-evidence-matrix`, `chi-literature-scout`,
   `chi-litreview-writer`, `chi-introduction`.

## Editing skills

`.claude/skills/` is the editing source of truth for skill text. `.codex/skills/` is generated:

```bash
bash .codex/sync-skills.sh          # regenerate .codex/skills from .claude/skills
bash .codex/sync-skills.sh --check  # fail if the Codex copies are stale
```

The script applies four rewrites, so the copies cannot drift in substance: `.claude/skills` paths
become `.codex/skills`, `CLAUDE.md` cross-references become `AGENTS.md`, Claude slash commands
(`` `/polish` ``) become Codex skill invocations (`` `$polish` ``), and the `thematic-analysis` slot
flips from `A1` to `A2`. Hand edits inside `.codex/skills/` are overwritten on the next run; make the
change in `.claude/skills/` and re-sync.

`AGENTS.md` and `CLAUDE.md` are maintained by hand, not generated. They keep identical section
numbering, so a rule cited as "Section 9.3" is the same rule in both. `AGENTS.md` adds Section 0,
which is Codex-only and has no counterpart in `CLAUDE.md`.

## Slot discipline

`bash .codex/skills/thematic-analysis/scripts/slot.sh` resolves the slot from the environment,
honours a `TA_SLOT` override, and exits 1 rather than guessing. Codex writes only inside `A2` and
does not read `A1` while producing its own analysis. Cross-slot comparison is a separate task with
its own instructions from the user.
