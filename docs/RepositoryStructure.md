# 📋 Repository Structure

This document provides a detailed overview of the Python Fundamentals repository structure.

## Agent and tool governance (mirrors)

| Layer | Path | Role |
| --- | --- | --- |
| **Canonical** | `AGENTS.md`, `.cursor/rules/`, `.cursor/skills/`, `.cursor/agents/` | Policies and curriculum skill |
| **Cline** | `.clinerules/` | Entry, agents, skills, workflows — must match canonical paths (`docs/RepositoryStructure.md`, `scripts/`) |
| **OpenCode** | `.opencode/` | Plugin config + same mirrors as Cline |
| **Copilot** | `.github/copilot-instructions.md`, `.github/prompts/`, `.github/instructions/` | In-IDE alignment |

If a mirror references another repo (`python-fundamentals-in-practice`), `docs/02_RepositoryStructure.md`, or `tools/psscripts/`, treat that as drift and fix the mirror — not this document.

## Two-repository model (workspace)

| Repository | Role |
| --- | --- |
| **`python-fundamentals`** (this repo) | **Single source of truth** for curriculum development — session docs, `src/L{level}/S{session}/`, master plan, intake migration, and meetup status tables |
| **`python-fundamentals-in-practice`** | **Meetup replica** — synced copy used for live meetup sessions; not the authoring source |

Develop and validate here first; prompt or sync scoped content into the meetup replica when ready for delivery.

**Meetup parity:** `docs/meetup/L1/sessions.md` in this repo and `python-fundamentals-in-practice` must stay identical — including status table, session agendas, and **event date/URL** fields after a session is scheduled or completed. Author meetup updates here first; if event details are captured during live delivery in the replica, back-sync them into this repo immediately.

---

## 📁 Complete Repository Structure

