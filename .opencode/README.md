# OpenCode — Python Fundamentals

OpenCode plugin config for **`python-fundamentals`**. Canonical governance: root `AGENTS.md`, `docs/RepositoryStructure.md`, `.cursor/rules/`, and `.github/copilot-instructions.md`.

**Python-only:** session docs (`docs/sessions/`), practice code (`src/L1`, `src/L2`), meetup summaries (`docs/meetup/`). Not AWS, cloud, Bedrock, or other non-Python tracks.

## Layout

```text
docs/sessions/L1/     src/L1/S*/     src/L2/S*/     scripts/
tests/                docs/meetup/   .cursor/rules/
```

## Rules

`rules/` contains OpenCode-facing summaries. Canonical rules remain `.cursor/rules/*.mdc`.

## Skills

See `skills/README.md`. Canonical project skill: `.cursor/skills/python-fundamentals-curriculum/SKILL.md`.

## Agents

| Agent | Use when |
| --- | --- |
| `agent-ci-verify` | After docs, Python, or governance edits |
| `session-roadmap-review` | Session docs, `_Plan.md`, meetup parity |
| `python-practice-code` | Creating or changing `src/L1` / `src/L2` practice files |
| `docs-originality-review` | Zero-copy / source-integrity risk in docs |

Legacy filenames `demo-roadmap-review` and `demo-code-audit` are retired — use the agents above.

## CI workflows

| Workflow | Scope |
| --- | --- |
| `python-quality.yml` | Ruff, compileall, pytest on `src/L1` + `src/L2` |
| `docs-quality.yml` | Markdown lint + Lychee links |

Local runners: `./scripts/docs-lint.ps1`, `./scripts/docs-links.ps1`, `skills/ci-checks/SKILL.md`.

## Package

`package.json` pins `@opencode-ai/plugin` for local OpenCode integration. `node_modules/` remains ignored by `.opencode/.gitignore`.
