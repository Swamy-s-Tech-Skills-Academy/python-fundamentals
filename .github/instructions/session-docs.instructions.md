---
applyTo: docs/sessions/**/*.md
---

# Session Documentation Instructions

These rules apply to every `.md` file under `docs/sessions/`.

**Repository scope:** Python fundamentals session write-ups only.

## Required content coverage

Session docs must include:

1. **Session context** — duration (30 min), type, level, session number
2. **Learning objectives** — measurable outcomes
3. **Prerequisites** — link to prior sessions when applicable
4. **Core teaching content** — progressive: simple → complex
5. **Practice file mapping** — explicit references to `src/L{level}/S{session}/` files
6. **Wrap-up summary** — key takeaways / progress check
7. **Troubleshooting** — common errors (required from S3 onward)

YAML front-matter is optional; pedagogical flow takes priority.

## File naming

- Session format: `S{session}.md` — e.g. `S3.md`
- Level plan: `_Plan.md`
- Location: `docs/sessions/L{level}/`

## Links and references

- Practice files: `src/L{level}/S{session}/{nn}_name.py`
- Verify every linked file **exists** before committing.
- Images: `../../images/S{session}/filename.png` or Mermaid/ASCII fallback when PNGs are unavailable

## Content standards

- **Zero-Copy**: no verbatim third-party text
- **Split, never trim**: do not delete pedagogy to save space
- **Mermaid-first diagrams** with ASCII fallback
- **Session bucketing**: check `docs/meetup/L1/sessions.md` before adding to completed sessions

## Linting

```powershell
./scripts/docs-lint.ps1
```

## Learning order guard (L1)

Variables (S2) → Operators (S3) → Conditionals (S4) → MP1 (S5) → Loops (S6) → Debugging (S7) → Lists (S8) → Dicts (S9) → MP2 (S10)
