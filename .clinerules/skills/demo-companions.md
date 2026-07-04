---
name: curriculum-practice-parity
description: >-
  Verify session docs reference the correct src/L1 and src/L2 practice files;
  align _Plan.md and meetup status with on-disk inventory.
---

# curriculum-practice-parity (skill)

**Scope:** `python-fundamentals` only.

## When to use

- After adding or renaming practice files under `src/L1` or `src/L2`
- Before meetup delivery or when auditing doc ↔ code parity

## Checklist

1. Open `docs/RepositoryStructure.md` for expected file counts per session.
2. For each `docs/sessions/L{1,2}/S{n}.md`, every cited `src/L{level}/S{n}/` path exists and runs.
3. Cross-check `docs/sessions/L{level}/_Plan.md` three-axis status vs `docs/meetup/L{level}/sessions.md`.
4. Flag orphan files under `src/L1` / `src/L2` not referenced in session docs.
5. Do **not** treat `src/Working/` as publish-facing unless promoting with Swamy's approval.

## References

- Structure: `docs/RepositoryStructure.md`
- Subagent: `.clinerules/agents/session-roadmap-review.md`
