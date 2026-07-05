---
applyTo: src/**/*.py
---

# Python Practice File Instructions

These rules apply to every `.py` file under `src/L1` and `src/L2` (formal curriculum).

**Repository scope:** Python fundamentals curriculum only.

## Mandatory header

```python
# Filename: src/L{level}/S{session}/{nn}_{name}.py
```

The first line (`# Filename: ...`) is required. Session context on line 2 is encouraged.

## Code quality

- All code must **run without syntax errors** — no TODOs, no placeholder values.
- Use **beginner-level vocabulary**: avoid features not yet introduced in earlier sessions.
- Include **inline comments** that explain the *why* behind code decisions.
- Keep examples **minimal**: one concept clearly per file when possible.

## File naming

- Numeric prefix for ordered files: `01_`, `02_`, …
- Descriptive suffix in snake_case: `01_hello.py`
- Location: `src/L{level}/S{session}/` — never legacy `src/S{session}/`
- Non-numbered names allowed for intentional demos (e.g. `bytecode_demo.py` in S1)

## Linting

```bash
ruff check src/L1 src/L2
python -m compileall -q src/L1 src/L2
pytest -q
```

## Working sandbox

Do not edit `src/Working/` unless explicitly requested. Promote into formal paths instead.

## Reasoning standard

```text
THOUGHT: Why is this structure the right choice here?
ACTION:  Write code with a comment explaining the reasoning.
OBSERVE: Can a beginner understand the WHY, not just the WHAT?
```
