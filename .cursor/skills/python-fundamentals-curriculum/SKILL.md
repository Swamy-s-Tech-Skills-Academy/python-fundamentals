---
name: python-fundamentals-curriculum
description: >-
  Educational Python curriculum (levels L*, sessions in docs/sessions/, code in src/). Use
  when editing learning materials, session write-ups, practice files under src/L1 or src/L2,
  or structure/navigation that affects the course. Points to project rules; does not replace them.
---

# Python Fundamentals — workflow

**Python-only repository:** session docs, `src/L{level}/` practice scripts, meetup summaries under `docs/meetup/`, and Level 1–2 formal curriculum. Do not add or migrate AWS, cloud, Bedrock, or other non-Python course material.

## When to use

- `docs/sessions/`, `docs/images/`, `docs/RepositoryStructure.md`, or curriculum text in the repo root
- `src/L1/**`, `src/L2/**` practice scripts
- `README`, `AGENTS.md`, or `docs/RepositoryStructure.md` when the change is **about the course** (not a one-line typo you can fix inline)

## Before you edit: read the source of truth

1. **`AGENTS.md`** (root) — policies, ReAct/CoT, where rules and CI live
2. **`docs/RepositoryStructure.md`** — **authoritative** paths, naming, what exists; never invent `src/S1/`-style layout
3. Relevant **`.cursor/rules/*.mdc`** (especially `01_educational-content-rules` for teaching content, `04_markdown-standards` for docs, `03_quality-assurance` for `src/`)
4. **`CLAUDE.md`** for a short Claude-oriented brief if needed

## Non-negotiables

- **Zero-copy, transformative only** — no long verbatim third-party text; own examples; brief quotes with attribution. See `01_educational-content-rules.mdc`.
- **Do not “compress away” teaching** — split or continue in the next part instead of cutting pedagogy
- **Paths and numbering** — match `L{level}/S{session}/` in `src/` and numbered session files under `docs/sessions/`
- **`src/Working/` hands-off** — do not edit Working files unless Swamy explicitly requests that path in the current task
- **Session bucketing** — default new content to planned/new sessions; do not inject into completed sessions without explicit user approval

## Quality (when a significant doc or code change is done)

- Docs: `scripts/docs-lint.ps1` and `scripts/docs-links.ps1`, or the `npx`/Docker flow in `README.md`
- Python: `ruff check src/L1 src/L2`, `python -m compileall -q src/L1 src/L2`, and `pytest -q`

## If unsure

Re-read the structure doc, then the relevant rule file, then the files you will change.
