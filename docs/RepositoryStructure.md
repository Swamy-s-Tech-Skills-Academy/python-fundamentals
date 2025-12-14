# 📋 Repository Structure

This document provides a detailed overview of the Python Fundamentals repository structure.

---

## 📁 Complete Repository Structure

```text
python-fundamentals/
├── 📚 docs/
│   ├── images/                 # Screenshots and educational images
│   │   └── S1/                 # Session 1 images
│   ├── RepositoryStructure.md  # This file
│   └── sessions/
│       └── L1/                 # Level 1: Noob → Nerd
│           ├── _Plan.md        # Complete Level 1 curriculum plan (sorts first)
│           ├── 01_S1.md        # Session 1: Python Introduction & Environment
│           ├── 02_S2.md        # Session 2: Variables & Data Types
│           ├── 03_S3.md        # Session 3: Operators & Expressions
│           ├── 04_S4.md        # Session 4: Conditionals & Modules
│           ├── 05_MP1.md       # Mini Project 1: Simple Calculator
│           ├── 06_S5.md        # Session 5: Loops & Iteration
│           ├── 07_S6.md        # Session 6: Debugging & Built-ins
│           ├── 08_S7.md        # Session 7: Lists & Loops
│           ├── 09_S8.md        # Session 8: Dictionaries & Testing
│           └── 10_MP2.md       # Mini Project 2: Profile Generator
├── 💻 src/
│   └── L1/
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
│       │   └── 03_fizzbuzz.py
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
│       │   └── simple_calculator.py
│       └── MP2/                # Mini Project 2
│           └── profile_generator.py
├── 🔧 scripts/                 # Development and utility scripts
│   ├── docs-lint.ps1           # Markdown linting script
│   ├── docs-links.ps1          # Link validation script
│   ├── show-tree.ps1           # Repository structure generator
│   └── repo-structure.txt      # Generated structure
├── ⚙️ .github/
│   ├── workflows/
│   │   └── docs-quality.yml    # CI/CD for documentation quality
│   └── copilot-instructions.md
├── 📄 README.md                # Main project README
├── 📄 LICENSE                  # MIT License
└── 📋 Configuration files      # .markdownlint*, lychee.toml, .gitignore
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
- **`repo-structure.txt`**: Generated structure output

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
`src/L1/MP1/simple_calculator.py`
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
| 5 | `05_MP1.md` | Mini Project: Calculator | 1 file |
| 6 | `06_S5.md` | Loops & Iteration | 3 files |
| 7 | `07_S6.md` | Debugging & Built-ins | 3 files |
| 8 | `08_S7.md` | Lists & Loops | 3 files |
| 9 | `09_S8.md` | Dictionaries & Testing | 3 files |
| 10 | `10_MP2.md` | Mini Project: Profile Generator | 1 file |

### Future Levels

- 🔄 **Level 2-9**: Planned for future development

---

## 🚀 Quick Navigation

- **Main README**: [README.md](../README.md)
- **Level 1 Plan**: [docs/sessions/L1/_Plan.md](sessions/L1/_Plan.md)
- **Session 1**: [docs/sessions/L1/01_S1.md](sessions/L1/01_S1.md)
- **Mini Project 1**: [docs/sessions/L1/05_MP1.md](sessions/L1/05_MP1.md)
- **Mini Project 2**: [docs/sessions/L1/10_MP2.md](sessions/L1/10_MP2.md)

---

**Last Updated**: December 2025
