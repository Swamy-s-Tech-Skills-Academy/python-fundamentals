# Quality Assurance

Canonical detail: `.cursor/rules/03_quality-assurance.mdc`, `README.md`, and `.github/workflows/`.

- Python practice: `ruff check src/L1 src/L2`, `black --check tests`, `isort --check-only src/L1 src/L2`, `flake8 src/L1 src/L2`, and `python -m compileall -q src/L1 src/L2`.
- Tests: `pytest -q` (`tests/test_curriculum_smoke.py`, `tests/test_mini_projects.py`).
- Runtime smoke checks: use the calculator examples documented in `README.md` when relevant.
- Docs: `./scripts/docs-lint.ps1` and `./scripts/docs-links.ps1`.
- Links and paths must match real files under `docs/RepositoryStructure.md`.
- This repo has no frontend, FastAPI, or MCP server.
