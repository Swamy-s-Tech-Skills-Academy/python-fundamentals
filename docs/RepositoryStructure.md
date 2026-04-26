# 📋 Repository Structure

This document provides a detailed overview of the Python Fundamentals repository structure.

---

## 📁 Complete Repository Structure

```text
python-fundamentals/
├── 📚 docs/
│   ├── 01_Python-Fundamentals-MasterPlan.md  # Complete 18-level course master plan
│   ├── images/                 # Screenshots and educational images
│   │   └── S1/                 # Session 1 images
│   ├── RepositoryStructure.md  # This file
│   └── sessions/
│       ├── L1/                 # Level 1: Noob → Nerd
│       │   ├── _Plan.md        # Complete Level 1 curriculum plan (sorts first)
│       │   ├── 01_S1.md        # Session 1: Python Introduction & Environment
│       │   ├── 02_S2.md        # Session 2: Variables & Data Types
│       │   ├── 03_S3.md        # Session 3: Operators & Expressions
│       │   ├── 04_S4.md        # Session 4: Conditionals & Modules
│       │   ├── 05_MP1.md       # Mini Project 1: Simple Calculator
│       │   ├── 06_S5.md        # Session 5: Loops & Iteration
│       │   ├── 07_S6.md        # Session 6: Debugging & Built-ins
│       │   ├── 08_S7.md        # Session 7: Lists & Loops
│       │   ├── 09_S8.md        # Session 8: Dictionaries & Testing
│       │   └── 10_MP2.md       # Mini Project 2: Profile Generator
│       └── L2/                 # Level 2: Nerd → Novice
│           ├── _Plan.md        # Complete Level 2 curriculum plan
│           ├── 01_S1.md        # Session 1: Sets & Tuples
│           ├── 02_S2.md        # Session 2: List Comprehensions
│           ├── 03_S3.md        # Session 3: Functions Basics
│           ├── 04_S4.md        # Session 4: Error Handling
│           ├── 05_MP1.md       # Mini Project 1: Data Processor
│           ├── 06_S5.md        # Session 5: Functions Parameters
│           ├── 07_S6.md        # Session 6: Functions Scope
│           ├── 08_S7.md        # Session 7: File Handling
│           ├── 09_S8.md        # Session 8: Modules Deep Dive
│           └── 10_MP2.md       # Mini Project 2: Contact Manager
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
│       ├── S5/                 # Session 5 practice files
│       │   ├── 01_for_loops.py
│       │   ├── 02_while_loops.py
│       │   └── 03_loop_controls_fizzbuzz.py
│       ├── S6/                 # Session 6 practice files
│       │   ├── 01_error_examples.py
│       │   ├── 02_debug_practice.py
│       │   └── 03_builtin_functions.py
│       ├── S7/                 # Session 7 practice files
│       │   ├── 01_list_basics.py
│       │   ├── 02_list_methods.py
│       │   └── 03_task_manager.py
│       ├── S8/                 # Session 8 practice files
│       │   ├── 01_dict_basics.py
│       │   ├── 02_dict_iteration.py
│       │   └── 03_gradebook.py
│       ├── MP1/                # Mini Project 1
│       │   ├── 01_simple_calculator.py
│       │   ├── 02_simple_calculator_loop.py
│       │   └── calculator_utils.py
│       └── MP2/                # Mini Project 2
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
│       ├── S5/                 # Session 5 practice files
│       │   ├── 01_basic_parameters.py
│       │   ├── 02_parameter_types.py
│       │   └── 03_return_values.py
│       ├── S6/                 # Session 6 practice files
│       │   ├── 01_local_scope.py
│       │   ├── 02_global_scope.py
│       │   └── 03_code_organization.py
│       ├── S7/                 # Session 7 practice files
│       │   ├── 01_reading_files.py
│       │   ├── 02_writing_files.py
│       │   └── 03_file_operations.py
│       ├── S8/                 # Session 8 practice files
│       │   ├── 01_creating_modules.py
│       │   ├── 02_name_main.py
│       │   └── 03_multi_file_project.py
│       ├── MP1/                # Mini Project 1
│       │   └── data_processor.py
│       └── MP2/                # Mini Project 2
│           └── contact_manager.py
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

- **`images/`**: Educational images organized by session (S1, S2, etc.)
- **`sessions/`**: Session documentation organized by level (L1, L2, etc.)
  - Each level contains:
    - `_Plan.md`: Complete level curriculum plan (underscore sorts first)
    - `01_S1.md`, `02_S2.md`, etc.: Numbered session documentation
    - `05_MP1.md`, `10_MP2.md`: Mini project documentation

### `src/`

Contains all practice code files:

- Organized by level (`L1/`, `L2/`, etc.)
- Each level contains session directories (`S1/`, `S2/`, `MP1/`, etc.)
- Practice files use numeric prefixes: `01_name.py`, `02_name.py`, etc.

### `scripts/`

PowerShell utility scripts for development:

- **`docs-lint.ps1`**: Markdown linting automation
- **`docs-links.ps1`**: Link validation using Lychee
- **`show-tree.ps1`**: Repository structure generator
- **Generated outputs**: Optional local structure snapshots (not committed by default)

### `.github/`

GitHub configuration:

- **`workflows/`**: CI/CD pipelines for quality assurance
- **`copilot-instructions.md`**: AI assistant guidelines

### `.cursor/`

Cursor AI configuration:

- **`rules/`**: Modular rule files for Cursor AI

---

## 📝 File Naming Conventions

### Python Practice Files

- Format: `{number}_{descriptive_name}.py`
- Examples: `01_hello.py`, `02_interactive_hello.py`, `03_type_conversion.py`
- Location: `src/L{level}/S{session}/` or `src/L{level}/MP{number}/`

### Session Documentation

- Format: `{number}_S{session}.md` or `{number}_MP{number}.md`
- Plan: `_Plan.md` (underscore prefix sorts first)
- Examples: `01_S1.md`, `05_MP1.md`, `_Plan.md`
- Location: `docs/sessions/L{level}/`

### Images

- Format: `{descriptive_name}.PNG` or `.png`
- Examples: `Help_V1.PNG`, `Py_Source_ByteCode.PNG`
- Location: `docs/images/S{session}/`

---

## 🔗 Path Reference Patterns

### Practice File References

```markdown
`src/L1/S1/01_hello.py`
`src/L1/MP1/01_simple_calculator.py`
`src/L1/MP1/02_simple_calculator_loop.py`
`src/L1/MP1/calculator_utils.py`
```

### Session Documentation References

```markdown
[Session 1](docs/sessions/L1/01_S1.md)
[Level 1 Plan](docs/sessions/L1/_Plan.md)
[Mini Project 1](docs/sessions/L1/05_MP1.md)
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
| 1 | `01_S1.md` | Python Introduction & Environment | 3 files |
| 2 | `02_S2.md` | Variables & Data Types | 3 files |
| 3 | `03_S3.md` | Operators & Expressions | 3 files |
| 4 | `04_S4.md` | Conditionals & Modules | 3 files |
| 5 | `05_MP1.md` | Mini Project: Calculator | 3 files |
| 6 | `06_S5.md` | Loops & Iteration | 3 files |
| 7 | `07_S6.md` | Debugging & Built-ins | 3 files |
| 8 | `08_S7.md` | Lists & Loops | 3 files |
| 9 | `09_S8.md` | Dictionaries & Testing | 3 files |
| 10 | `10_MP2.md` | Mini Project: Profile Generator | 1 file |

