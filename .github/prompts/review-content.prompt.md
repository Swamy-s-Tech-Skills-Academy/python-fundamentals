---
mode: agent
description: Audit session documentation and practice code for quality, correctness, and policy compliance.
---

# Review Content

You are auditing educational content in **Python Fundamentals** (**Python fundamentals only**).

## Required inputs (ask if not provided)

- **Scope** — level (`L1`), session (`L1/S3`), or `all`

## Workflow: OBSERVE → ANALYZE → REASON → VERIFY → ACT

### OBSERVE

List **every** file in scope — no sampling:

- Session docs: `docs/sessions/L{level}/`
- Practice files: `src/L{level}/S{session}/`

### ANALYZE

For each file:

- Session docs: overview, objectives, prerequisites, practice file refs, takeaways, links
- Practice files: header, runnable code, beginner comments, naming
- Cross-cutting: `L{level}/S{session}/` paths, zero-copy, session order, meetup status for placement

### REASON

Prioritise: **critical** (broken code, broken links) → **warning** (missing sections) → **info** (style).

### ACT

Fix critical issues; report summary table with file, issue, severity, status.

## Hard rules

- Review **every** file — never sample.
- Do not remove educational content — **split** instead.
- Formal paths only in publish-facing docs — not `src/Working/`.