```text
python-fundamentals/
├── 📚 docs/
│   ├── 01_Python-Fundamentals-MasterPlan.md  # Complete 18-level course master plan
│   ├── images/                 # Screenshots and educational images
│   │   ├── S1/                 # Session 1 images
│   ├── meetup/                 # Meetup planning and scheduling notes
│   │   ├── L1/
│   │   │   └── sessions.md
│   │   ├── L2/
│   │   │   └── sessions.md
│   │   ├── L3/
│   │   │   └── sessions.md
│   │   ├── L4/
│   │   │   └── sessions.md
│   │   ├── L5/
│   │   │   └── sessions.md
│   │   ├── L6/
│   │   │   └── sessions.md
│   │   ├── L7/
│   │   │   └── sessions.md
│   │   ├── L8/
│   │   │   └── sessions.md
│   │   ├── L9/
│   │   │   └── sessions.md
│   │   ├── L10/
│   │   │   └── sessions.md
│   │   ├── L11/
│   │   │   └── sessions.md
│   │   ├── L12/
│   │   │   └── sessions.md
│   │   ├── L13/
│   │   │   └── sessions.md
│   │   ├── L14/
│   │   │   └── sessions.md
│   │   ├── L15/
│   │   │   └── sessions.md
│   │   ├── L16/
│   │   │   └── sessions.md
│   │   ├── L17/
│   │   │   └── sessions.md
│   │   └── L18/
│   │       └── sessions.md
│   ├── PythonFileTemplates.md  # Approved Python file templates for lessons and helpers
│   ├── RepositoryStructure.md  # This file
│   └── sessions/
│       ├── L1/                 # Level 1: Noob → Nerd
│       │   ├── _Plan.md        # Complete Level 1 curriculum plan (sorts first)
│       │   ├── S1.md        # Session 1: Python Introduction & Environment
│       │   ├── S2.md        # Session 2: Variables & Data Types
│       │   ├── S3.md        # Session 3: Operators & Expressions
│       │   ├── S4.md        # Session 4: Conditionals & Modules
│       │   ├── S5.md       # Session 5 - Mini Project 1: Simple Calculator
│       │   ├── S6.md        # Session 6: Loops & Iteration
│       │   ├── S7.md        # Session 7: Debugging & Built-ins
│       │   ├── S8.md        # Session 8: Lists, Iteration & String Sequences
│       │   ├── S9.md        # Session 9: Dictionaries & Testing
│       │   └── S10.md       # Session 10 - Mini Project 2: Profile Generator
│       └── L2/                 # Level 2: Nerd → Novice
│           ├── _Plan.md        # Complete Level 2 curriculum plan
│           ├── S1.md        # Session 1: Sets & Tuples
│           ├── S2.md        # Session 2: List Comprehensions
│           ├── S3.md        # Session 3: Functions Basics
│           ├── S4.md        # Session 4: Error Handling
│           ├── S5.md       # Mini Project 1: Data Processor
│           ├── S6.md        # Session 6: Functions Parameters
│           ├── S7.md        # Session 7: Functions Scope
│           ├── S8.md        # Session 8: File Handling
│           ├── S9.md        # Session 9: Modules Deep Dive
│           └── S10.md       # Mini Project 2: Contact Manager
│       ├── L3/                 # Level 3 planning scaffold
│       │   └── _Plan.md
│       ├── L4/                 # Level 4 planning scaffold
│       │   └── _Plan.md
│       ├── L5/                 # Level 5 planning scaffold
│       │   └── _Plan.md
│       ├── L6/                 # Level 6 planning scaffold
│       │   └── _Plan.md
│       ├── L7/                 # Level 7 planning scaffold
│       │   └── _Plan.md
│       ├── L8/                 # Level 8 planning scaffold
│       │   └── _Plan.md
│       ├── L9/                 # Level 9 planning scaffold
│       │   └── _Plan.md
│       ├── L10/                # Level 10 planning scaffold
│       │   └── _Plan.md
│       ├── L11/                # Level 11 planning scaffold
│       │   └── _Plan.md
│       ├── L12/                # Level 12 planning scaffold
│       │   └── _Plan.md
│       ├── L13/                # Level 13 planning scaffold
│       │   └── _Plan.md
│       ├── L14/                # Level 14 planning scaffold
│       │   └── _Plan.md
│       ├── L15/                # Level 15 planning scaffold
│       │   └── _Plan.md
│       ├── L16/                # Level 16 planning scaffold
│       │   └── _Plan.md
│       ├── L17/                # Level 17 planning scaffold
│       │   └── _Plan.md
│       └── L18/                # Level 18 planning scaffold (program capstone)
│           └── _Plan.md
├── 💻 src/
│   ├── L1/
│       ├── S1/                 # Session 1 practice files
│       │   ├── 01_hello.py
│       │   ├── 02_interactive_hello.py
│       │   └── bytecode_demo.py
│       ├── S2/                 # Session 2 practice files
│       │   ├── 01_variables.py
│       │   ├── 02_data_types.py
│       │   └── 03_type_conversion.py
│       ├── S3/                 # Session 3 practice files
│       │   ├── 01_arithmetic.py
│       │   ├── 02_comparisons.py
│       │   └── 03_mini_calculator.py
│       ├── S4/                 # Session 4 practice files
│       │   ├── 01_conditionals.py
│       │   ├── 02_boolean_logic.py
│       │   └── 03_number_guessing_game.py
│       ├── S5/             # Session 5 Mini Project 1
│       │   ├── 01_PEP8_naming_and_spacing.py
│       │   ├── 02_del_and_bool_arithmetic.py
│       │   ├── 03_simple_calculator.py
│       │   └── calculator_utils.py
│       ├── S6/                 # Session 6 practice files
│       │   ├── 01_for_loops.py
│       │   ├── 02_while_loops.py
│       │   ├── 03_loop_controls_fizzbuzz.py
│       │   ├── 04_calculator_loop.py
│       │   ├── 05_values_to_variables.py
│       │   ├── 06_chained_and_multi_assignment.py
│       │   ├── 07_conversion_limits.py
│       │   ├── 08_boolean_logic_precedence.py
│       │   └── 09_non_bool_values.py
│       ├── S7/                 # Session 7 practice files
│       │   ├── 01_error_examples.py
│       │   ├── 02_debug_practice.py
│       │   ├── 03_builtin_functions.py
│       │   ├── 04_pep8_style_refactor.py
│       │   ├── 05_pep8_indentation.py
│       │   ├── 06_print_sep_end.py
│       │   └── 07_escape_sequences.py
│       ├── S8/                 # Session 8 practice files
│       │   ├── 01_list_basics.py
│       │   ├── 02_list_methods.py
│       │   ├── 03_task_manager.py
│       │   ├── 04_string_basics.py
│       │   ├── 05_string_len.py
│       │   ├── 06_string_methods.py
│       │   ├── 07_string_replace.py
│       │   ├── 08_string_case_methods.py
│       │   ├── 09_string_strip_methods.py
│       │   ├── 10_string_indexing_and_slicing.py
│       │   ├── 11_string_format_method.py
│       │   ├── 12_f_strings.py
│       │   ├── 13_list_append_remove.py
│       │   ├── 14_list_insert_pop.py
│       │   ├── 15_list_sort_reverse.py
│       │   ├── 16_percent_formatting.py
│       │   └── 17_string_compound_operators.py
│       ├── S9/                 # Session 9 practice files
│       │   ├── 01_dict_basics.py
│       │   ├── 02_dict_iteration.py
│       │   └── 03_gradebook.py
│       └── S10/            # Session 10 Mini Project 2
│           └── profile_generator.py
│   └── L2/
│       ├── S1/                 # Session 1 practice files
│       │   ├── 01_sets_basics.py
│       │   ├── 02_tuples_basics.py
│       │   └── 03_conversions.py
│       ├── S2/                 # Session 2 practice files
│       │   ├── 01_basic_comprehensions.py
│       │   ├── 02_filtered_comprehensions.py
│       │   └── 03_practical_examples.py
│       ├── S3/                 # Session 3 practice files
│       │   ├── 01_basic_functions.py
│       │   ├── 02_reusable_functions.py
│       │   └── 03_organized_code.py
│       ├── S4/                 # Session 4 practice files
│       │   ├── 01_basic_error_handling.py
│       │   ├── 02_multiple_exceptions.py
│       │   └── 03_else_finally.py
│       ├── S5/             # Session 5 Mini Project 1
│       │   └── data_processor.py
│       ├── S6/                 # Session 6 practice files
│       │   ├── 01_basic_parameters.py
│       │   ├── 02_parameter_types.py
│       │   └── 03_return_values.py
│       ├── S7/                 # Session 7 practice files
│       │   ├── 01_local_scope.py
│       │   ├── 02_global_scope.py
│       │   └── 03_code_organization.py
│       ├── S8/                 # Session 8 practice files
│       │   ├── 01_reading_files.py
│       │   ├── 02_writing_files.py
│       │   └── 03_file_operations.py
│       ├── S9/                 # Session 9 practice files
│       │   ├── 01_creating_modules.py
│       │   ├── 02_name_main.py
│       │   └── 03_multi_file_project.py
│       └── S10/            # Session 10 Mini Project 2
│           └── contact_manager.py
│   ├── L3/                     # Future formal practice files (placeholder)
│   ├── L4/                     # Future formal practice files (placeholder)
│   ├── L5/                     # Future formal practice files (placeholder)
│   ├── L6/                     # Future formal practice files (placeholder)
│   ├── L7/                     # Future formal practice files (placeholder)
│   ├── L8/                     # Future formal practice files (placeholder)
│   ├── L9/                     # Future formal practice files (placeholder)
│   └── Working/                # Sandbox — bucketing guide: see § `src/Working/` below
│       ├── References.md
│       ├── module3/            # Informal drafts (promote into formal `src/L{level}/S{session}/`)
│       ├── module4/            # Informal drafts (promote into formal `src/L{level}/S{session}/`)
│       ├── module5/            # Informal drafts (promote into formal `src/L{level}/S{session}/`)
│       └── module6/            # Informal drafts (promote into formal `src/L{level}/S{session}/`)
├── 🧪 tests/
│   ├── test_curriculum_smoke.py  # Smoke: formal `src/L1` + `src/L2` files compile
│   └── test_mini_projects.py     # Behavioral regression tests for the mini projects
├── 🔧 scripts/                 # Development and utility scripts
│   ├── docs-lint.ps1           # Markdown linting script
│   ├── docs-links.ps1          # Link validation script
│   ├── show-tree.ps1           # Repository structure generator
│   └── (generated outputs)     # Optional local outputs from scripts (not tracked)
├── ⚙️ .github/
│   ├── workflows/
│   │   ├── docs-quality.yml    # CI/CD for documentation quality
│   │   └── python-quality.yml  # CI/CD for Python quality checks
│   └── copilot-instructions.md
├── 📄 README.md                # Main project README
├── 📄 LICENSE                  # MIT License
└── 📋 Configuration files      # .markdownlint*, lychee.toml, .gitignore, pyproject.toml
```

