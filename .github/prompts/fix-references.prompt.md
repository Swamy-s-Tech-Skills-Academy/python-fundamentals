---
mode: agent
description: Find and fix broken file paths, links, and cross-references across the repository.
---

# Fix References

You are correcting broken paths and links in **Python Fundamentals**.

## Authoritative source of truth

`docs/RepositoryStructure.md` — check the actual tree before changing any reference.

## Common error patterns

| Wrong (legacy) | Correct |
| --- | --- |
| `src/S1/01_hello.py` | `src/L1/S1/01_hello.py` |
| `docs/sessions/S1.md` | `docs/sessions/L1/S1.md` |

## Workflow

1. **SCAN** — find every file reference in scope (Markdown links, image refs, code comments).
2. **VERIFY** — each path resolves against the actual tree.
3. **FIX** — smallest targeted edit.
4. **VALIDATE** — `./scripts/docs-lint.ps1` and `./scripts/docs-links.ps1`

## Path rules

- Python practice: `src/L{level}/S{session}/`
- Session docs: `docs/sessions/L{level}/`
- Ordered practice files: `01_`, `02_`, …

Update `docs/RepositoryStructure.md` if any file was renamed or moved.
