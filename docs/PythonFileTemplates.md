# Python File Templates

This repository intentionally uses a small set of Python file templates instead of forcing every lesson file into one shape.

The goal is consistency where it helps learners, without hiding beginner concepts behind unnecessary structure.

---

## Template 1: Teaching Script

Use this template for early beginner walkthroughs where top-level execution is part of the lesson.

### Teaching Script Use When

- The file is short and linear.
- Learners benefit from reading statements in execution order without function indirection.
- The script is a simple demonstration rather than a reusable command-line program.

### Teaching Script Shape

```python
# Filename: src/L1/S1/01_example.py
# Short lesson label

print("Demo output")
```

### Teaching Script Rules

- Include a `# Filename:` header.
- Keep the flow linear and readable.
- Prefer short explanatory comments that explain why, not obvious syntax.
- Do not add `HELP_TEXT`, `main(argv)`, or `SystemExit` unless the file is being promoted to Template 2.

---

## Template 2: CLI Lesson Script

Use this template for runnable lesson files, Working samples, reinforcement scripts, and interactive practice scripts.

### CLI Lesson Script Use When

- The file is meant to be run from the terminal.
- The script benefits from a help mode or a clear entry point.
- The lesson is large enough to justify named helper functions.
- The file will likely be reused, promoted, or expanded.

### CLI Lesson Script Shape

```python
"""Short module summary."""

# Filename: src/L1/S8/04_example.py

import sys

HELP_TEXT = """04_example.py

Purpose
    Explain what this script demonstrates.

Usage
    python src/L1/S8/04_example.py
"""


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("Lesson output")
    return 0


raise SystemExit(main(sys.argv))
```

### CLI Lesson Script Rules

- Include a module docstring.
- Include a `# Filename:` header below the docstring.
- Use `import sys`, `HELP_TEXT`, `main(argv: list[str]) -> int`, and `raise SystemExit(main(sys.argv))`.
- Keep helper functions above `main()`.
- Return an integer status code from `main()`.
- Use this as the default template for `src/Working/` and for later formal lesson files that are more than tiny linear demos.

---

## Template 3: Helper Module or App Entry Point

Use this template for importable helper modules and mini-project style application files.

### Helper module

Use for files that are primarily imported by other files.

```python
# Filename: src/L1/S5/calculator_utils.py

def helper() -> bool:
    return True
```

### App entry point

Use for application-style scripts where a classic `if __name__ == "__main__":` guard is clearer than lesson-style `HELP_TEXT`.

```python
"""Application entry point."""

# Filename: src/L2/S10/contact_manager.py

def main() -> None:
    print("Run app")


if __name__ == "__main__":
    main()
```

### Helper/App Rules

- Helper modules should be safe to import without side effects.
- App entry points should use a `main()` function and `if __name__ == "__main__":`.
- Do not force helper modules into the CLI lesson template.

---

## Current Cleanup Policy

- `src/Working/` should use Template 2 unless a file is intentionally a helper module.
- `src/L1/S5/` through `src/L1/S8/` should use Template 2 for runnable lesson scripts and Template 3 for helpers.
- Earlier beginner sessions may keep Template 1 where that supports the pedagogy.
- Avoid repo-wide mechanical rewrites outside the agreed folders unless explicitly requested.
