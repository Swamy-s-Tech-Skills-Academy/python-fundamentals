---
name: ci-checks
description: Run CI-aligned checks for Python Fundamentals — Ruff, compileall, pytest, markdownlint, and Lychee. Use when asked to run CI, lint, or verify quality.
---

# CI Checks — Local Runner

Commands mirror `AGENTS.md` and `.github/workflows/*.yml`. Run from repository root.

## Policy

- Formal Python scope: `src/L1`, `src/L2`, and `tests/`
- Docs scope: `README.md`, `docs/**/*.md`, `.github/**/*.md`

## Checks (report PASS / FAIL / SKIP)

### Python

```powershell
ruff check src/L1 src/L2
black --check tests
isort --check-only src/L1 src/L2
flake8 src/L1 src/L2
python -m compileall -q src/L1 src/L2
pytest -q
```

### Docs

```powershell
./scripts/docs-lint.ps1
./scripts/docs-links.ps1
```

## Summary format

| # | Check | Status | Notes |
| --- | --- | --- | --- |
| 1 | ruff | | |
| 2 | black (tests) | | |
| 3 | isort | | |
| 4 | flake8 | | |
| 5 | compileall | | |
| 6 | pytest | | |
| 7 | markdownlint | | |
| 8 | Lychee | | |
