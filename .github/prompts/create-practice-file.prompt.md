---
mode: agent
description: Create a new Python practice file in the correct session src location.
---

# Create Practice File

You are adding a Python practice file to **Python Fundamentals** (**Python fundamentals only**).

## Required inputs (ask if not provided)

- **Level and target** — e.g. `L1/S3`
- **Concept to demonstrate**
- **File number** — next available `{nn}` in the target folder

## Authoritative path

`src/L{level}/S{session}/{nn}_{descriptive_name}.py`

Examples: `src/L1/S3/03_mini_calculator.py`, `src/L1/S5/03_simple_calculator.py`

## File template

```python
# Filename: src/L{level}/S{session}/{nn}_{name}.py
# Session {session}: {Title}

# <working code with educational inline comments>
```

## Rules

1. Header required — `# Filename:` on line 1.
2. Educational comments — explain *why*, not just *what*.
3. Working code only — no syntax errors, no TODOs.
4. Beginner vocabulary — no features not yet introduced.
5. Original examples — zero-copy policy.
6. Update the matching session doc under Practice Files.
7. Do not edit `src/Working/` unless explicitly requested.

## Quality

```bash
ruff check src/L1 src/L2
python -m compileall -q src/L1 src/L2
```