---

## 📂 Directory Descriptions

### `docs/`

Contains all educational documentation:

- **`images/`**: Educational images organized by session folders (see `docs/images/README.md` for required S1 assets)
- **`meetup/`**: Meetup planning/status files organized by level (`sessions.md` per level)
- **`sessions/`**: Session documentation organized by level (`L1`–`L2` complete; `L3`–`L18` level plans aligned to master plan; session docs pending)
  - Each level contains:
    - `_Plan.md`: Complete level curriculum plan (underscore sorts first)
    - `S1.md`, `S2.md`, etc.: Session documentation files
    - `S5.md`, `S10.md`: Mini project documentation

### `src/`

Contains all practice code files:

- Organized by level (`L1/`, `L2/`, etc.)
- Each level contains session-aligned directories (`S1/`, `S5/`, `S10/`, etc.)
- Practice files use numeric prefixes: `01_name.py`, `02_name.py`, etc.
- Python file shapes follow the three approved templates in `docs/PythonFileTemplates.md`
- Future levels `L3/` through `L18/` currently exist as `_Plan.md` scaffolds; formal `S{n}.md` and `src/L{n}/` content is pending.

### `src/Working/`

Sandbox staging area for **informal live-coding drafts** before promotion into formal `src/L{level}/S{session}/`.

