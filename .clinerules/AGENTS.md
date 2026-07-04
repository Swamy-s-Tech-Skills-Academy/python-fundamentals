# AGENTS.md — Cline Entry

**Canonical index:** root [`AGENTS.md`](../AGENTS.md).

**Repository:** `python-fundamentals`

Educational **Python Fundamentals** curriculum for Swamy's Tech Skills Academy. Documentation plus beginner-friendly practice scripts — not a web application.

## Python-only scope

All curriculum work belongs under `docs/sessions/`, `src/L{level}/`, and `docs/meetup/`. Do **not** add AWS, cloud, Bedrock, or other non-Python course material. `source-material/` is gitignored instructor intake — transform only, never copy verbatim.

## Read First

1. `AGENTS.md` — full agent map, ReAct/CoT, zero-copy and placement guardrails
2. `docs/RepositoryStructure.md` — authoritative paths, names, inventory
3. `.cursor/rules/*.mdc` — canonical modular rules
4. `.github/copilot-instructions.md` — Copilot-aligned policy
5. `CLAUDE.md` and `.claude/CLAUDE.md` — short Claude pointers

## Structure

```text
docs/sessions/L1/     src/L1/S1/     src/L2/S1/
docs/images/          scripts/
tests/                src/Working/   (hands-off unless Swamy asks)
```

## Cline Subagents

| Agent | Use when |
| --- | --- |
| `agent-ci-verify` | After docs, Python, or governance edits |
| `session-roadmap-review` | Reviewing session docs, plans, practice-file parity |
| `docs-originality-review` | Checking docs for zero-copy risk |

## CI Workflows

| Workflow | Scope |
| --- | --- |
| `docs-quality.yml` | Markdown lint + Lychee links |
| `python-quality.yml` | Ruff, compileall, pytest on `src/L1` + `src/L2` |

Local: `./scripts/docs-lint.ps1`, `./scripts/docs-links.ps1`, `ruff check src/L1 src/L2`, `pytest -q`.

## Do Not

- Edit `src/Working/` unless Swamy explicitly requests it.
- Add new content to completed meetup sessions without explicit approval.
- Use legacy `src/S1/` paths.
