# agentic-core-context — Cline

**Repository:** `python-fundamentals` (**single source of truth** — Swamy-only development)

**Meetup replica:** `python-fundamentals-in-practice` — sync scoped content for live meetups; not the authoring source.

Educational Python fundamentals curriculum (L1–L18 roadmap; formal practice code L1–L2 today).

**Python-only boundary:** not for AWS, cloud, Bedrock, or other non-Python courses. Meetup tables live under `docs/meetup/L{level}/`. Transform `source-material/` intake only — never copy verbatim.

| Layer | Path | Role |
| --- | --- | --- |
| Structure | `docs/RepositoryStructure.md` | Paths, inventory, status |
| Agent entry | `AGENTS.md` | Policies, ReAct/CoT, CI checklist |
| Rules | `.cursor/rules/*.mdc` | Canonical modular rules |
| Skills | `.cursor/skills/python-fundamentals-curriculum/` | Curriculum editing skill |
| Tooling | `scripts/` | Docs lint/link helpers |
| Tests | `tests/` | pytest smoke + mini-project behavior |

## Local checks (formal curriculum)

```powershell
ruff check src/L1 src/L2
python -m compileall -q src/L1 src/L2
pytest -q
./scripts/docs-lint.ps1
./scripts/docs-links.ps1
```

Canonical policy wins over this mirror if anything conflicts.
