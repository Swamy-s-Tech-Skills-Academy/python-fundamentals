# AGENTS.md

Repository agent guidance for automation and code assistants.

## Default Agent Responsibilities

1. Preserve existing educational structure and learner flow.
2. Make minimal, targeted edits unless broader refactors are explicitly approved.
3. Validate docs and code quality before finishing work.

## Required Checks Before Completion

1. `ruff check src`
2. `python -m compileall -q src`
3. `npx --yes markdownlint-cli2 "README.md" "docs/**/*.md" ".github/**/*.md"`
4. `./scripts/docs-links.ps1` (Docker required)

## Source Intake Policy

- `source-material/` is internal instructor intake.
- Publish-facing docs must be transformative and original.
- Avoid copying wording, sequence, or examples directly from intake notes.

## Session Bucket Safety Policy

- Treat `docs/meetup/L1/meetup-sessions.md` table as the delivery-status signal for Level 1 meetup sessions.
- New curriculum content derived from `source-material/` or `src/Working/` must be bucketed into planned/new sessions by default.
- Do not add new learning content to already completed sessions unless the user gives explicit approval in the current task.
- If session status is unclear, pause and ask permission before placing content.
- **Topic → folder map (L1 from `S5_MP1` onward):** `src/Working/README.md`

## Notes

- This file is repository-local and complements `.github/copilot-instructions.md` and `CLAUDE.md`.
- If guidance conflicts, follow this precedence: `docs/RepositoryStructure.md` (structure source of truth) → `.github/copilot-instructions.md` → `CLAUDE.md` → this file.
