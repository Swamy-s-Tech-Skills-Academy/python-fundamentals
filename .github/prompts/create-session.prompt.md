---
mode: agent
description: Create a new session document and matching practice files for the Python Fundamentals curriculum.
---

# Create Session

You are creating educational content for the **Python Fundamentals** curriculum (**Python only**).

## Required inputs (ask if not provided)

- **Level** — `L1`–`L9`
- **Session number** — `S1`–`S10` (mini projects at `S5`, `S10`)
- **Topic** — brief description of the concept to teach

## Authoritative paths

- Session doc → `docs/sessions/L{level}/S{session}.md`
- Practice code → `src/L{level}/S{session}/`
- Structure ref → `docs/RepositoryStructure.md`
- Placement guard → `docs/meetup/L1/sessions.md` (do not add to completed sessions without approval)

## Workflow: THINK → REASON → ACT → VERIFY

### THINK

1. State the learning objective in one sentence.
2. Decompose the topic into 3–5 digestible chunks ordered simple → complex.
3. Anticipate the top two beginner misconceptions.

### REASON

1. List prerequisite sessions — verify they are numbered **before** this one.
2. List sessions this content **enables** — verify they are numbered **after** this one.
3. Sketch two original examples (no copying from books, tutorials, or prior art).

### ACT

1. Write `docs/sessions/L{level}/S{session}.md` with overview, objectives, prerequisites, content, practice files, takeaways, troubleshooting.
2. Write practice files at `src/L{level}/S{session}/{nn}_{name}.py` with `# Filename:` header and working code.

### VERIFY

1. All code runs without errors.
2. All file references resolve to existing files.
3. Session numbering respects learning-dependency order.
4. Zero-Copy: no borrowed sentence structure from external sources.

## Hard rules

- **Never trim content** — split into parts if needed.
- **Numeric prefixes mandatory** — `01_`, `02_`, … on ordered practice files.
- **Path format** — `src/L1/S6/` not `src/S6/`.
- Update `docs/RepositoryStructure.md` if the tree changes.
