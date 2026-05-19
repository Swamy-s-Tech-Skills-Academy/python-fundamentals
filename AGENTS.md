# AGENTS.md

Repository agent guidance for automation and code assistants.

## Default Agent Responsibilities

1. Preserve existing educational structure and learner flow.
2. Make minimal, targeted edits unless broader refactors are explicitly approved.
3. Validate docs and code quality before finishing work.

## Required Checks Before Completion

1. `ruff check src/L1 src/L2`
2. `black --check tests`
3. `isort --check-only src/L1 src/L2`
4. `flake8 src/L1 src/L2`
5. `python -m compileall -q src/L1 src/L2`
6. `pytest -q`
7. `npx --yes markdownlint-cli2 "README.md" "docs/**/*.md" ".github/**/*.md"`
8. `./scripts/docs-links.ps1` (Docker required)

## Python Quality Scope

- Treat Python quality checks as scoped to formal curriculum paths: `src/L1` and `src/L2`.
- Keep `src/Working/` out of blocking quality gates unless a task explicitly includes Working paths.

## Current Test Coverage

- Keep existing smoke coverage in `tests/test_curriculum_smoke.py`.
- Maintain targeted behavioral tests in `tests/test_mini_projects.py` for:
  - `src/L1/S5/03_simple_calculator.py`: invalid-number text handling, operator validation, divide-by-zero path.
  - `src/L1/S10/profile_generator.py`: required-field validation and output structure checks.
  - `src/L2/S5/data_processor.py`: representative input-processing and summary-flow assertions.
  - `src/L2/S10/contact_manager.py`: add/search/update/delete workflow checks.

## CI Hardening Roadmap (Actions Pinning)

- Audit third-party GitHub Actions in `.github/workflows/*.yml` and pin each to immutable commit SHAs.
- Keep a companion comment with upstream version tags for readability.
- Refresh pinned SHAs on a scheduled cadence (e.g., monthly) or immediately for security advisories.
- Validate workflow behavior after each pin update before merge.

## Source Intake Policy

- `source-material/` is an internal, read-only intake folder for instructor notes.
- Publish-facing docs must be transformative and original.
- Avoid copying wording, sequence, or examples directly from intake notes.

## Python File Templates

- Use `docs/PythonFileTemplates.md` as the source of truth for Python file structure.
- Prefer the CLI lesson template for `src/Working/` and runnable lesson files in `src/L1/S5/` through `src/L1/S8/`.
- Preserve teaching-script files in earlier sessions unless the task explicitly calls for template conversion.
- Keep helper modules and app-style entry points on the helper/app template; do not force them into the CLI lesson template.

## `src/Working/` modification policy (Swamy-owned sandbox)

- **Do not** create, edit, move, rename, or delete files under `src/Working/` **unless Swamy explicitly asks** for that change in the current task (e.g. “update `src/Working/module3/02_sample.py`” or “add a draft under Working”).
- You may still **read** `docs/RepositoryStructure.md` (section **src/Working/**) for routing context when advising on promotion into `src/L{level}/S{session}/`.
- Routine automation (formatting entire `src/`, mass refactors) must **exclude** or skip `src/Working/` unless the task scope includes it by name.

## Session Bucket Safety Policy

- Treat `docs/meetup/L1/sessions.md` table as the delivery-status signal for Level 1 meetup sessions.
- New curriculum content derived from `source-material/` or `src/Working/` must be bucketed into planned/new sessions by default.
- Do not add new learning content to already completed sessions unless the user gives explicit approval in the current task.
- If session status is unclear, pause and ask permission before placing content.
- **Topic → folder map (L1 from `S5` onward):** `docs/RepositoryStructure.md` (section **src/Working/**)

## Notes

- This file is repository-local and complements `.github/copilot-instructions.md` and `CLAUDE.md`.
- If guidance conflicts, follow this precedence: `docs/RepositoryStructure.md` (structure source of truth) → `docs/PythonFileTemplates.md` (Python file shapes) → `.github/copilot-instructions.md` → `CLAUDE.md` → this file.
