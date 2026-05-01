# Claude Code Instructions — Python Fundamentals

**Project:** Python Fundamentals Curriculum (Swamy's Tech Skills Academy)
**Purpose:** Educational content development, session documentation, and practice code.

---

## 🚨 Critical Rules

1. **Zero-Copy Policy** — All educational content must be original and transformative. Never copy verbatim from transcripts, books, or third-party material. See `.cursor/rules/01_educational-content-rules.mdc`.
2. **Preserve existing structure** — Read the full file before editing. Make minimal, targeted changes.
3. **Do not corrupt content** — If a change feels broad or risky, ask first.

---

## 📁 Repository Structure (Quick Reference)

Full structure: `docs/RepositoryStructure.md` (single source of truth).

```text
python-fundamentals/
├── docs/
│   ├── 01_Python-Fundamentals-MasterPlan.md   # 18-level course roadmap
│   ├── RepositoryStructure.md                 # Authoritative structure doc
│   └── sessions/
│       ├── L1/   # Noob → Nerd (S1–S8, S5_MP1, S10_MP2, _Plan.md)
│       └── L2/   # Nerd → Novice
├── src/
│   ├── L1/       # Formal practice files: src/L1/S1/01_name.py
│   ├── L2/
│   └── Working/  # Sandbox staging area (see below)
│       ├── day1/ # Live-coding samples for Day 1
│       ├── day2/ # Live-coding samples for Day 2
│       └── dayN/
├── .cursor/rules/          # Cursor AI rule files
├── .github/
│   ├── copilot-instructions.md
│   └── workflows/
└── CLAUDE.md               # This file
```

---

## 🗂️ `src/Working/` — Sandbox Staging Area

`src/Working/dayN/` holds **informal live-coding samples** written during teaching sessions. Files here may be promoted to `src/L{level}/S{session}/` when ready.

### Working vs Formal

| `src/Working/dayN/` | `src/L{level}/S{session}/` |
|---|---|
| Informal, exploratory | Formal, tested, complete |
| Flexible names (`hello_world.py`) | Numbered names (`01_hello.py`) |
| Work-in-progress | Production curriculum |

### Promotion workflow (Working → Formal)

1. Identify the target `L{level}/S{session}/`.
2. Rename to `01_name.py` (next available number).
3. Add file header, clean comments, verify it runs.
4. Move to `src/L{level}/S{session}/`.
5. Reference the new file in `docs/sessions/L{level}/S{session}.md`.

### Standard file template

Modelled on `src/Working/day1/hello_world.py`:

```python
"""Module docstring — what this file demonstrates."""

import sys

HELP_TEXT = """script_name.py

Purpose
    One-line purpose.

Usage
    python script_name.py
"""

def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0
    # implementation here
    return 0

raise SystemExit(main(sys.argv))
```

### Rules for Claude

- ✅ Apply relaxed quality expectations to `src/Working/` files
- ✅ When asked to "bucket" / promote a Working file, follow the promotion workflow
- ✅ Source-material transcripts in `source-material/` are instructor notes — use them as inspiration only; transform ideas, never copy text
- ❌ Do **not** reference `src/Working/` paths in `docs/sessions/` — only promoted `src/L{level}/S{session}/` paths belong in session docs
- ❌ Do **not** treat CI lint failures on Working files as blockers

---

## 📝 Session Documentation (`docs/sessions/`)

- Every session doc must follow the structure in `.cursor/rules/01_educational-content-rules.mdc`.
- YAML frontmatter is optional; clear headings and educational flow are mandatory.
- Practice file references point to `src/L{level}/S{session}/` only.

## 💻 Practice Code (`src/L{level}/S{session}/`)

- Files named `01_name.py`, `02_name.py`, …
- All files must run without errors.
- Include a file-header comment: `# Filename: src/L1/S2/01_variables.py`.

---

## 🔗 Related Files

- **Cursor rules:** `.cursor/rules/` — full rule set for content creation, structure, QA
- **Copilot instructions:** `.github/copilot-instructions.md`
- **Structure doc:** `docs/RepositoryStructure.md`
- **Master plan:** `docs/01_Python-Fundamentals-MasterPlan.md`
