# Working area — sandbox and bucketing guide

Informal drafts live here. **Publish-facing session docs must only reference promoted files under `src/L1/{S5_MP1,S6,S7,S8,S9,S10_MP2}/`** (never raw `Working/` paths).

Use `docs/meetup/L1/meetup-sessions.md` plus `docs/sessions/L1/_Plan.md` for delivery order. Repo **folder names** below are what you import and link in Markdown.

## Layout (on disk)

| Path | Role |
| --- | --- |
| `S1/` | Foundational drafts (sessions 1–2); see `S1/README.md` |
| `S5_MP1/` … `S10_MP2/` | Staging folders aligned with formal `src/L1/…` targets; each has a short `README.md` |
| `References.md` | External reference links (not session practice) |

Drop new `.py` drafts in the staging folder that matches your promotion target, then follow the checklist below to move them into `src/L1/…`.

---

## Formal buckets from Mini Project 1 onward

Route **new** ideas from `source-material/` or fresh Working drafts into **one** folder by outcome (rewrite content; zero-copy).

| Formal folder | Session doc | What belongs here |
| --- | --- | --- |
| `src/L1/S5_MP1/` | `docs/sessions/L1/S5_MP1.md` | Mini calculator project: branching, validated input, `import` across local modules, divide-by-zero, style cleanup on real project code |
| `src/L1/S6/` | `docs/sessions/L1/S6.md` | Loops: `for` + `range`, `while`, `break` / `continue` / `pass`, loop-heavy mini programs (e.g. countdown, FizzBuzz, menu loop patterns) |
| `src/L1/S7/` | `docs/sessions/L1/S7.md` | Reading errors, debugging practice, builtins tour, PEP 8–style readability refactors |
| `src/L1/S8/` | `docs/sessions/L1/S8.md` | Lists: basics, methods, slightly larger list-driven exercises |
| `src/L1/S9/` | `docs/sessions/L1/S9.md` | Dictionaries: create, traverse, asserts / light testing mindset |
| `src/L1/S10_MP2/` | `docs/sessions/L1/S10_MP2.md` | Second mini project integrating loops + collections + output formatting |

### Earlier formal homes (do not confuse with rows above)

- `src/L1/S1/` … `S4/` — environment, variables/types, operators, conditionals/modules.

---

### Current `S1/` sample scripts

The existing `01_sample.py`–`05_sample.py` files teach **Session 1–2 level** concepts (printing, core types, PEP 8 tour, chained assignment, conversion edge cases). Each includes a `# Filename: src/Working/S1/…` header aligned with its real path.

### Decision for those scripts

Keep promoting or refining them under **`src/L1/S1/`** or **`src/L1/S2/`** only.

Do **not** drop them unchanged into **`S5_MP1` … `S10_MP2`**; that would teach topics out of order. If you reuse a pattern (e.g. validation) in a calculator **after** learners know conditionals, re-author a **`S5_MP1`** script that fits that session’s checklist instead.

---

## Promotion checklist (Working → formal)

1. Pick the single folder row from the table above (or `S1`–`S4` for foundational content).
2. Name the next file `NN_clear_topic.py` in that folder.
3. Add the standard header (`# Filename:` + session marker) and runnable `main`/help where the rest of L1 expects it.
4. Link it from the matching **`docs/sessions/L1/*.md`** practice section.
5. Run `ruff check src`, `python -m compileall -q src`.

Intake transcripts stay in `source-material/`; extract **ideas**, not wording.