- **`module3/`**, **`module4/`**, **`module5/`**, **`module6/`**: informal numbered samples (e.g. `01_sample.py`) staged before cleanup and promotion.
- **`References.md`**: links to source material and reference repositories.
- Working Python samples should default to the CLI lesson template in `docs/PythonFileTemplates.md`.

#### Topic → session routing (L1, from `S5` onward)

Intake notes in gitignored `source-material/Module3`–`Module6` map to Working lanes, then to formal sessions. Use this table when promoting or auditing migration — rewrite content; never copy intake verbatim.

| Working lane | Intake topics (summary) | Formal destination |
| --- | --- | --- |
| `module3/` | PEP 8 style; assignment patterns; type conversion; arithmetic; `print(sep=, end=)`; escape sequences | `S5` (PEP 8, `del`/bool), `S6` (optional assignment/conversion drills), `S7` (PEP 8 revisit, print/escape) |
| `module4/` | Boolean precedence; truthy/falsy; short-circuit evaluation | `S4` (core boolean logic), `S6/08`, `S6/09` (optional reinforcement) |
| `module5/` | Strings as sequences: operators, `len`, methods, indexing/slicing, formatting (`%`, `.format()`, f-strings) | `S8/04`–`S8/12`, `S8/16`–`S8/17` (optional string reinforcement) |
| `module6/` | Lists: creation, indexing, methods (`append`, `remove`, `insert`, `pop`, `sort`, `reverse`) | `S8/01`–`S8/03` (core), `S8/13`–`S8/15` (optional list-method drills) |
| *(no Working lane)* | Core loops, debugging, built-ins, dictionaries, `assert`, Profile Generator capstone | `S6/01`–`S6/04`, `S7/01`–`S7/03`, `S9/*`, `S10/*` (authored directly into formal paths) |

After promotion, Working copies may remain as instructor scratch until explicitly retired — do not reference `src/Working/` paths in publish-facing session docs.

### `tests/`

Lightweight **pytest** checks for repository health, including smoke compilation for formal curriculum files and targeted behavioral coverage for the mini projects. Does not replace running lesson scripts while learning.

### `scripts/`

PowerShell utility scripts for development:

- **`docs-lint.ps1`**: Markdown linting automation
- **`docs-links.ps1`**: Link validation using Lychee
- **`show-tree.ps1`**: Repository structure generator
- **Generated outputs**: Optional local structure snapshots (not committed by default)

### `.github/`

GitHub configuration:

- **`workflows/`**: CI/CD pipelines for quality assurance
- **`copilot-instructions.md`**: Internal contributor/automation guidance

### `.cursor/`

Cursor configuration:

- **`rules/`**: Modular internal rule files

---

## 📝 File Naming Conventions

### Python Practice Files

- Format: `{number}_{descriptive_name}.py`
- Examples: `01_hello.py`, `02_interactive_hello.py`, `03_type_conversion.py`
- Location: `src/L{level}/S{session}/` (including session-aligned mini-project folders such as `S5/` and `S10/`)

### Session Documentation

- Format: `S{session}.md`
- Plan: `_Plan.md` (underscore prefix sorts first)
- Examples: `S1.md`, `S5.md`, `_Plan.md`
- Location: `docs/sessions/L{level}/`
- Note: pedagogical session numbers can differ from filename order because mini projects are stored as `S5.md` and `S10.md` in the same sequence.

### Images

