# AGENTS.md

Repository agent guidance for automation and code assistants.

**Version:** 1.1  
**Last updated:** July 2026

---

## 1. What this repository is

- **Purpose:** Educational **Python fundamentals** curriculum (progressive levels, ~30-minute sessions, practice code under `src/`, session write-ups under `docs/sessions/`, meetup summaries under `docs/meetup/`).
- **Tone:** Beginner-friendly, hands-on, visually clear. Content must be **transformative**, not copied from third-party materials (see Zero-Copy Policy below).
- **Non-goals:** This is not a production app repository; code teaches concepts and must remain runnable and readable.

**Single source of truth for folder layout, naming, and file inventory:** `docs/RepositoryStructure.md` — when structure or conventions change, update that document first, then align references (README, copilot instructions, and this file).

---

## 2. Where project instructions live (use the right layer)

| Layer | Path | Role |
| --- | --- | --- |
| **Structure (authoritative)** | `docs/RepositoryStructure.md` | Definitive tree, naming, status |
| **Agent entry (this file)** | `AGENTS.md` | How agents should behave; pointers to all rules |
| **Skills pointer** | `skills.md` | Index; project skill in `.cursor/skills/python-fundamentals-curriculum/SKILL.md` |
| **Cursor subagents** | `.cursor/agents/*.md` | Optional custom subagents (session content, practice code, doc verification) |
| **Claude / Anthropic (short form)** | `CLAUDE.md` (repo root) | Condensed guardrails; same project as this file |
| **Claude Code folder (optional)** | `.claude/CLAUDE.md` | Confirms root instructions; use when tools expect `.claude/` |
| **Cursor (modular rules)** | `.cursor/rules/*.mdc` | Mandatory and scoped rules; see `.cursor/rules/README.md` |
| **GitHub Copilot** | `.github/copilot-instructions.md` | In-browser / Copilot alignment with Cursor rules |
| **Python file templates** | `docs/PythonFileTemplates.md` | Approved teaching-script, CLI lesson, and helper/app shapes |
| **CI (docs)** | `.github/workflows/docs-quality.yml` | Markdown lint + Lychee on doc paths |
| **CI (Python)** | `.github/workflows/python-quality.yml` | Ruff, compileall, pytest on formal curriculum paths |

If anything in this table conflicts with **`docs/RepositoryStructure.md`**, treat the doc as correct and fix the other file.

---

## 3. Reasoning: ReAct and Chain-of-Thought (CoT)

This project **expects explicit reasoning** in learning material and in agent work. Use the same patterns as in `.github/copilot-instructions.md` and `.cursor/rules/01_educational-content-rules.mdc` (which contain the full tables).

**Content creation (teaching material and examples):**  
**THINK → REASON → ACT → VERIFY** (and iterate if a verification step fails).

- **THINK (CoT):** Objectives, chunk the topic, order from simple to complex, anticipate misconceptions.
- **REASON:** Prerequisites, links to other sessions, original examples, pitfalls.
- **ACT:** Write docs, `src/` practice files, Mermaid-first diagrams with ASCII fallback, exercises.
- **VERIFY:** Clarity, completeness, fit in the sequence, originality (zero-copy).

**Content or repo review (audits, "review everything" requests):**  
**OBSERVE → ANALYZE → REASON → VERIFY → ACT**

- **OBSERVE:** List every file in scope (no sampling).
- **ANALYZE:** Open and check each file against the checklists in `03_quality-assurance.mdc` and `01_educational-content-rules.mdc`.
- **REASON:** Explain issues and patterns; do not skip edge cases.
- **VERIFY:** Cross-check paths, links, and naming.
- **ACT:** Fix or report with paths and clear follow-ups.

**Code edits in this repo (not "write a new session"):** default to **minimal, targeted diffs** — read surrounding context, preserve pedagogy and formatting, and do not rename or restructure files unless the user asked or it is required to fix a bug.

---

## 4. Default agent responsibilities

1. Preserve existing educational structure and learner flow.
2. Make minimal, targeted edits unless broader refactors are explicitly approved.
3. Validate docs and code quality before finishing work.

---

## 5. Required checks before completion

