---
learning_level: "Noob → Nerd"
prerequisites:
  - "docs/sessions/L1/S1.md"
  - "docs/sessions/L1/S2.md"
  - "docs/sessions/L1/S3.md"
  - "docs/sessions/L1/S4.md"
estimated_time: "30 minutes"
session_type: "Project"
learning_objectives:
  - "Build a working CLI calculator that performs basic arithmetic operations"
  - "Validate and convert user input before calculation to avoid type-related failures"
  - "Use if/elif/else branching to select operations and handle divide-by-zero safely"
  - "Apply PEP 8 naming, spacing, and comment rules to write clean, readable code"
related_topics:
  prerequisites:
    - "docs/sessions/L1/S1.md"
    - "docs/sessions/L1/S2.md"
    - "docs/sessions/L1/S3.md"
    - "docs/sessions/L1/S4.md"
  builds_upon: []
  enables:
    - "docs/sessions/L1/S6.md"
  cross_refs: []
---

# Mini Project 1: Simple Calculator

**Duration:** 30 minutes  
**Type:** 🛠️ Project  
**Level:** Noob → Nerd  
**Session:** MP1

---

## 🎯 Project mission

Build a calculator that does more than print fixed lines: it asks for input, validates it, chooses the correct operation, and handles edge cases safely.

This project is the first "full-flow" integration point for Sessions 1–4:

- **Session 1** gives input/output and script flow
- **Session 2** gives data types and conversion
- **Session 3** gives arithmetic operators
- **Session 4** gives branching with `if/elif/else`

---

## ✅ Outcomes

By the end of this mini project, you should be able to:

- Build a CLI calculator that supports `+`, `-`, `*`, `/`
- Validate number input before conversion
- Use branching to route operations
- Guard against divide-by-zero
- Apply PEP 8 rules to write clean, readable code
- Explain why validation and branching make the program safer

---

## 📋 Prerequisites / builds-on

Complete these first:

- [S1.md](S1.md)
- [S2.md](S2.md)
- [S3.md](S3.md)
- [S4.md](S4.md)

This project then builds toward:

- [S6.md](S6.md) for loop fluency and control flow extension

---

## 🧪 Practice file mapping

**Project practice folder:** `src/L1/S5_MP1/`

| File | Purpose |
| --- | --- |
| `src/L1/S5_MP1/calculator_utils.py` | Shared helper: `is_valid_number_text()` validates numeric input (imported by the calculator) |
| `src/L1/S5_MP1/01_simple_calculator.py` | One-run calculator with operation choice, numeric validation, and divide-by-zero handling |

---

## 🛠️ Build path

### Step 1: Core one-run calculator

Start with `01_simple_calculator.py`:

1. Ask for operation (`+`, `-`, `*`, `/`)
2. Ask for two numbers
3. Validate that both inputs are numeric text — uses `is_valid_number_text()` from `calculator_utils.py`
4. Convert to `float`
5. Use `if/elif/else` to choose operation
6. Handle divide-by-zero explicitly

> **About the import:** `calculator_utils.py` is a small helper file in the same folder.
> `from calculator_utils import is_valid_number_text` loads that one function into your script.
> This is the same `import` pattern from Session 4 — now applied to your own file instead of a built-in module.

### Step 2: PEP 8 style review

PEP 8 is Python's official style guide, written by Guido van Rossum (Python's creator).
It covers naming, spacing, and commenting rules that make code readable — for yourself and for anyone who reads your code later.

Your calculator already works. Now open `01_simple_calculator.py` and check it against each rule below.

#### Rule 1 — Meaningful variable names

Names should describe what they hold. Use lowercase with underscores for multi-word names.

| ✅ Clear | ❌ Vague |
| --- | --- |
| `operation` | `op` |
| `first_raw` | `a` |
| `second_raw` | `b` |
| `first_is_number` | `check` |

#### Rule 2 — Spaces around operators

One space on each side of `=`, `+`, `-`, `*`, `/`, `==`, `not`.

```python
# ✅ Good
result = first + second
first_is_number = is_valid_number_text(first_raw)

# ❌ Poor
result=first+second
first_is_number=is_valid_number_text(first_raw)
```

#### Rule 3 — No spaces inside parentheses or brackets

No space immediately after `(` or before `)`.

```python
# ✅ Good
float(first_raw)
input("Enter first number: ")

# ❌ Poor
float( first_raw )
input( "Enter first number: " )
```

#### Rule 4 — Space after commas

One space after every comma in function calls and collections.

```python
# ✅ Good
{"+", "-", "*", "/"}

# ❌ Poor
{"+","-","*","/"}
```

#### Rule 5 — Comments explain *why*, not *what*

The code already shows *what* it does. Use `#` comments to explain *why* a decision was made.

```python
# ❌ What (the code already shows this)
# checks if second equals zero

# ✅ Why (useful — explains the reasoning)
# Why: dividing by zero is undefined — guard before attempting division
```

Your `01_simple_calculator.py` already has `# Why:` comments.
Check that at least one comment per major decision explains the *reason*, not just the action.

---

## 📚 Appendix concepts from Session 2

These materials extend Session 2 knowledge:

### `del` and `NameError` (extra)

You can remove a variable with `del`. After deletion, any reference to it raises a `NameError` — the same error you get when you use a name before assigning it.

```python
season = "October"
print(season)   # → October

del season
print(season)   # → NameError: name 'season' is not defined
```

**Practical tip:** If you `del` a variable and later re-run a cell or script that assigns it again, the deletion runs again too. Comment out the `del` line once you no longer need the cleanup.

### `bool` in arithmetic (extra)

`True` and `False` are Python objects that behave as `1` and `0` in numeric operations.
This rarely comes up in beginner code, but it demystifies why `bool` is a subtype of `int`:

```python
print(True * 7)   # → 7   (True treated as 1)
print(False * 7)  # → 0   (False treated as 0)
print(type(True)) # → <class 'bool'>
```

**Why it matters:** Conditional expressions in loops and filters silently rely on this — good to know it exists even if you don't use it directly yet.

---

## 🔍 Project acceptance checklist

Use this to verify your implementation:

- [ ] Program supports `+`, `-`, `*`, `/`
- [ ] Invalid operation input is handled clearly
- [ ] Non-numeric input is rejected before conversion
- [ ] Division by zero does not crash the program
- [ ] Output is readable and beginner-friendly
- [ ] Variable names are meaningful (`operation`, `first_raw` — not `op`, `a`, `b`)
- [ ] Spaces around all operators (`result = first + second` — not `result=first+second`)
- [ ] No spaces inside parentheses (`float(first_raw)` — not `float( first_raw )`)
- [ ] At least one `# Why:` comment per major decision

---

## 🔧 Troubleshooting

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| `ValueError` on conversion | Input text was not numeric | Validate first, then convert |
| Wrong branch runs | Condition order/logic issue | Re-check `if/elif` flow |
| Crash on division | Denominator is `0` | Add explicit divide-by-zero guard |
| `ModuleNotFoundError` on import | Running from wrong directory | Run with `python src/L1/S5_MP1/01_simple_calculator.py` from repo root |

---

## 🧠 Why this project matters

This project is your first full program with clear input → validation → decision → output flow.  
It sets up the same pattern you will reuse in every bigger project.

---

## 📌 Wrap-up

After this project, you can say:

- "I can build a calculator that handles normal and edge cases."
- "I know why input validation matters before doing arithmetic."
- "I can combine operators and conditionals in one complete script."
- "I can apply PEP 8 rules to make my code clean and readable."

Next: take loop skills further in [S6.md](S6.md), then apply the same validated-input pattern in Mini Project 2.