- Format: `{descriptive_name}.PNG` or `.png`
- Examples: `Help_V1.PNG`, `Py_Source_ByteCode.PNG`
- Location: `docs/images/S{session}/`

---

## 🔗 Path Reference Patterns

### Practice File References

```markdown
`src/L1/S1/01_hello.py`
`src/L1/S5/03_simple_calculator.py`
`src/L1/S5/calculator_utils.py`
```

### Session Documentation References

```markdown
[Session 1](docs/sessions/L1/S1.md)
[Level 1 Plan](docs/sessions/L1/_Plan.md)
[Mini Project 1](docs/sessions/L1/S5.md)
```

### Image References

```markdown
![Help System](../../images/S1/Help_V1.PNG)
```

---

## 📊 Current Repository Status

### Level 1 (Noob → Nerd) - ✅ Complete

| # | File | Topic | Practice Files |
|---|------|-------|----------------|
| - | `_Plan.md` | Level Overview | - |
| 1 | `S1.md` | Python Introduction & Environment | 3 files |
| 2 | `S2.md` | Variables & Data Types | 3 files |
| 3 | `S3.md` | Operators & Expressions | 3 files |
| 4 | `S4.md` | Conditionals & Modules | 3 files |
| 5 | `S5.md` | Mini Project: Calculator | 4 files |
| 6 | `S6.md` | Loops & Iteration | 9 files |
| 7 | `S7.md` | Debugging & Built-ins | 7 files |
| 8 | `S8.md` | Lists, Iteration & String Sequences | 16 files (3 list core + 13 optional string/list drills) |
| 9 | `S9.md` | Dictionaries & Testing | 3 files |
| 10 | `S10.md` | Mini Project: Profile Generator | 1 file |

### Level 2 (Nerd → Novice) - ✅ Complete

| # | File | Topic | Practice Files |
|---|------|-------|----------------|
| - | `_Plan.md` | Level Overview | - |
| 1 | `S1.md` | Sets & Tuples | 3 files |
| 2 | `S2.md` | List Comprehensions | 3 files |
| 3 | `S3.md` | Functions: Definition & Basics | 3 files |
| 4 | `S4.md` | Error Handling: try/except | 3 files |
| 5 | `S5.md` | Mini Project: Data Processor | 1 file |
| 6 | `S6.md` | Functions: Parameters & Return | 3 files |
| 7 | `S7.md` | Functions: Scope & Organization | 3 files |
| 8 | `S8.md` | File Handling: Read & Write | 3 files |
| 9 | `S9.md` | Modules Deep Dive | 3 files |
| 10 | `S10.md` | Mini Project: Contact Manager | 1 file |

### Future Levels (L3–L18)

Level plans live at `docs/sessions/L{level}/_Plan.md` (three-axis status: Curriculum / Delivery / Repository). Session docs and practice code are **planned**, not yet authored, except where noted in each level plan.

| Level | Plan | Stage |
| --- | --- | --- |
| 3 | [L3/_Plan.md](sessions/L3/_Plan.md) | Part 1 — OOP fundamentals |
| 4–6 | [L4](sessions/L4/_Plan.md) · [L5](sessions/L5/_Plan.md) · [L6](sessions/L6/_Plan.md) | Part 1 — design, data, SQLite |
| 7–12 | [L7](sessions/L7/_Plan.md) … [L12](sessions/L12/_Plan.md) | Part 2 — professional Python |
| 13–18 | [L13](sessions/L13/_Plan.md) … [L18](sessions/L18/_Plan.md) | Part 3 — systems engineering |

---

## 🚀 Quick Navigation

- **Main README**: [README.md](../README.md)
- **Level 1 Plan**: [docs/sessions/L1/_Plan.md](sessions/L1/_Plan.md)
- **Level 2 Plan**: [docs/sessions/L2/_Plan.md](sessions/L2/_Plan.md)
- **Level 3 Plan**: [docs/sessions/L3/_Plan.md](sessions/L3/_Plan.md)
- **Level 18 Plan (capstone)**: [docs/sessions/L18/_Plan.md](sessions/L18/_Plan.md)
- **Master plan**: [docs/01_Python-Fundamentals-MasterPlan.md](01_Python-Fundamentals-MasterPlan.md)
- **L1 Session 1**: [docs/sessions/L1/S1.md](sessions/L1/S1.md)
- **L2 Session 1**: [docs/sessions/L2/S1.md](sessions/L2/S1.md)

---

**Last Updated**: May 2026