1. `ruff check src/L1 src/L2`
2. `black --check tests`
3. `isort --check-only src/L1 src/L2`
4. `flake8 src/L1 src/L2`
5. `python -m compileall -q src/L1 src/L2`
6. `pytest -q`
7. `npx --yes markdownlint-cli2 "README.md" "docs/**/*.md" ".github/**/*.md"`
8. `./scripts/docs-links.ps1` (Docker required)

---

## 6. Python quality scope

- Treat Python quality checks as scoped to formal curriculum paths: `src/L1` and `src/L2`.
- Keep `src/Working/` out of blocking quality gates unless a task explicitly includes Working paths.

---

## 7. Current test coverage

- Keep existing smoke coverage in `tests/test_curriculum_smoke.py`.
- Maintain targeted behavioral tests in `tests/test_mini_projects.py` for:
  - `src/L1/S5/03_simple_calculator.py`: invalid-number text handling, operator validation, divide-by-zero path.
  - `src/L1/S10/profile_generator.py`: required-field validation and output structure checks.
  - `src/L2/S5/data_processor.py`: representative input-processing and summary-flow assertions.
  - `src/L2/S10/contact_manager.py`: add/search/update/delete workflow checks.

---

## 8. CI hardening roadmap (Actions pinning)

- Audit third-party GitHub Actions in `.github/workflows/*.yml` and pin each to immutable commit SHAs.
- Keep a companion comment with upstream version tags for readability.
- Refresh pinned SHAs on a scheduled cadence (e.g., monthly) or immediately for security advisories.
- Validate workflow behavior after each pin update before merge.

---

## 9. Non-negotiable policies

### Source intake policy

- `source-material/` is an internal, read-only intake folder for instructor notes.
- Publish-facing docs must be transformative and original.
- Avoid copying wording, sequence, or examples directly from intake notes.

### Python file templates

- Use `docs/PythonFileTemplates.md` as the source of truth for Python file structure.
- Prefer the CLI lesson template for runnable lesson files in `src/L1/S5/` through `src/L1/S8/`.
- Preserve teaching-script files in earlier sessions unless the task explicitly calls for template conversion.
- Keep helper modules and app-style entry points on the helper/app template; do not force them into the CLI lesson template.

### `src/Working/` modification policy (Swamy-owned sandbox)

- **Do not** create, edit, move, rename, or delete files under `src/Working/` **unless Swamy explicitly asks** for that change in the current task.
- You may still **read** `docs/RepositoryStructure.md` (section **src/Working/**) for routing context when advising on promotion into `src/L{level}/S{session}/`.
- Routine automation (formatting entire `src/`, mass refactors) must **exclude** or skip `src/Working/` unless the task scope includes it by name.

### Session bucket safety policy

- Treat `docs/meetup/L1/sessions.md` table as the delivery-status signal for Level 1 meetup sessions.
- New curriculum content derived from `source-material/` or `src/Working/` must be bucketed into planned/new sessions by default.
- Do not add new learning content to already completed sessions unless the user gives explicit approval in the current task.
- If session status is unclear, pause and ask permission before placing content.
- **Topic → folder map (L1 from `S5` onward):** `docs/RepositoryStructure.md` (section **src/Working/**)

---

## 10. Cursor rules: reading order

1. `05_primary-directives.mdc` — what to do first, automation, update protocol
2. `01_educational-content-rules.mdc` — zero-copy, CoT/ReAct, session structure
3. `02_repository-structure.mdc` — context and links to the structure doc
4. `04_markdown-standards.mdc` — links, encodings, session doc shape
5. `03_quality-assurance.mdc` — checklists before commit
6. `06_cross-level-integration.mdc` — prerequisites and "enables" links between sessions

---

## 11. When unsure

Prefer **ask** over **guess** on large pedagogical rewrites, licensing-sensitive material, or repo-wide moves. For small, mechanical fixes (typos, broken links, wrong paths), fix and run lint/link checks when docs are touched.

---

**Bottom line:** Treat `docs/RepositoryStructure.md` as the map, `.cursor/rules/` and `.github/copilot-instructions.md` as the detailed law, and **AGENTS.md** / **CLAUDE.md** as the compass for any automated assistant in this repository.

**Precedence on conflict:** `docs/RepositoryStructure.md` → `docs/PythonFileTemplates.md` → `.github/copilot-instructions.md` → `CLAUDE.md` → this file.