### Level 2 (Nerd → Novice) - ✅ Complete

| # | File | Topic | Practice Files |
|---|------|-------|----------------|
| - | `_Plan.md` | Level Overview | - |
| 1 | `01_S1.md` | Sets & Tuples | 3 files |
| 2 | `02_S2.md` | List Comprehensions | 3 files |
| 3 | `03_S3.md` | Functions: Definition & Basics | 3 files |
| 4 | `04_S4.md` | Error Handling: try/except | 3 files |
| 5 | `05_MP1.md` | Mini Project: Data Processor | 1 file |
| 6 | `06_S5.md` | Functions: Parameters & Return | 3 files |
| 7 | `07_S6.md` | Functions: Scope & Organization | 3 files |
| 8 | `08_S7.md` | File Handling: Read & Write | 3 files |
| 9 | `09_S8.md` | Modules Deep Dive | 3 files |
| 10 | `10_MP2.md` | Mini Project: Contact Manager | 1 file |

### Future Levels

- 🔄 **Level 3-18**: Planned for future development

---

## 🚀 Quick Navigation

- **Main README**: [README.md](../README.md)
- **Level 1 Plan**: [docs/sessions/L1/_Plan.md](sessions/L1/_Plan.md)
- **Level 2 Plan**: [docs/sessions/L2/_Plan.md](sessions/L2/_Plan.md)
- **L1 Session 1**: [docs/sessions/L1/01_S1.md](sessions/L1/01_S1.md)
- **L2 Session 1**: [docs/sessions/L2/01_S1.md](sessions/L2/01_S1.md)

---

**Last Updated**: April 2026
