# 🐍 Python Software Engineering Journey — Master Plan

## From Clueless to Curious: An 18-Level Transformation

> **Program framing:** This journey is marketed as the **Python Software Engineering Journey** — a path from absolute beginner to curious professional. The repository name (`python-fundamentals`) reflects where we started; the master plan describes the full arc.
>
> **Philosophy:** Each level builds confidence, curiosity, and practical skills through 30-minute focused sessions with hands-on practice and real-world applications.

**Note:** This master plan evolves as we progress — reflecting student feedback, delivery experience, and industry trends. **When curriculum reality and this document diverge, update this file first**, then level plans (`docs/sessions/L{level}/_Plan.md`), then session docs and meetup status.

---

## 🗺️ **Program Positioning — Three Stages**

This is not a single homogeneous “syntax course.” It is an **ecosystem** with a shifting audience and deepening expectations:

| Stage | Levels | Audience shift | Primary outcome |
| --- | --- | --- | --- |
| **Part 1 — Python Fundamentals** | 1–6 | Absolute beginner → confident programmer | Write structured programs; persist and query data |
| **Part 2 — Professional Python Development** | 7–12 | Programmer → practitioner | Clean code, tooling, patterns, stdlib, packaging |
| **Part 3 — Python Systems Engineering** | 13–18 | Practitioner → systems-minded engineer | Production data, messaging, services, observability, capstone |

**Repository home:** [`docs/RepositoryStructure.md`](RepositoryStructure.md) · **Level plans:** `docs/sessions/L{level}/_Plan.md` · **Sessions:** `docs/sessions/L{level}/S{n}.md` · **Meetup delivery:** `docs/meetup/L{level}/sessions.md`

---

## 📐 **Source-of-Truth Hierarchy**

```text
Master Plan (this file)     — roadmap, stages, status axes, spiral labels, time bands
        ↓
Level Plan (_Plan.md)       — level outcomes, session list, links to S{n}.md
        ↓
Session doc (S{n}.md)       — teachable 30-minute lesson + practice file mapping
        ↓
Practice code (src/L{n}/)   — runnable scripts referenced by session docs
        ↓
Meetup status (sessions.md) — delivery schedule (completed / planned / pending)
```

Authoring rule: **never invent paths** — align with [`RepositoryStructure.md`](RepositoryStructure.md).

---

## 📋 **Course Architecture Overview**

**Guided instruction format:** 18 levels × 10 sessions × **30 minutes** ≈ **90 hours of live, guided instruction** (core session time).

**Realistic learner effort (indicative):**

| Band | Hours (approx.) | What it includes |
| --- | --- | --- |
| **Core guided instruction** | ~90 | 18 × 10 × 30 min sessions |
| **Mini projects** | ~35–45 | 36 MPs at 30–45 min each |
| **Practice & optional reinforcement** | ~40–60 | Extra drills (e.g. L1 S8 strings/lists) |
| **Guided labs (esp. L13–18)** | ~40–70 | Docker, DB setup, messaging, integration |
| **Stretch & portfolio** | Optional | Capstone polish, portfolio case studies |

**Advertise:** *“90+ hours of guided instruction”* — not *“90-hour total course.”* Total mastery time often exceeds **200 hours** for learners who complete labs and stretch work.

**Outcome:** Transformation from absolute beginner to curious professional who can design, build, test, and ship small Python systems.

**Approach:** Progressive complexity with practical application at every step; **spiral revisits** (see below) instead of accidental repetition.

---

## 🔄 **Spiral Learning Labels**

Topics that reappear across levels are **intentional spirals**. Label each pass:

| Label | Meaning | Example |
| --- | --- | --- |
| **Introduction** | First exposure; minimal API | L7: HTTP/JSON with `requests` |
| **Reinforcement** | Apply in a richer project | L8: CLI wrapper + error handling |
| **Professional usage** | Tooling, tests, repo workflow | L11: `requests` + Excel/report CLI |
| **Production usage** | Real infra, observability, CI | L16–18: services, Docker, capstone |

**Spiral topics in this plan:** `requests`/HTTP · pytest/unittest · Git · CLI (argparse/click) · formatting/linting (black, ruff, flake8) · file I/O → CSV/JSON → DB → APIs · testing depth (unit → integration).

---

## 🧱 **Capability Layers (parallel mental model)**

Levels also map to cumulative **capabilities** (orthogonal to level numbers):

```text
Language (L1–2) → Programming (L3–4) → Design (L4, L9) → Data (L5–7, L13–14)
    → Integration (L7, L15–16) → Systems (L16–17) → Production (L17–18)
```

Use this map when explaining *why* abstraction oscillates (e.g. patterns before stdlib depth) — each level still has a primary job-to-be-done.

---

## 📊 **Status Model — Three Independent Axes**

Do not mix “complete,” “ready,” and “delivered.” Track separately:

| Axis | Values | Meaning |
| --- | --- | --- |
| **Curriculum** | Draft · Ready · Validated · Frozen | Session docs + practice files quality |
| **Delivery** | Not started · Teaching · Completed | Meetup / live cohort progress |
| **Repository** | Scaffolded · Implemented · Reviewed | Files exist, CI passes, links resolve |

### **Level Status Map**

| Level | Stage (From → To) | Stage part | Curriculum | Delivery (meetup) | Repository |
| --- | --- | --- | --- | --- | --- |
| 1 | Noob → Nerd | Part 1 | Validated | S1–S4 completed; S5–S10 pending | Implemented |
| 2 | Nerd → Novice | Part 1 | Validated | All pending | Implemented |
| 3 | Novice → Object Thinker | Part 1 | Draft | Not started | Scaffolded |
| 4 | Object Thinker → Design Learner | Part 1 | Draft | Not started | Scaffolded |
| 5 | Design Learner → Data Wrangler | Part 1 | Draft | Not started | Scaffolded |
| 6 | Data Wrangler → DB Beginner | Part 1 | Draft | Not started | Scaffolded |
| 7 | DB Beginner → Integration Novice | Part 2 | Draft | Not started | Scaffolded |
| 8 | Integration Novice → Practitioner | Part 2 | Draft | Not started | Scaffolded |
| 9 | Practitioner → Patterned Coder | Part 2 | Draft | Not started | Scaffolded |
| 10 | Patterned Coder → Stdlib Specialist | Part 2 | Draft | Not started | Scaffolded |
| 11 | Stdlib Specialist → Pro Toolsmith | Part 2 | Draft | Not started | Scaffolded |
| 12 | Pro Toolsmith → Curious Learner | Part 2 | Draft | Not started | Scaffolded |
| 13 | Curious Learner → Data Platform Explorer | Part 3 | Draft | Not started | Scaffolded |
| 14 | Data Platform Explorer → Data Systems Builder | Part 3 | Draft | Not started | Scaffolded |
| 15 | Data Systems Builder → Service Integrator | Part 3 | Draft | Not started | Scaffolded |
| 16 | Service Integrator → Service Builder | Part 3 | Draft | Not started | Scaffolded |
| 17 | Service Builder → Systems Crafter | Part 3 | Draft | Not started | Scaffolded |
| 18 | Systems Crafter → Curious Professional | Part 3 | Draft | Not started | Scaffolded |

**Level plan links:** [L1](sessions/L1/_Plan.md) · [L2](sessions/L2/_Plan.md) · [L3](sessions/L3/_Plan.md) · L4–L18 `_Plan.md` scaffolds under `docs/sessions/`

---

## 📚 **Pedagogy Templates (all levels)**

### **Session rhythm**

```text
Learn → Practice → Mini Project → Learn → Practice → Mini Project
```

Mini projects occupy **session slots 5 (MP1)** and **10 (MP2)** in every level — matching `S5.md` / `S10.md` in the repository.

### **Exit criteria**

Use measurable **“Can you…?”** checks (kept per level below).

### **Anti-patterns (expand over time)**

Each anti-pattern can grow into a micro-lesson with:

1. **Recognition signals** — how you notice it in code review  
2. **Why it happens** — beginner pressure, copy-paste, time stress  
3. **How to fix it** — one concrete refactor step  
4. **Professional example** — what good looks like at industry level  

### **Reflection questions (end of each level)**

- What surprised me?  
- What was hardest?  
- What would I redesign in my mini project?  
- What could I explain to a peer in five minutes?  

### **Architecture Decision Records (from Level 8 onward)**

Optional **one ADR per mini project** (keep short — not a second homework course):

```text
ADR-001: Why SQLite? / Why classes? / Why JSON cache?
```

Template: **Context → Decision → Consequences**. Stored in project `docs/adr/` or session appendix.

---

## 🎯 **The 18-Level Transformation Journey**

### **🌱 Level 1: Noob → Nerd** *(Foundation Building — Part 1)*

**Focus:** Environment setup, basic syntax, curiosity ignition  
**Duration:** ~5 hours core sessions + optional reinforcement  
**Curriculum:** Validated · **Delivery:** S1–S4 completed; S5–S10 pending · **Repository:** Implemented  
**Level plan:** [docs/sessions/L1/_Plan.md](sessions/L1/_Plan.md)

**Actual Session Breakdown:**

| Phase | Session | Topic                                                      | Type         | Curriculum     |
| ----- | ------- | ---------------------------------------------------------- | ------------ | -------------- |
| A     | 1       | **Python Introduction & Environment Setup**                 | 📚 Knowledge | Validated      |
| A     | 2       | **Variables & Data Types**                                 | 📚 Knowledge | Validated      |
| A     | 3       | **Operators & Expressions**                                | 📚 Knowledge | Validated      |
| A     | 4       | **Conditionals, Indentation & Introduction to Modules**    | 📚 Knowledge | Validated      |
| A     | 5 (MP1) | **🚀 Mini Project 1: Simple Calculator**                   | 🛠️ Project   | Validated      |
| B     | 6       | **Loops & Iteration**                                      | 📚 Knowledge | Validated      |
| B     | 7       | **Basic Debugging & Built-in Functions**                   | 📚 Knowledge | Validated      |
| B     | 8       | **Lists, Iteration & String Sequences**                    | 📚 Knowledge | Validated      |
| B     | 9       | **Dictionaries & Basic Testing**                           | 📚 Knowledge | Validated      |
| B     | 10 (MP2) | **🚀 Mini Project 2: Personal Profile Generator**          | 🛠️ Project   | Validated      |

**Key Learning Focus:**

**Phase A (Sessions 1–4 + Session 5 MP1):**

- Python installation & VS Code setup with PVM execution understanding
- Variables, data types (`int`, `float`, `str`, `bool`), and dynamic typing
- Arithmetic, comparison, and assignment operators with precedence
- **Python indentation rules** and conditional statements (`if/elif/else`)
- Introduction to modules and the `random` module
- **PEP 8 introduced** in MP1 (naming, spacing, comments) — *spiral: reinforced in S7*
- **Mini Project 1: Simple Calculator** — applying Sessions 1–4 concepts

**Phase B (Sessions 6–9 + Session 10 MP2):**

- Loops (`for`, `while`) with `range()`, `break`, `continue` controls
- Optional: **boolean precedence & truthy/falsy** (`S6` optional `08`–`09`)
- **PEP 8 reinforcement** in S7 (warm-up, not a second full style lesson)
- **Error reading skills** and built-in functions (`len()`, `max()`, `min()`, `sum()`, `abs()`, `round()`)
- **Lists** with iteration, nested access, slice replacement; **optional string-sequence drills** (`S8` files `04`–`16`: methods, formatting including `%`, `.format()`, f-strings; list-method drills `13`–`15`)
- Dictionaries with **basic testing using `assert`**
- **Mini Project 2: Personal Profile Generator** — applying Sessions 6–9 concepts

**Mini Projects:**

- **Simple Calculator** (`src/L1/S5/`) — CLI calculator with validation and divide-by-zero handling
- **Personal Profile Generator** (`src/L1/S10/`) — profile system using dictionaries/lists; **refactor target for L3 MP1**

**Learning Outcome:** "I can write basic Python programs with proper structure, understand error messages, and I'm genuinely curious to learn more!"

**Exit Criteria:**

Before moving to Level 2, you should be able to:

- ✅ Write a Python script that uses variables, conditionals, and loops without syntax errors
- ✅ Read and understand basic error messages (NameError, TypeError, IndentationError)
- ✅ Use lists and dictionaries to store and retrieve data
- ✅ Use `assert` for simple manual checks
- ✅ Explain why Python uses indentation instead of braces

**Common Anti-Patterns to Avoid:**

- ❌ **Copy-Paste Without Understanding** — typing code without knowing what each line does  
  *Signal:* you cannot change one line without fear. *Fix:* explain each line aloud before running.
- ❌ **Ignoring Error Messages** — not reading the full traceback  
  *Signal:* random edits until something runs. *Fix:* read bottom-up; locate file and line first.
- ❌ **Magic Numbers Everywhere** — `42` or `"admin"` inline instead of named variables  
  *Signal:* repeated literals with unclear meaning. *Fix:* extract to `UPPER_SNAKE` or local names.
- ❌ **No Comments** — code only you understand (briefly)  
  *Signal:* `# Why:` missing on non-obvious decisions. *Fix:* one `# Why:` per branch or validation.

**Reflection (Level 1):**

- What surprised you about Python's indentation or `input()` always returning strings?
- What debugging habit will you keep after Session 7?
- Which optional S8 drill helped most — lists or strings?

---

### **🔧 Level 2: Nerd → Novice** *(Skill Development — Part 1)*

**Focus:** Functions, error handling, file operations, modular programming  
**Duration:** ~5–6 hours core sessions + MPs  
**Curriculum:** Validated · **Delivery:** All pending · **Repository:** Implemented  
**Level plan:** [docs/sessions/L2/_Plan.md](sessions/L2/_Plan.md)

**Actual Session Breakdown:**

| Phase | Session | Topic                                                      | Type         | Curriculum     |
| ----- | ------- | ---------------------------------------------------------- | ------------ | -------------- |
| A     | 1       | **Advanced Data Structures: Sets & Tuples**                 | 📚 Knowledge | Validated      |
| A     | 2       | **List Comprehensions**                                    | 📚 Knowledge | Validated      |
| A     | 3       | **Functions: Definition & Basics**                         | 📚 Knowledge | Validated      |
| A     | 4       | **Error Handling: try/except Basics**                      | 📚 Knowledge | Validated      |
| A     | 5 (MP1) | **🚀 Mini Project 1: Data Processor**                      | 🛠️ Project   | Validated      |
| B     | 6       | **Functions: Parameters & Return Values**                  | 📚 Knowledge | Validated      |
| B     | 7       | **Functions: Scope & Code Organization**                   | 📚 Knowledge | Validated      |
| B     | 8       | **File Handling: Reading & Writing Text Files**            | 📚 Knowledge | Validated      |
| B     | 9       | **Modules Deep Dive & Code Organization**                  | 📚 Knowledge | Validated      |
| B     | 10 (MP2) | **🚀 Mini Project 2: Contact Manager**                    | 🛠️ Project   | Validated      |

**Key Learning Focus:**

**Phase A (Sessions 1-4 + MP1):**

- Advanced data structures: Sets (unique collections) and Tuples (immutable sequences)
- List comprehensions: Elegant way to create and transform lists
- **Functions basics**: Defining functions, calling functions, code reusability
- **Error handling**: try/except blocks, handling common errors gracefully
- **Mini Project 1: Data Processor** - Applying Sessions 1-4 concepts

**Phase B (Sessions 6-9 + MP2):**

- **Functions advanced**: Parameters (positional, keyword, default), return values, multiple returns
- **Functions scope**: Local vs global scope, variable visibility, best practices
- **File handling**: Reading from and writing to text files, file modes, context managers
- **Modules deep dive**: Creating modules, `__name__` and `__main__`, organizing code into modules
- **Mini Project 2: Contact Manager** - Applying Sessions 6-9 concepts

**Mini Projects:**

- **Data Processor** - Process collections using sets, tuples, and list comprehensions with error handling
- **Contact Manager** - Build a practical contact management application that reads/writes files using well-organized modular code

**Learning Outcome:** "I can write reusable functions, handle errors gracefully, and work with files to solve real problems!"

**Exit Criteria:**

Before moving to Level 3, you should be able to:

- ✅ Refactor a 50-line script into 3–5 well-named functions
- ✅ Use `try/except` to handle at least two different error types gracefully
- ✅ Read data from a file, process it, and write results to another file
- ✅ Explain the difference between a function definition and a function call

**Common Anti-Patterns to Avoid:**

- ❌ **God Function** – One function that does everything (200+ lines)
- ❌ **Silent Failures** – Using `except: pass` without logging or handling the error
- ❌ **Global Variables Everywhere** – Modifying global state from inside functions
- ❌ **No Error Handling** – Assuming files always exist and operations always succeed

**Reflection (Level 2):**

- Which function refactor made the biggest clarity gain?
- Where did `try/except` save you from a crash?
- What would you change before refactoring Contact Manager into classes (L3)?

**Bridge to Level 3:** `Contact Manager` (L2 MP2) and `Profile Generator` (L1 MP2) are intentional **refactor targets** for object-based redesign in Level 3.

---

### **🔢 Level 3: Novice → Object Thinker** *(Core OOP Fundamentals — Part 1)*

**Focus:** Solidify **core OOP thinking** — moving from scripts to well‑modeled objects.  
**Duration:** ~5 hours core sessions + MPs  
**Curriculum:** Draft (next to build) · **Delivery:** Not started · **Repository:** Scaffolded (`docs/sessions/L3/_Plan.md`)  
**Prerequisites bridge:** Refactor **L1 Profile Generator** and **L2 Contact Manager** from dict/file scripts into collaborating classes.

**Actual Session Breakdown:**

| Phase | Session | Topic                                                      | Type         | Status         |
| ----- | ------- | ---------------------------------------------------------- | ------------ | -------------- |
| A     | 1       | **Why OOP? From Scripts to Objects**                       | 📚 Knowledge | 🔄 **Planned** |
| A     | 2       | **Defining Classes & Creating Objects**                    | 📚 Knowledge | 🔄 **Planned** |
| A     | 3       | **`__init__`, Attributes & Basic Encapsulation**          | 📚 Knowledge | 🔄 **Planned** |
| A     | 4       | **Instance Methods & Working with Object State**          | 📚 Knowledge | 🔄 **Planned** |
| A     | 5 (MP1) | **🚀 Mini Project 1: Object‑Based Profile Manager**        | 🛠️ Project   | 🔄 **Planned** |
| B     | 6       | **Composing Multiple Objects (Has‑a Relationships)**      | 📚 Knowledge | 🔄 **Planned** |
| B     | 7       | **Collections of Objects (Lists of Objects)**             | 📚 Knowledge | 🔄 **Planned** |
| B     | 8       | **User‑Friendly Objects with `__str__` / `__repr__`**     | 📚 Knowledge | 🔄 **Planned** |
| B     | 9       | **Refactoring Scripts into Classes (OOP in Practice)**    | 📚 Knowledge | 🔄 **Planned** |
| B     | 10 (MP2) | **🚀 Mini Project 2: Object‑Oriented Task / Inventory App**| 🛠️ Project   | 🔄 **Planned** |

**Key Learning Focus:**

**Phase A (Sessions 1-4 + MP1):**

- Build an **intuitive mental model of objects**: when and why to use classes vs plain scripts  
- Learn to define simple classes and construct objects with `__init__`  
- Store and update object state via instance attributes safely  
- Call instance methods correctly and avoid “global data everywhere”  
- **Mini Project 1: Object‑Based Profile Manager** – represent a user profile (or contact) using 1–2 small classes instead of dictionaries

**Phase B (Sessions 6-9 + MP2):**

- Model **relationships between objects** using composition (“has‑a”)  
- Work with **collections of objects** (lists of class instances) and iterate over them  
- Make objects easier to debug and display with `__str__` / `__repr__` (intro level)  
- Practice refactoring an existing script into a class‑based design  
- **Mini Project 2: Object‑Oriented Task / Inventory App** – manage tasks, todos, or items using multiple interacting objects and collections

**Mini Projects:**

- **Object‑Based Profile / Contact Manager** – basic CRUD on user profiles using classes and lists of objects  
- **Task / Todo or Inventory Manager** – simple console app using objects to represent tasks/items and operations on them

**Learning Outcome:** "I can design and use simple classes and objects with confidence, refactor small scripts into object‑oriented code, and recognize when OOP structure makes my programs easier to understand and extend."

**Exit Criteria:**

Before moving to Level 4, you should be able to:

- ✅ **Can you** refactor a dictionary-based script (e.g., contact manager) into 2–3 collaborating classes?
- ✅ **Can you** explain why a specific attribute belongs on one class and not another?
- ✅ **Can you** create objects, call their methods, and access their attributes without errors?
- ✅ **Can you** use `__str__` to make objects print in a human-readable format?

**Common Anti-Patterns to Avoid:**

- ❌ **God Object** – One class that does everything (violates Single Responsibility)
- ❌ **Anemic Model** – Classes that are just data containers with no behavior (all getters/setters, no logic)
- ❌ **Premature Inheritance** – Using inheritance when composition would be simpler
- ❌ **Classes for Everything** – Creating classes for simple functions that don't need state

**Reflection (Level 3):**

- When did a class feel clearer than a dictionary for the same data?
- What attribute placement decision was hardest?
- How would you explain `__init__` to a peer using your MP1 project?

---

### **🏗️ Level 4: Object Thinker → Design Learner** *(OOP Design & Clean Code Intro)*

**Focus:** Turn basic OOP skills into **good small designs** and introduce clean‑code thinking.  
**Duration:** 5 hours (10 sessions × 30 min)  
**Status:** 🔄 **Planned**

**Actual Session Breakdown:**

| Phase | Session | Topic                                                         | Type         | Status         |
| ----- | ------- | ------------------------------------------------------------- | ------------ | -------------- |
| A     | 1       | **From Requirements to Classes (Thinking in Models)**        | 📚 Knowledge | 🔄 **Planned** |
| A     | 2       | **Designing Responsibilities & Avoiding “God Classes”**      | 📚 Knowledge | 🔄 **Planned** |
| A     | 3       | **Improving Class Interfaces (KISS for Methods & Classes)**  | 📚 Knowledge | 🔄 **Planned** |
| A     | 4       | **Intro to Refactoring: Making Existing Code Cleaner**       | 📚 Knowledge | 🔄 **Planned** |
| A     | 5 (MP1) | **🚀 Mini Project 1: Refactor a Script into a Class Design**  | 🛠️ Project   | 🔄 **Planned** |
| B     | 6       | **Clean Code Principles: KISS, DRY, YAGNI (Applied)**        | 📚 Knowledge | 🔄 **Planned** |
| B     | 7       | **Reading & Reviewing Code: Finding Smells in OOP Code**     | 📚 Knowledge | 🔄 **Planned** |
| B     | 8       | **Intro Unit Tests for Classes (Arrange–Act–Assert)**        | 📚 Knowledge | 🔄 **Planned** |
| B     | 9       | **Organizing a Small OOP Project (Modules & Packages)**      | 📚 Knowledge | 🔄 **Planned** |
| B     | 10 (MP2) | **🚀 Mini Project 2: Clean, Tested OOP Console Application**  | 🛠️ Project   | 🔄 **Planned** |

**Key Learning Focus:**

**Phase A (Sessions 1–4 + MP1):**

- Take simple problem statements and **turn them into small class models**  
- Assign responsibilities to classes so each one “does one thing well”  
- Keep class and method interfaces simple and readable (KISS at class level)  
- Practice basic refactorings (extract method, rename, split classes) on existing Level 2–3 style code  
- **Mini Project 1: Refactor a Script into a Class Design** – choose a previous Level 2/3 script (e.g. data processor or profile manager) and redesign it as a cleaner set of classes

**Phase B (Sessions 6–9 + MP2):**

- Apply **KISS, DRY, YAGNI** to real OOP code, not just theory  
- Learn to **read and review code**: spot duplication, long methods, and unclear names  
- Write **very first unit tests for classes** (no heavy framework, just core patterns and maybe unittest/pytest basics)  
- Organize a tiny project into modules/packages (`models.py`, `services.py`, etc.) to prepare for larger apps in later levels  
- **Mini Project 2: Clean, Tested OOP Console Application** – a small console app (e.g. Todo/Booking/Tracker) with clear class design, basic tests, and a simple project structure

**Mini Projects:**

- **Refactored Data / Profile Manager** – turning a previous data‑heavy script into a clearer set of classes with better naming and structure  
- **Clean OOP Console App** – small but well‑organized application (e.g. task manager, booking tracker) with tests and a simple multi‑module layout

**Learning Outcome:** "I can take a small problem, design sensible classes for it, refactor messy code into a cleaner object‑oriented structure, and apply basic clean‑code principles and tests to keep my designs maintainable."

**Exit Criteria:**

Before moving to Level 5, you should be able to:

- ✅ **Can you** identify at least one "code smell" in a small script and refactor it?
- ✅ **Can you** write a simple unit test using `assert` or `unittest` that verifies a class method works correctly?
- ✅ **Can you** explain why a class has too many responsibilities (God Object) and how to split it?
- ✅ **Can you** apply KISS, DRY, or YAGNI to a real code example?

**Common Anti-Patterns to Avoid:**

- ❌ **Over-Engineering** – Adding patterns and abstractions before you feel the pain
- ❌ **Copy-Paste Refactoring** – Duplicating code instead of extracting shared logic (violates DRY)
- ❌ **Premature Abstraction** – Creating base classes or interfaces "just in case" (violates YAGNI)
- ❌ **If-Else Hell** – Long chains of conditionals that should be replaced with polymorphism or strategy

**Reflection (Level 4):**

- What surprised me at this level?
- What was hardest — and what habit will I keep?
- What would I redesign in my mini project?
- What could I explain to a peer in five minutes?

---

### **📂 Level 5: Design Learner → Data Wrangler** *(Files & Data Formats)*

**Focus:** Become fluent with **real‑world files and data formats** (text, CSV, JSON, simple serialization).  
**Duration:** 5 hours (10 sessions × 30 min)  
**Status:** 🔄 **Planned**

**Actual Session Breakdown:**

| Phase | Session | Topic                                                          | Type         | Status         |
| ----- | ------- | -------------------------------------------------------------- | ------------ | -------------- |
| A     | 1       | **Reviewing File I/O: Text vs Binary, Paths, Encodings**      | 📚 Knowledge | 🔄 **Planned** |
| A     | 2       | **CSV Basics: Reading & Writing Tabular Data**                | 📚 Knowledge | 🔄 **Planned** |
| A     | 3       | **JSON Basics: Nested Structures & Config‑Style Data**        | 📚 Knowledge | 🔄 **Planned** |
| A     | 4       | **From Raw Text to Structured Data (Parsing & Cleaning)**     | 📚 Knowledge | 🔄 **Planned** |
| A     | 5 (MP1) | **🚀 Mini Project 1: CSV/JSON Data Cleaner & Reporter**        | 🛠️ Project   | 🔄 **Planned** |
| B     | 6       | **Building Simple Data Pipelines (Read → Transform → Write)** | 📚 Knowledge | 🔄 **Planned** |
| B     | 7       | **Basic Serialization & Settings Files (Configs & States)**   | 📚 Knowledge | 🔄 **Planned** |
| B     | 8       | **Robust File Handling: Errors, Missing Data & Validation**   | 📚 Knowledge | 🔄 **Planned** |
| B     | 9       | **End‑to‑End File‑Based Mini App (Putting It All Together)**  | 📚 Knowledge | 🔄 **Planned** |
| B     | 10 (MP2) | **🚀 Mini Project 2: File‑Based Data Dashboard / Reporter**    | 🛠️ Project   | 🔄 **Planned** |

**Key Learning Focus:**

**Phase A (Sessions 1–4 + MP1):**

- Deepen understanding of **file I/O** from Level 2: text vs binary, encodings, safe path handling  
- Work confidently with **CSV files**: headers, rows, reading, writing, and simple transformations  
- Work confidently with **JSON files**: nested structures, lists vs dicts, mapping JSON ↔ Python data structures  
- Practice turning **raw or messy text** into structured CSV/JSON data with minimal parsing and cleaning logic  
- **Mini Project 1: CSV/JSON Data Cleaner & Reporter** – read a CSV or JSON file, clean/transform the data, and write out a simple summary or cleaned file

**Phase B (Sessions 6–9 + MP2):**

- Build **simple data pipelines** that read from one format, transform in Python, and write to another file  
- Introduce **basic serialization and configuration** patterns (e.g. JSON settings, simple config files)  
- Handle common file/data issues: missing files, bad rows, invalid values, and fallback defaults  
- Design a small, end‑to‑end **file‑based mini application** that students can run and customize  
- **Mini Project 2: File‑Based Data Dashboard / Reporter** – e.g. a gradebook/expense/report tool that reads CSV/JSON, computes summaries, and writes human‑readable reports

**Mini Projects:**

- **CSV/JSON Data Cleaner & Reporter** – clean and summarize a small dataset stored in CSV/JSON  
- **File‑Based Data Dashboard / Reporter** – build a console‑based dashboard that reads data files, computes key metrics, and writes reports

**Learning Outcome:** "I can confidently read, clean, transform, and write common text/CSV/JSON data from Python, and build small file‑based tools that solve real data‑wrangling problems."

**Exit Criteria:**

Before moving to Level 6, you should be able to:

- ✅ **Can you** read a CSV file, filter rows based on criteria, and write the results to a new file?
- ✅ **Can you** parse a JSON file with nested structures and extract specific data fields?
- ✅ **Can you** handle missing or malformed data gracefully (without crashing)?
- ✅ **Can you** explain when to use CSV vs JSON for storing data?

**Reflection (Level 5):**

- What surprised me at this level?
- What was hardest — and what habit will I keep?
- What would I redesign in my mini project?
- What could I explain to a peer in five minutes?

---

### **🗃️ Level 6: Data Wrangler → DB Beginner** *(Relational Databases with SQLite)*

**Focus:** Build a strong **relational database (SQL + SQLite)** foundation and connect it to Python programs.  
**Duration:** 5 hours (10 sessions × 30 min)  
**Status:** 🔄 **Planned**

**Actual Session Breakdown:**

| Phase | Session | Topic                                                          | Type         | Status         |
| ----- | ------- | -------------------------------------------------------------- | ------------ | -------------- |
| A     | 1       | **Why Databases? From Files to Tables**                       | 📚 Knowledge | 🔄 **Planned** |
| A     | 2       | **Tables, Rows & Keys: Designing a Simple Schema**           | 📚 Knowledge | 🔄 **Planned** |
| A     | 3       | **SQL Basics: SELECT, INSERT, UPDATE, DELETE**               | 📚 Knowledge | 🔄 **Planned** |
| A     | 4       | **Filtering & Ordering Data (WHERE, ORDER BY, LIMIT)**       | 📚 Knowledge | 🔄 **Planned** |
| A     | 5 (MP1) | **🚀 Mini Project 1: CLI over a Single‑Table SQLite DB**      | 🛠️ Project   | 🔄 **Planned** |
| B     | 6       | **Connecting Python to SQLite (sqlite3 Fundamentals)**       | 📚 Knowledge | 🔄 **Planned** |
| B     | 7       | **Parameterized Queries & Avoiding SQL Injection**           | 📚 Knowledge | 🔄 **Planned** |
| B     | 8       | **Simple Joins & Multi‑Table Designs (Intro Only)**          | 📚 Knowledge | 🔄 **Planned** |
| B     | 9       | **Migrating a File‑Based App to SQLite (End‑to‑End)**        | 📚 Knowledge | 🔄 **Planned** |
| B     | 10 (MP2) | **🚀 Mini Project 2: SQLite‑Backed Record Manager**           | 🛠️ Project   | 🔄 **Planned** |

**Key Learning Focus:**

**Phase A (Sessions 1–4 + MP1):**

- Understand **why and when** to move from CSV/JSON files to a relational database  
- Learn core relational concepts: tables, rows, columns, primary keys, simple relationships  
- Write basic SQL for everyday tasks: `SELECT`, `INSERT`, `UPDATE`, `DELETE`  
- Use `WHERE`, `ORDER BY`, and `LIMIT` to filter and sort data  
- **Mini Project 1: CLI over a Single‑Table SQLite DB** – e.g. a student/contact/task table with basic add/list/update/delete operations via SQL

**Phase B (Sessions 6–9 + MP2):**

- Use Python’s **sqlite3** module to connect, execute queries, and handle results  
- Use **parameterized queries** to keep code safe and avoid SQL injection patterns  
- Get a gentle introduction to **multi‑table designs and simple joins** without deep normalization theory  
- Practice taking a small **file‑based app from Level 5** and migrating its storage layer to SQLite  
- **Mini Project 2: SQLite‑Backed Record Manager** – e.g. a gradebook, contact manager, or inventory tool whose data now lives in SQLite instead of flat files

**Mini Projects:**

- **Single‑Table SQLite CLI Tool** – simple CRUD over one table using SQL directly  
- **SQLite‑Backed Record Manager** – small console app that stores and queries records using SQLite instead of CSV/JSON

**Learning Outcome:** "I can design a simple relational schema, write basic SQL queries, and connect a Python application to a SQLite database to store and retrieve data reliably."

**Exit Criteria:**

Before moving to Level 7, you should be able to:

- ✅ **Can you** design a simple schema with 2–3 related tables and explain the relationships?
- ✅ **Can you** write SQL queries for INSERT, SELECT, UPDATE, and DELETE operations?
- ✅ **Can you** use parameterized queries to prevent SQL injection?
- ✅ **Can you** explain when to use a database vs a JSON/CSV file?

**Reflection (Level 6):**

- What surprised me at this level?
- What was hardest — and what habit will I keep?
- What would I redesign in my mini project?
- What could I explain to a peer in five minutes?

---

### **🌐 Level 7: DB Beginner → Integration Novice** *(Intro to NoSQL & HTTP/JSON APIs)*

**Focus:** Gently introduce **NoSQL‑style thinking** and **HTTP/JSON APIs**, and show how to integrate external data with local storage.  
**Duration:** 5 hours (10 sessions × 30 min)  
**Status:** 🔄 **Planned**

**Actual Session Breakdown:**

| Phase | Session | Topic                                                          | Type         | Status         |
| ----- | ------- | -------------------------------------------------------------- | ------------ | -------------- |
| A     | 1       | **From Tables to Documents: NoSQL Concepts with JSON**        | 📚 Knowledge | 🔄 **Planned** |
| A     | 2       | **Using JSON Files as a Simple Document Store**               | 📚 Knowledge | 🔄 **Planned** |
| A     | 3       | **Modeling Data in Documents (Keys, Collections, Nested Data)**| 📚 Knowledge | 🔄 **Planned** |
| A     | 4       | **Query‑Like Operations over In‑Memory / File‑Based Docs**    | 📚 Knowledge | 🔄 **Planned** |
| A     | 5 (MP1) | **🚀 Mini Project 1: JSON‑Backed “NoSQL” Notes / Profile Store**| 🛠️ Project  | 🔄 **Planned** |
| B     | 6       | **HTTP & REST Basics: Requests, Responses, Status Codes**     | 📚 Knowledge | 🔄 **Planned** |
| B     | 7       | **Consuming JSON APIs with `requests` (GET + Query Params)**  | 📚 Knowledge | 🔄 **Planned** |
| B     | 8       | **Handling API Errors, Timeouts & Basic Response Validation** | 📚 Knowledge | 🔄 **Planned** |
| B     | 9       | **Combining APIs with Local Storage (Caching Remote Data)**   | 📚 Knowledge | 🔄 **Planned** |
| B     | 10 (MP2) | **🚀 Mini Project 2: API‑Powered App with Local JSON Cache**   | 🛠️ Project   | 🔄 **Planned** |

**Key Learning Focus:**

**Phase A (Sessions 1–4 + MP1):**

- Understand how **document‑style data** (nested JSON) differs from relational tables  
- Use JSON files as a simple, file‑based **document store** (pseudo‑NoSQL)  
- Practice modeling data in documents: choosing keys, nesting, and collections  
- Implement simple “query‑like” operations in Python (filters, searches) over in‑memory/file‑based JSON data  
- **Mini Project 1: JSON‑Backed Notes / Profile Store** – e.g. a notes/profile/tag manager that stores and retrieves data from JSON documents instead of tables

**Phase B (Sessions 6–9 + MP2):**

- Learn the basics of **HTTP & REST**: URLs, methods, status codes, and JSON payloads  
- Use the `requests` library to call public JSON APIs (GET, simple query params)  
- Handle common API problems: bad responses, timeouts, missing fields; add light validation/parsing  
- Combine **remote API data with local JSON storage** to cache results and reduce repeated calls  
- **Mini Project 2: API‑Powered App with Local JSON Cache** – e.g. a weather/dashboard/news viewer that fetches from an API, caches locally, and reads from cache when appropriate

**Mini Projects:**

- **JSON “NoSQL” Notes / Profile Store** – simple CRUD over JSON‑stored documents using Python filters and searches  
- **API‑Powered Cached App** – small console app that fetches JSON from a public API, stores it locally, and serves data from both sources

**Learning Outcome:** "I understand the basic ideas behind document‑style storage and HTTP/JSON APIs, and I can build small Python tools that fetch data from web APIs and persist them in JSON for later use."

**Exit Criteria:**

Before moving to Level 8, you should be able to:

- ✅ **Can you** explain when JSON documents are better than relational tables?
- ✅ **Can you** cache API data locally and explain cache invalidation risks?
- ✅ **Can you** handle API errors (timeouts, 404s, rate limits) gracefully?
- ✅ **Can you** make a GET request to a JSON API and parse the response?

**Reflection (Level 7):**

- What surprised me at this level?
- What was hardest — and what habit will I keep?
- What would I redesign in my mini project?
- What could I explain to a peer in five minutes?

---

### **🧹 Level 8: Integration Novice → Practitioner** *(Clean Code & Tooling — Part 2)*

**Focus:** Turn learners into **working practitioners** — clean-code habits, CLI tooling, Git, testing, optional **ADRs**.  
**Duration:** ~5 hours core + guided practice  
**Curriculum:** Draft · **Spiral:** pytest/Git/CLI/formatting — *Reinforcement* after L4/L7 introductions  
**Portfolio checkpoint:** MP2 should be a clone-and-run CLI in a Git repo.

**Actual Session Breakdown:**

| Phase | Session | Topic                                                          | Type         | Status         |
| ----- | ------- | -------------------------------------------------------------- | ------------ | -------------- |
| A     | 1       | **Practical KISS/DRY/YAGNI on Real Code**                      | 📚 Knowledge | 🔄 **Planned** |
| A     | 2       | **Building User‑Friendly CLIs (argparse / click Intro)**       | 📚 Knowledge | 🔄 **Planned** |
| A     | 3       | **Structuring Projects: Folders, Modules, and Entry Points**   | 📚 Knowledge | 🔄 **Planned** |
| A     | 4       | **Git Basics: Commits, Branches, and Clean Histories**        | 📚 Knowledge | 🔄 **Planned** |
| A     | 5 (MP1) | **🚀 Mini Project 1: CLI Wrapper Around an Existing Project**  | 🛠️ Project   | 🔄 **Planned** |
| B     | 6       | **Everyday Testing with pytest / unittest (No TDD Dogma)**    | 📚 Knowledge | 🔄 **Planned** |
| B     | 7       | **AI as Pair Programmer: Prompting for Refactoring & Code Review** | 📚 Knowledge | 🔄 **Planned** |
| B     | 8       | **Formatting & Linting (black, isort, flake8 – Concept Intro)**| 📚 Knowledge | 🔄 **Planned** |
| B     | 9       | **Polishing a Small Project: From Script to “Mini Product”**  | 📚 Knowledge | 🔄 **Planned** |
| B     | 10 (MP2) | **🚀 Mini Project 2: Polished, Tested CLI Tool in Git Repo**   | 🛠️ Project   | 🔄 **Planned** |

**Key Learning Focus:**

**Phase A (Sessions 1–4 + MP1):**

- Apply **KISS, DRY, YAGNI** directly to code they’ve already written (Levels 5–7)  
- Build simple but **friendly CLIs** (argparse or a gentle click intro) with clear help text and arguments  
- Learn to **lay out a small project**: where to put modules, how to define an entry point, and how to run it  
- Get comfortable with **Git basics**: init, status, meaningful commits, simple branching, and ignoring build artifacts  
- **Mini Project 1: CLI Wrapper Around an Existing Project** – wrap a prior mini project (e.g. Data Processor, SQLite manager, JSON cache) in a user‑friendly CLI and put it under version control

**Phase B (Sessions 6–9 + MP2):**

- Practice **lightweight testing** of real code with pytest or unittest (focus on arranging tests, not full TDD)  
- Use **AI as a pair programmer**: learn to prompt for refactoring suggestions, code explanations, and test generation (then review AI output critically – AI augments, doesn't replace understanding)  
- See how **formatting and linting tools** (black, isort, flake8) improve readability and consistency without going deep into configuration  
- Take one small project through a “polish” pass: tests, logging, CLI, basic docs/README, and a clean Git history  
- **Mini Project 2: Polished, Tested CLI Tool in Git Repo** – a small but “real” tool that someone else could clone and run

**Mini Projects:**

- **CLI‑Enhanced Existing Project** – turn a previous level’s project into a user‑friendly command‑line tool under Git  
- **Polished Practitioner‑Level Tool** – a small, well‑structured, tested, and documented CLI app that represents a learner’s first “portfolio‑ready” Python project

**Learning Outcome:** "I can structure, test, debug, version‑control, and polish small Python projects so they look and behave like real tools a teammate could use and maintain."

**Exit Criteria:**

Before moving to Level 9, you should be able to:

- ✅ Create a Git repository, make meaningful commits, and explain what changed in each commit
- ✅ Write at least 3 pytest tests that verify a function or class works correctly
- ✅ Use AI tools to generate test cases or refactoring suggestions, then review and adapt the output
- ✅ Run `black` and `flake8` on your code and fix the issues they find

**Common Anti-Patterns to Avoid:**

- ❌ **Blind AI Trust** – Using AI-generated code without understanding what it does
- ❌ **No Version Control** – Not using Git because "it's just a small project"
- ❌ **Tests That Don't Test** – Writing tests that always pass or test the wrong thing
- ❌ **Over-Configuration** – Spending hours configuring tools instead of using sensible defaults

**AI Usage Guidelines:**

- ✅ **Use AI for**: Explaining unfamiliar code, generating test cases, suggesting refactorings, finding bugs
- ✅ **Always**: Review AI output critically, understand what it does, and **test it yourself** (AI outputs must always be reviewed with tests or examples)
- ✅ **AI is a reasoning accelerator, not a correctness oracle** – verify everything
- ❌ **Don't**: Copy-paste AI code without understanding, rely on AI for core learning, skip manual practice

**Reflection (Level 8):**

- What surprised me at this level?
- What was hardest — and what habit will I keep?
- What would I redesign in my mini project?
- What could I explain to a peer in five minutes?
- What one ADR would I write for MP1 or MP2?

---

### **🏛️ Level 9: Practitioner → Patterned Coder** *(Design Patterns & Architecture)*

**Focus:** Learn a small, practical set of **design patterns and architectural habits** for building clearer, more maintainable small applications.  
**Duration:** 5 hours (10 sessions × 30 min)  
**Status:** 🔄 **Planned**

**Actual Session Breakdown:**

| Phase | Session | Topic                                                                  | Type         | Status         |
| ----- | ------- | ---------------------------------------------------------------------- | ------------ | -------------- |
| A     | 1       | **Why Patterns? When & When *Not* to Use Them**                       | 📚 Knowledge | 🔄 **Planned** |
| A     | 2       | **Strategy Pattern: Swappable Behaviours Without `if` Everywhere**    | 📚 Knowledge | 🔄 **Planned** |
| A     | 3       | **Factory / Creator Functions: Centralizing Object Creation**         | 📚 Knowledge | 🔄 **Planned** |
| A     | 4       | **Observer / Pub‑Sub (Intro to Event‑Driven Thinking)**               | 📚 Knowledge | 🔄 **Planned** |
| A     | 5 (MP1) | **🚀 Mini Project 1: Refactor to Use One Core Pattern**               | 🛠️ Project   | 🔄 **Planned** |
| B     | 6       | **Separation of Concerns & Layering (UI / Logic / Data)**             | 📚 Knowledge | 🔄 **Planned** |
| B     | 7       | **Decorator vs Inheritance: Extending Behaviour Safely**              | 📚 Knowledge | 🔄 **Planned** |
| B     | 8       | **SOLID‑Lite: SRP & Open/Closed in Small Python Projects**            | 📚 Knowledge | 🔄 **Planned** |
| B     | 9       | **Putting It Together: A Patterned, Layered Console Application**     | 📚 Knowledge | 🔄 **Planned** |
| B     | 10 (MP2) | **🚀 Mini Project 2: Patterned Console App / Plugin‑Style Tool**      | 🛠️ Project   | 🔄 **Planned** |

**Key Learning Focus:**

**Phase A (Sessions 1–4 + MP1):**

- Understand the **purpose and limits** of patterns – avoiding both “no structure” and “over‑engineering”  
- Learn the **Strategy pattern** to swap behaviours without big `if/elif` chains  
- Use simple **Factory / creator functions** (or tiny factory classes) to centralize how objects are constructed  
- Get an introductory feel for **Observer / pub‑sub** for event‑driven style flows in small apps  
- **Mini Project 1: Refactor to Use One Core Pattern** – take a previous project (e.g. calculator, data processor, CLI tool) and refactor one part to use Strategy or Factory where it clearly helps

**Phase B (Sessions 6–9 + MP2):**

- Practice **separation of concerns**: keeping UI, business logic, and persistence concerns in different modules or layers  
- Compare **Decorator vs inheritance** as ways to extend behaviour without breaking existing code  
- Apply **SOLID‑lite** (especially Single Responsibility and Open/Closed) to keep classes and functions focused and extensible  
- Design and implement a small **patterned, layered console application** that uses 1–2 patterns and a simple architectural structure  
- **Mini Project 2: Patterned Console App / Plugin‑Style Tool** – e.g. a notifier, rules engine, or plugin‑style CLI where behaviours can be swapped/extended via patterns

**Mini Projects:**

- **Pattern‑Refactored Existing Project** – enhance a familiar project by introducing a targeted pattern where it improves clarity or extensibility  
- **Patterned Console / Plugin Tool** – a small but well‑structured application that demonstrates Strategy/Factory/Observer/Decorator plus basic layering

**Learning Outcome:** "I can recognize when a small number of design patterns and architectural ideas will help, and I can apply them to structure my Python applications so they are easier to extend and maintain."

**Exit Criteria:**

Before moving to Level 10, you should be able to:

- ✅ **Can you** refactor a small application to use at least one design pattern (Strategy, Factory, or Observer) where it clearly improves the code?
- ✅ **Can you** explain when a pattern helps vs when it adds unnecessary complexity?
- ✅ **Can you** separate concerns into at least two distinct layers (e.g., UI vs business logic)?
- ✅ **Can you** identify when you're over-engineering and when you're under-engineering?
- ✅ **Can you** explain this system to a new teammate in 3 minutes? (Architecture Narrative)

**Common Anti-Patterns to Avoid:**

- ❌ **Pattern Overload** – Using patterns everywhere "just because" (violates YAGNI)
- ❌ **Premature Abstraction** – Creating interfaces and base classes before you have 2–3 concrete implementations
- ❌ **Anemic Domain Model** – All logic in services, classes are just data containers
- ❌ **Tight Coupling** – Classes that directly depend on concrete implementations instead of abstractions

**Architecture Narrative Exercise:**

From Level 9 onwards, practice explaining your system architecture:

- **Can you** explain why each component exists? (What would break if we removed it?)
- **Can you** explain this system to a new teammate in 3 minutes?
- **Can you** identify the boundaries between layers and explain their responsibilities?

This builds architectural communication skills essential for professional development.

**Reflection (Level 9):**

- What surprised me at this level?
- What was hardest — and what habit will I keep?
- What would I redesign in my mini project?
- What could I explain to a peer in five minutes?
- What one ADR would I write for MP1 or MP2?

---

### **🧰 Level 10: Patterned Coder → Stdlib Specialist** *(Python Standard Library Mastery)*

**Focus:** Become confident with the **core Python Standard Library** so you reach for built‑in tools instead of reinventing them.  
**Duration:** 5 hours (10 sessions × 30 min)  
**Status:** 🔄 **Planned**

**Actual Session Breakdown:**

| Phase | Session | Topic                                                          | Type         | Status         |
| ----- | ------- | -------------------------------------------------------------- | ------------ | -------------- |
| A     | 1       | **Filesystem Essentials with `os` and `pathlib`**             | 📚 Knowledge | 🔄 **Planned** |
| A     | 2       | **Dates & Times with `datetime` and `time`**                  | 📚 Knowledge | 🔄 **Planned** |
| A     | 3       | **Smart Collections: `collections` (Counter, defaultdict, etc.)** | 📚 Knowledge | 🔄 **Planned** |
| A     | 4       | **Efficient Iteration with `itertools`**                      | 📚 Knowledge | 🔄 **Planned** |
| A     | 5 (MP1) | **🚀 Mini Project 1: File & Data Utility Powered by Stdlib**   | 🛠️ Project   | 🔄 **Planned** |
| B     | 6       | **System & Environment Info with `sys` and `platform`**       | 📚 Knowledge | 🔄 **Planned** |
| B     | 7       | **Running Other Programs Safely with `subprocess`**           | 📚 Knowledge | 🔄 **Planned** |
| B     | 8       | **Structured Logging with `logging`**                         | 📚 Knowledge | 🔄 **Planned** |
| B     | 9       | **Text & Pattern Matching with `re` (Regex Intro)**           | 📚 Knowledge | 🔄 **Planned** |
| B     | 10 (MP2) | **🚀 Mini Project 2: Stdlib‑Powered System / Log Toolkit**     | 🛠️ Project   | 🔄 **Planned** |

**Key Learning Focus:**

**Phase A (Sessions 1–4 + MP1):**

- Use `os` and `pathlib` to **inspect and manipulate the filesystem** in a cross‑platform way  
- Work with `datetime` and `time` to generate timestamps, do simple date/time math, and schedule repeated actions  
- Leverage `collections` (such as `Counter`, `defaultdict`, and `namedtuple`) to simplify common data‑processing patterns  
- Use `itertools` to express more complex loops (combinations, grouping, chaining) succinctly and efficiently  
- **Mini Project 1: File & Data Utility Powered by Stdlib** – e.g. a log summarizer, file organizer, or mini report generator that leans heavily on these stdlib modules

**Phase B (Sessions 6–9 + MP2):**

- Use `sys` and `platform` to **inspect the environment and runtime**, making scripts more portable and introspective  
- Learn to use `subprocess` to run other programs safely (capturing output, handling errors) instead of shelling out ad‑hoc  
- Introduce the `logging` module to replace ad‑hoc prints with **structured, configurable logs**  
- Use `re` for basic text and pattern matching (validation, simple extract/replace operations) in a safe, beginner‑friendly way  
- **Mini Project 2: Stdlib‑Powered System / Log Toolkit** – e.g. a system info dashboard, log/backup organizer, or pattern‑based file processor that demonstrates practical use of multiple stdlib modules

**Mini Projects:**

- **File & Data Utility** – small console tool that organizes files, summarizes logs, or produces simple reports using `os`, `pathlib`, `datetime`, and `collections`  
- **System / Log Toolkit** – a utility that inspects the environment, runs subprocesses, logs activity, and does basic regex‑based filtering

**Learning Outcome:** "I can confidently use Python's Standard Library to work with files, dates, collections, system information, subprocesses, logging, and simple text patterns, so I reach for built‑in modules first when solving everyday problems."

**Exit Criteria:**

Before moving to Level 11, you should be able to:

- ✅ **Can you** use `pathlib` to work with file paths in a cross-platform way?
- ✅ **Can you** use `datetime` to parse dates, format them, and do simple date arithmetic?
- ✅ **Can you** use `collections.Counter` or `defaultdict` to simplify a data-processing task?
- ✅ **Can you** explain why you'd use stdlib modules instead of writing custom code?

**Reflection (Level 10):**

- What surprised me at this level?
- What was hardest — and what habit will I keep?
- What would I redesign in my mini project?
- What could I explain to a peer in five minutes?
- What one ADR would I write for MP1 or MP2?

---

### **🔌 Level 11: Stdlib Specialist → Pro Toolsmith** *(Third‑Party Ecosystem)*

**Focus:** Get comfortable with a **curated set of third‑party libraries and tools** that show up in real Python projects (HTTP, spreadsheets, CLIs, testing, config).  
**Duration:** 5 hours (10 sessions × 30 min)  
**Status:** 🔄 **Planned**

**Actual Session Breakdown:**

| Phase | Session | Topic                                                                  | Type         | Status         |
| ----- | ------- | ---------------------------------------------------------------------- | ------------ | -------------- |
| A     | 1       | **Third‑Party Libraries 101: pip, venvs & Choosing Dependencies**     | 📚 Knowledge | 🔄 **Planned** |
| A     | 2       | **HTTP & JSON APIs with `requests` (GET + Params + JSON)**            | 📚 Knowledge | 🔄 **Planned** |
| A     | 3       | **Working with Excel & Tabular Data using `openpyxl`**                | 📚 Knowledge | 🔄 **Planned** |
| A     | 4       | **Configuration & Secrets: `.env`, `configparser`, Basic Validation** | 📚 Knowledge | 🔄 **Planned** |
| A     | 5 (MP1) | **🚀 Mini Project 1: API‑to‑Excel Reporter CLI**                       | 🛠️ Project   | 🔄 **Planned** |
| B     | 6       | **Building Polished CLIs with `click`**                               | 📚 Knowledge | 🔄 **Planned** |
| B     | 7       | **Better Terminal UX with `rich` and Progress with `tqdm`**           | 📚 Knowledge | 🔄 **Planned** |
| B     | 8       | **Everyday Testing with `pytest` (Basics & Parametrized Tests)**      | 📚 Knowledge | 🔄 **Planned** |
| B     | 9       | **Formatting & Linting in Practice (black, isort, flake8 Intro)**     | 📚 Knowledge | 🔄 **Planned** |
| B     | 10 (MP2) | **🚀 Mini Project 2: Fully Tooled CLI App in a Clean Repo**           | 🛠️ Project   | 🔄 **Planned** |

**Key Learning Focus:**

**Phase A (Sessions 1–4 + MP1):**

- Understand how to **install and manage dependencies** safely (pip, virtual environments at a conceptual level)  
- Use `requests` to call real JSON APIs (status codes, basic error handling, decoding JSON)  
- Read and write **Excel workbooks** with `openpyxl`, and relate them to CSV/JSON workflows from earlier levels  
- Store configuration and secrets more safely with `.env`‑style files and `configparser` / simple validation patterns  
- **Mini Project 1: API‑to‑Excel Reporter CLI** – for example, fetch from a public API and write a cleaned/filtered summary into an Excel file via a CLI

**Phase B (Sessions 6–9 + MP2):**

- Build **user‑friendly CLIs** with `click` (commands, options, help text)  
- Improve terminal UX using `rich` (colours, tables) and `tqdm` for progress bars on longer operations  
- Write and run **pytest** tests for a small project (basic assertions, parametrized tests, simple fixtures)  
- Introduce an opinionated **format/lint workflow** (black, isort, flake8) and wire them into the everyday dev loop  
- **Mini Project 2: Fully Tooled CLI App** – a small, realistic CLI (e.g. data fetcher/reporter) that uses `requests`, `openpyxl` or CSV, `click`, `rich`/`tqdm`, pytest tests, and basic formatting/linting in a clean Git repo

**Mini Projects:**

- **API‑to‑Excel Reporter CLI** – fetch JSON data from an API and export it into Excel with a simple CLI interface  
- **Fully Tooled CLI App** – a portfolio‑ready CLI that demonstrates dependency management, good UX, tests, and basic formatting/linting

**Learning Outcome:** "I can confidently bring in and use key third‑party libraries – for HTTP APIs, spreadsheets, CLIs, testing, and formatting – and wire them into small projects that look and feel like real, professional Python tools."

**Exit Criteria:**

Before moving to Level 12, you should be able to:

- ✅ **Can you** use `requests` to call a JSON API and handle errors gracefully?
- ✅ **Can you** write at least 3 pytest tests with parametrization or fixtures?
- ✅ **Can you** use `click` to build a CLI with commands and options?
- ✅ **Can you** explain when to add a third-party library vs using stdlib?

**Reflection (Level 11):**

- What surprised me at this level?
- What was hardest — and what habit will I keep?
- What would I redesign in my mini project?
- What could I explain to a peer in five minutes?
- What one ADR would I write for MP1 or MP2?

---

### **🚀 Level 12: Pro Toolsmith → Curious Learner** *(Advanced Features & Packaging Capstone)*

**Focus:** Explore **advanced Python features and packaging**, and build a small, shareable project that ties the entire journey together.  
**Duration:** 5 hours (10 sessions × 30 min)  
**Status:** 🔄 **Planned**

**Actual Session Breakdown:**

| Phase | Session | Topic                                                                | Type         | Status         |
| ----- | ------- | -------------------------------------------------------------------- | ------------ | -------------- |
| A     | 1       | **When to Reach for Advanced Features (Trade‑offs & Pitfalls)**     | 📚 Knowledge | 🔄 **Planned** |
| A     | 2       | **Generators, Iterators & Lazy Evaluation (Beyond `for` Loops)**    | 📚 Knowledge | 🔄 **Planned** |
| A     | 3       | **Concurrency Basics: `threading` vs `multiprocessing`**            | 📚 Knowledge | 🔄 **Planned** |
| A     | 4       | **Asyncio Intro: `async`/`await` and Event Loops (Conceptual)**     | 📚 Knowledge | 🔄 **Planned** |
| A     | 5 (MP1) | **🚀 Mini Project 1: Simple Concurrent / Async Fetcher or Worker**   | 🛠️ Project   | 🔄 **Planned** |
| B     | 6       | **Measuring Performance with `timeit` and `cProfile`**              | 📚 Knowledge | 🔄 **Planned** |
| B     | 7       | **Practical Optimization: Hot Spots, Caching & Small Refactors**    | 📚 Knowledge | 🔄 **Planned** |
| B     | 8       | **Packaging & Distribution: `pyproject.toml`, Wheels & venv Basics**| 📚 Knowledge | 🔄 **Planned** |
| B     | 9       | **Sharing Your Work: Publishing, Docs, and Next‑Step Roadmaps**     | 📚 Knowledge | 🔄 **Planned** |
| B     | 10 (MP2) | **🚀 Mini Project 2: Installable Capstone Package / CLI Tool**       | 🛠️ Project   | 🔄 **Planned** |

**Key Learning Focus:**

**Phase A (Sessions 1–4 + MP1):**

- Build intuition for **when** advanced features (generators, concurrency, async) are helpful and when they add unnecessary complexity  
- Go beyond basic iteration with **generators and iterators** to produce values lazily and compose data pipelines more efficiently  
- Compare **threads vs processes** conceptually and try simple parallelization patterns for I/O‑bound vs CPU‑bound tasks  
- Get a high‑level, beginner‑friendly view of **asyncio** and `async`/`await`, with at least one small, clear example  
- **Mini Project 1: Simple Concurrent / Async Fetcher or Worker** – e.g. a multi‑URL fetcher, thumbnail generator, or parallel file checker that demonstrates one concrete concurrency/async benefit

**Phase B (Sessions 6–9 + MP2):**

- Use `timeit` and `cProfile` to **measure performance** and find hot spots instead of guessing  
- Apply a few **simple optimizations** (better data structures, caching, avoiding redundant work) driven by measurement  
- Learn the basics of **packaging and distribution**: `pyproject.toml`, building a wheel, and using virtual environments to test installs  
- Discuss how to **share and grow** a project: hosted docs, READMEs, simple changelogs, and paths toward open‑source contribution or further specialization  
- **Mini Project 2: Installable Capstone Package / CLI Tool** – turn a small but meaningful project (possibly from an earlier level) into an installable package or CLI with a `pyproject.toml`, basic docs, and at least a local/TestPyPI installation

**Mini Projects:**

- **Concurrent / Async Mini Tool** – a compact project that clearly demonstrates one advantage of concurrency or async in a controlled, understandable way  
- **Capstone Package / CLI** – a polished, installable project that showcases the learner’s end‑to‑end skills from Level 1 through advanced Python features and packaging

**Learning Outcome:** "I understand what advanced Python features can do, when to use them, and how to package and share my own tools, so I can keep exploring Python with curiosity and confidence beyond this course."

**Exit Criteria:**

Before moving to Level 13, you should be able to:

- ✅ **Can you** explain when to use generators vs regular functions?
- ✅ **Can you** explain the difference between `threading` and `multiprocessing` conceptually?
- ✅ **Can you** create a simple installable package with `pyproject.toml`?
- ✅ **Can you** measure performance with `timeit` and identify a bottleneck?

**Reflection (Level 12):**

- What surprised me at this level?
- What was hardest — and what habit will I keep?
- What would I redesign in my mini project?
- What could I explain to a peer in five minutes?
- What one ADR would I write for MP1 or MP2?

---

### **🗄️ Level 13: Curious Learner → Data Platform Explorer** *(Production Relational Databases — Part 3)*

**Focus:** Production-grade relational databases (SQL Server, PostgreSQL) from Python.  
**Duration:** 10 × 30 min guided + **~6–10 h guided labs** (setup, port, SQLAlchemy)  
**Curriculum:** Draft · **Stretch:** full migration automation optional

**Actual Session Breakdown:**

| Phase | Session | Topic                                                                                 | Type         | Status         |
| ----- | ------- | ------------------------------------------------------------------------------------- | ------------ | -------------- |
| A     | 1       | **SQL Server & PostgreSQL Overview: Architecture, Tools & Local Setup**              | 📚 Knowledge | 🔄 **Planned** |
| A     | 2       | **Connecting from Python: Drivers, Connection Strings & Parameterized Queries**      | 📚 Knowledge | 🔄 **Planned** |
| A     | 3       | **Schemas, Keys & Constraints in Production Databases**                              | 📚 Knowledge | 🔄 **Planned** |
| A     | 4       | **Indexes & Query Performance 101 (Execution Plans at a Glance)**                    | 📚 Knowledge | 🔄 **Planned** |
| A     | 5 (MP1) | **🚀 Mini Project 1: Port a SQLite App to PostgreSQL or SQL Server**                 | 🛠️ Project   | 🔄 **Planned** |
| B     | 6       | **Working with SQLAlchemy (Core + Simple ORM Models)**                               | 📚 Knowledge | 🔄 **Planned** |
| B     | 7       | **Environments & Migrations: Dev/Test/Prod, Alembic‑Style Migration Basics**         | 📚 Knowledge | 🔄 **Planned** |
| B     | 8       | **Multi‑Database Support & Vendor Differences (SQLite vs PostgreSQL vs SQL Server)** | 📚 Knowledge | 🔄 **Planned** |
| B     | 9       | **Designing a Reusable Data Access Layer for a Small App**                           | 📚 Knowledge | 🔄 **Planned** |
| B     | 10 (MP2) | **🚀 Mini Project 2: Production‑Style Data Layer Library / Module**                   | 🛠️ Project   | 🔄 **Planned** |

**Key Learning Focus:**

**Phase A (Sessions 1–4 + MP1):**

- Understand the **role of enterprise databases** and how SQL Server and PostgreSQL fit into real systems  
- Install and use basic tools (`sqlcmd` / SQL Server Management Studio, `psql` / pgAdmin) to inspect databases and run queries  
- Connect to SQL Server/PostgreSQL from Python using appropriate drivers and **safe, parameterized queries**  
- Design and refine schemas with **primary keys, foreign keys, unique constraints, and basic normalization**  
- Read simple **execution plans**, add indexes, and observe how they affect query performance  
- **Mini Project 1: Port a SQLite App to PostgreSQL or SQL Server** – take a Level 6‑style app and move its data layer to a real RDBMS, updating connection code and SQL where needed

**Phase B (Sessions 6–9 + MP2):**

- Use **SQLAlchemy Core and a small slice of ORM** to reduce boilerplate and model tables as Python classes  
- Understand **environment separation** (dev/test/prod) and the concept of migrations (Alembic‑style) for evolving schemas over time  
- Compare vendor differences (types, AUTO INCREMENT vs IDENTITY/SERIAL, LIMIT/OFFSET vs TOP) and design code that can adapt where reasonable  
- Organize a **reusable data access layer** (DAL) as a module that can be imported by services/CLIs in later levels  
- **Mini Project 2: Production‑Style Data Layer Library / Module** – package a small DAL (for tasks/orders/etc.) that supports SQLite in dev and PostgreSQL or SQL Server in “production” using configuration

**Mini Projects:**

- **SQLite → Postgres/SQL Server Migration** – update a previous SQLite‑backed mini‑project to run on PostgreSQL or SQL Server with proper connection handling and schema setup  
- **Reusable Data Layer Module** – a small but realistic DAL package that other projects in later levels can import and build on

**Learning Outcome:** "I can connect Python applications to production‑grade relational databases (SQL Server and PostgreSQL), design sensible schemas with keys and indexes, and build a small, reusable data layer that prepares me for real backend work."

**Reflection (Level 13):**

- What surprised me at this level?
- What was hardest — and what habit will I keep?
- What would I redesign in my mini project?
- What could I explain to a peer in five minutes?
- What one ADR would I write for MP1 or MP2?

---

### **🧱 Level 14: Data Platform Explorer → Data Systems Builder** *(Document DBs & Caching)*

**Focus:** Learn to **model data for a document database** and use **Redis as a cache/key‑value store**, understanding when and why to choose them and how to integrate them with your existing relational stack.  
**Duration:** 5 hours (10 sessions × 30 min)  
**Status:** 🔄 **Planned**

**Actual Session Breakdown:**

| Phase | Session | Topic                                                                                          | Type         | Status         |
| ----- | ------- | ---------------------------------------------------------------------------------------------- | ------------ | -------------- |
| A     | 1       | **Document Databases 101: Collections, Documents & When to Use Them**                         | 📚 Knowledge | 🔄 **Planned** |
| A     | 2       | **Hands‑On with a Mongo‑Style Document DB from Python (CRUD & Simple Queries)**               | 📚 Knowledge | 🔄 **Planned** |
| A     | 3       | **Modeling in a Document DB: Embedding vs Referencing & Basic Aggregations**                  | 📚 Knowledge | 🔄 **Planned** |
| A     | 4       | **Indexes, Query Patterns & Evolving Schemas in Document DBs**                                | 📚 Knowledge | 🔄 **Planned** |
| A     | 5 (MP1) | **🚀 Mini Project 1: Document‑Backed Feature for an Existing App**                             | 🛠️ Project   | 🔄 **Planned** |
| B     | 6       | **Redis Fundamentals: Keys, Expiry & Basic Data Structures**                                  | 📚 Knowledge | 🔄 **Planned** |
| B     | 7       | **Caching Patterns with Redis: Read‑Through, Write‑Through & TTL‑Based Caches**              | 📚 Knowledge | 🔄 **Planned** |
| B     | 8       | **Combining Relational + Document DB + Redis in a Small System**                              | 📚 Knowledge | 🔄 **Planned** |
| B     | 9       | **Connection Management, Timeouts & Configuration for Doc DB + Redis**                        | 📚 Knowledge | 🔄 **Planned** |
| B     | 10 (MP2) | **🚀 Mini Project 2: Hybrid Data Stack Demo (RDBMS + Document DB + Redis Cache)**             | 🛠️ Project   | 🔄 **Planned** |

**Key Learning Focus:**

**Phase A (Sessions 1–4 + MP1):**

- Understand when **document databases** are a better fit than strict relational schemas (flexible documents, evolving fields, nested data)  
- Learn core concepts: collections, documents, `_id`, basic queries and filters, and how they relate to JSON and Python dicts  
- Practice **modeling data** using embedding vs referencing, and run simple aggregation‑style queries for summaries/reports  
- See how **indexes** improve common query patterns and what “schema on read” feels like in practice  
- **Mini Project 1: Document‑Backed Feature** – add a feature (e.g. activity log, flexible profile, settings, or audit history) to an existing app using a document DB instead of a relational table

**Phase B (Sessions 6–9 + MP2):**

- Learn **Redis basics**: connecting, setting/getting keys, expirations (TTL), and a small set of core data structures (strings, hashes, lists)  
- Implement simple **caching patterns**: cached lookups, per‑user data cache, rate‑limit‑style counters using TTLs  
- Design a tiny system that uses **relational DB for core records**, **document DB for flexible/secondary data**, and **Redis for fast caching**  
- Apply **connection management and configuration** patterns: environment variables, connection pooling concepts, sane timeouts/fallbacks  
- **Mini Project 2: Hybrid Data Stack Demo** – a small API/CLI that reads/writes from RDBMS, stores flexible metadata in a document DB, and uses Redis to cache expensive reads

**Mini Projects:**

- **Document‑Backed Feature** – enhance a previous relational project by moving one flexible/optional data area into a document DB  
- **Hybrid Data Stack Demo** – a small end‑to‑end example that combines RDBMS, document DB, and Redis caching in a coherent, understandable way

**Learning Outcome:** "I can choose when to use a document database versus a relational database, integrate a Mongo‑style document store and Redis into a Python application, and design small systems that use the right data store for the right job."

**Reflection (Level 14):**

- What surprised me at this level?
- What was hardest — and what habit will I keep?
- What would I redesign in my mini project?
- What could I explain to a peer in five minutes?
- What one ADR would I write for MP1 or MP2?

---

### **📡 Level 15: Data Systems Builder → Service Integrator** *(Messaging, Streaming & Deep Testing)*

**Focus:** Understand **messaging and streaming systems** (RabbitMQ & Kafka) and learn how to design, test, and debug small **message‑driven Python services** with solid unit and integration tests.  
**Duration:** 5 hours (10 sessions × 30 min)  
**Status:** 🔄 **Planned**

**Actual Session Breakdown:**

| Phase | Session | Topic                                                                                  | Type         | Status         |
| ----- | ------- | -------------------------------------------------------------------------------------- | ------------ | -------------- |
| A     | 1       | **Messaging & Streaming 101: Queues, Topics & When to Use Them**                      | 📚 Knowledge | 🔄 **Planned** |
| A     | 2       | **RabbitMQ from Python: Producers, Consumers & Acknowledgements**                     | 📚 Knowledge | 🔄 **Planned** |
| A     | 3       | **Kafka from Python: Topics, Partitions & Simple Consumer Groups**                    | 📚 Knowledge | 🔄 **Planned** |
| A     | 4       | **Designing Message‑Driven Flows for a Small Application**                            | 📚 Knowledge | 🔄 **Planned** |
| A     | 5 (MP1) | **🚀 Mini Project 1: RabbitMQ‑Backed Background Worker for an Existing Feature**      | 🛠️ Project   | 🔄 **Planned** |
| B     | 6       | **Advanced Unit Testing: Mocks, Fakes & Testing Around Message Boundaries**          | 📚 Knowledge | 🔄 **Planned** |
| B     | 7       | **Integration Testing with Real Infrastructure (DB + RabbitMQ + Kafka via Containers)** | 📚 Knowledge | 🔄 **Planned** |
| B     | 8       | **Contract & Schema Testing for Messages (Payload Validation & Backwards Compatibility)** | 📚 Knowledge | 🔄 **Planned** |
| B     | 9       | **End‑to‑End Scenarios & Debugging Asynchronous Flows**                              | 📚 Knowledge | 🔄 **Planned** |
| B     | 10 (MP2) | **🚀 Mini Project 2: Message‑Driven Mini Service with Full Test Suite**               | 🛠️ Project   | 🔄 **Planned** |

**Key Learning Focus:**

**Phase A (Sessions 1–4 + MP1):**

- Build a clear intuition for **why messaging/streaming exists** (decoupling, buffering, resilience) and basic trade‑offs versus direct HTTP calls  
- Learn core RabbitMQ concepts (exchanges, queues, bindings) and implement a simple **producer/consumer** pair in Python with acknowledgements  
- Learn core Kafka concepts (topics, partitions, offsets, consumer groups) and implement a **basic producer and consumer** in Python  
- Design a **message‑driven flow** for a small feature (commands vs events, idempotent processing at a conceptual level)  
- **Mini Project 1: RabbitMQ‑Backed Background Worker** – take an existing feature (e.g. email sending, report generation, thumbnail creation) and move the heavy work into a RabbitMQ worker process

**Phase B (Sessions 6–9 + MP2):**

- Deepen **unit testing** skills at service boundaries using mocks/fakes for message brokers and external systems  
- Set up **integration tests** that run against real infrastructure (databases, RabbitMQ, Kafka) using local containers or test instances  
- Introduce simple **contract/schema testing** for message payloads so producers and consumers stay compatible over time  
- Practice designing and running **end‑to‑end test scenarios** that cover async behaviour, retries, and failure handling paths  
- **Mini Project 2: Message‑Driven Mini Service with Full Test Suite** – build a tiny but realistic service that processes messages via RabbitMQ/Kafka and is covered by unit, integration, and basic contract tests

**Mini Projects:**

- **RabbitMQ‑Backed Background Worker** – offload one expensive operation from a previous project into an asynchronous worker using RabbitMQ  
- **Message‑Driven Mini Service with Tests** – a small but complete service that demonstrates messaging, streaming concepts, and robust testing around them

**Learning Outcome:** "I can design small message‑driven Python services that use RabbitMQ and Kafka, and I know how to write unit, integration, and basic contract tests so that these services remain reliable as they evolve."

**Reflection (Level 15):**

- What surprised me at this level?
- What was hardest — and what habit will I keep?
- What would I redesign in my mini project?
- What could I explain to a peer in five minutes?
- What one ADR would I write for MP1 or MP2?

---

### **🌐 Level 16: Service Integrator → Service Builder** *(End‑to‑End Service Foundations)*

**Focus:** Build a **small, end‑to‑end HTTP service** that exposes APIs, talks to real databases, and is structured with clear layers and tests – turning all previous levels into a working service.  
**Duration:** 5 hours (10 sessions × 30 min)  
**Status:** 🔄 **Planned**

**Actual Session Breakdown:**

| Phase | Session | Topic                                                                                  | Type         | Status         |
| ----- | ------- | -------------------------------------------------------------------------------------- | ------------ | -------------- |
| A     | 1       | **From Scripts to Services: HTTP, REST & Resource Modeling Basics**                   | 📚 Knowledge | 🔄 **Planned** |
| A     | 2       | **Designing API Endpoints & Request/Response Schemas (JSON Contracts)**               | 📚 Knowledge | 🔄 **Planned** |
| A     | 3       | **Implementing a Simple CRUD API with a Python Web Framework**                        | 📚 Knowledge | 🔄 **Planned** |
| A     | 4       | **Hooking the API to the Data Layer (DB Repositories + Basic Validation)**            | 📚 Knowledge | 🔄 **Planned** |
| A     | 5 (MP1) | **🚀 Mini Project 1: CRUD Microservice for an Existing Domain (Tasks/Contacts/etc.)** | 🛠️ Project   | 🔄 **Planned** |
| B     | 6       | **Service Structure: Routers/Controllers, Services & Repositories**                   | 📚 Knowledge | 🔄 **Planned** |
| B     | 7       | **Basic Security & Guardrails: Simple Auth, Input Validation & Error Handling**       | 📚 Knowledge | 🔄 **Planned** |
| B     | 8       | **Testing the Service: Unit Tests for Logic, Functional Tests for Endpoints**         | 📚 Knowledge | 🔄 **Planned** |
| B     | 9       | **Running the Service Locally: Environments, Config & Simple Documentation**          | 📚 Knowledge | 🔄 **Planned** |
| B     | 10 (MP2) | **🚀 Mini Project 2: End‑to‑End Service with DB, Tests & API Documentation**          | 🛠️ Project   | 🔄 **Planned** |

**Key Learning Focus:**

**Phase A (Sessions 1–4 + MP1):**

- Understand how to go from **Python scripts** to a simple **HTTP/JSON API** that exposes clear resources (tasks, users, orders, etc.)  
- Design **endpoint contracts** (URLs, methods, request/response bodies, status codes) and represent them as JSON schemas or simple models  
- Implement a small CRUD API using a modern Python web framework (e.g. FastAPI or Flask) with clear separation between routing and logic  
- Connect API endpoints to the **existing data layer** (from Levels 6, 13, 14) via repository functions, with basic validation and error handling  
- **Mini Project 1: CRUD Microservice** – build a minimal but real microservice (e.g. Task/Contact/Order service) that supports create/read/update/delete via HTTP

**Phase B (Sessions 6–9 + MP2):**

- Apply layering: **routers/controllers → services → repositories**, and keep business rules out of the HTTP layer  
- Add basic **auth/guardrails** appropriate to the course level (e.g. simple API key or token stub, role‑less auth, or “owner‑only” checks)  
- Write tests at two levels: **unit tests** for business logic and repository functions, and **functional tests** for HTTP endpoints (using a test client)  
- Run the service locally with simple **environment‑based configuration**, and provide lightweight **API documentation** (OpenAPI/docs page or Markdown)  
- **Mini Project 2: End‑to‑End Service** – an API service that uses a real DB, has clear layers, includes tests, and is documented enough for another learner to consume

**Mini Projects:**

- **CRUD Microservice** – a small REST‑style API wrapped around an existing domain (tasks, contacts, inventory, etc.) backed by a real database  
- **End‑to‑End Service with Docs** – a more polished version with layers, tests, error handling, and basic documentation for consumers

**Learning Outcome:** "I can design and implement a small, well‑structured HTTP API service in Python that talks to real databases, has clear layers, and is covered by meaningful tests and documentation."

**Reflection (Level 16):**

- What surprised me at this level?
- What was hardest — and what habit will I keep?
- What would I redesign in my mini project?
- What could I explain to a peer in five minutes?
- What one ADR would I write for MP1 or MP2?

---

### **🛡️ Level 17: Service Builder → Systems Crafter** *(Service Hardening & Observability)*

**Focus:** Make services **robust and observable** by improving configuration, logging, metrics, health checks, and learning how to run them in **Docker‑based environments** that feel closer to production.  
**Duration:** 5 hours (10 sessions × 30 min)  
**Status:** 🔄 **Planned**

**Actual Session Breakdown:**

| Phase | Session | Topic                                                                                   | Type         | Status         |
| ----- | ------- | --------------------------------------------------------------------------------------- | ------------ | -------------- |
| A     | 1       | **Service Hardening 101: Failure Modes, Timeouts & Retries**                           | 📚 Knowledge | 🔄 **Planned** |
| A     | 2       | **Structured Logging & Log Levels for Services**                                       | 📚 Knowledge | 🔄 **Planned** |
| A     | 3       | **Configuration Management: Env Vars, Config Files & 12‑Factor Basics**               | 📚 Knowledge | 🔄 **Planned** |
| A     | 4       | **Health Checks & Basic Metrics (Counters, Timers, Gauges)**                           | 📚 Knowledge | 🔄 **Planned** |
| A     | 5 (MP1) | **🚀 Mini Project 1: Harden an Existing Service (Timeouts, Logs, Health Endpoint)**    | 🛠️ Project   | 🔄 **Planned** |
| B     | 6       | **Docker for Python Services: Writing a Simple, Production‑Friendly Dockerfile**      | 📚 Knowledge | 🔄 **Planned** |
| B     | 7       | **Docker Compose: Running Service + DB/Redis/RabbitMQ Together Locally**               | 📚 Knowledge | 🔄 **Planned** |
| B     | 8       | **Observability in Containers: Logs, Metrics & Simple Dashboards**                     | 📚 Knowledge | 🔄 **Planned** |
| B     | 9       | **Production‑Like Environments: Resource Limits, Readiness & Rollout Basics**          | 📚 Knowledge | 🔄 **Planned** |
| B     | 10 (MP2) | **🚀 Mini Project 2: Containerized, Observable Mini Stack (Service + Infra)**          | 🛠️ Project   | 🔄 **Planned** |

**Key Learning Focus:**

**Phase A (Sessions 1–4 + MP1):**

- Identify common **failure modes** in services (network errors, timeouts, partial failures) and introduce basic timeouts/retries where appropriate  
- Use **structured logging** and log levels (DEBUG/INFO/WARN/ERROR) to make issues diagnosable in production‑like environments  
- Apply simple **configuration management** patterns: environment variables, layered configs, secrets separation, and 12‑factor‑style ideas  
- Implement lightweight **health and readiness checks** plus **basic metrics** (e.g. request counts, latency timings, error rates) using a friendly Python metrics library  
- **Mini Project 1: Harden an Existing Service** – take the Level 16 service and add better error handling, logging, configuration, and a `/health`‑style endpoint with simple metrics

**Phase B (Sessions 6–9 + MP2):**

- Write a **production‑friendly Dockerfile** for a Python service (small image, clear entrypoint, correct working directory and dependencies)  
- Use **Docker Compose** to run a local stack: service + database + Redis/RabbitMQ, wiring configuration via environment variables  
- Learn how to **collect logs and metrics from containers**, and view them in simple dashboards or CLI tools for troubleshooting  
- Understand high‑level **deployment concepts**: resource limits, graceful shutdown, rolling restarts, and what “production‑like” really means for learners  
- **Mini Project 2: Containerized, Observable Mini Stack** – package the Level 16/17 service and its dependencies into a small Docker Compose setup, complete with logs, health checks, and basic metrics

**Mini Projects:**

- **Hardened Service** – a version of the Level 16 API with improved configuration, logging, health checks, and basic metrics  
- **Observable Containerized Stack** – a small multi‑container environment (service + infra) that demonstrates how to run, observe, and troubleshoot a Python service

**Learning Outcome:** "I can take a working Python service and harden it with better configuration, logging, health checks, metrics, and Docker‑based deployment so it behaves more like a real production system."

**Reflection (Level 17):**

- What surprised me at this level?
- What was hardest — and what habit will I keep?
- What would I redesign in my mini project?
- What could I explain to a peer in five minutes?
- What one ADR would I write for MP1 or MP2?

---

### **🏁 Level 18: Systems Crafter → Curious Professional** *(Capstone Project & Portfolio)*

**Focus:** Consolidate everything into a **single capstone project** with real‑world structure, docs, tests, packaging, and CI/CD – and turn it into a strong **portfolio piece and learning roadmap**.  
**Duration:** 5 hours (10 sessions × 30 min)  
**Status:** 🔄 **Planned**

**Actual Session Breakdown:**

| Phase | Session | Topic                                                                                                 | Type         | Status         |
| ----- | ------- | ----------------------------------------------------------------------------------------------------- | ------------ | -------------- |
| A     | 1       | **Choosing & Scoping Your Capstone (Domain, Users, Success Criteria)**                               | 📚 Knowledge | 🔄 **Planned** |
| A     | 2       | **Writing a Lightweight Design Doc (Architecture, Data, Interfaces)**                                | 📚 Knowledge | 🔄 **Planned** |
| A     | 3       | **Integrating Building Blocks: DB, Caching, Messaging & HTTP APIs**                                  | 📚 Knowledge | 🔄 **Planned** |
| A     | 4       | **Capstone Implementation Sprint 1 (Core Functionality)**                                            | 📚 Knowledge | 🔄 **Planned** |
| A     | 5 (MP1) | **🚀 Mini Project 1: Capstone MVP (End‑to‑End Happy Path Working)**                                  | 🛠️ Project   | 🔄 **Planned** |
| B     | 6       | **Docs & Developer Experience: README, API Docs & Quickstart**                                       | 📚 Knowledge | 🔄 **Planned** |
| B     | 7       | **CI/CD Basics: Automated Tests, Linting & Simple Deployment Pipeline (e.g. GitHub Actions)**        | 📚 Knowledge | 🔄 **Planned** |
| B     | 8       | **Polishing & Refactoring: Code Quality Pass, Logging/Metrics Review, Packaging for Reuse**          | 📚 Knowledge | 🔄 **Planned** |
| B     | 9       | **Storytelling & Next Steps: Writing a Portfolio Case Study & Future Learning Roadmap**              | 📚 Knowledge | 🔄 **Planned** |
| B     | 10 (MP2) | **🚀 Mini Project 2: Capstone v1.0 Release (Tagged, Documented & Showcased in Portfolio)**           | 🛠️ Project   | 🔄 **Planned** |

**Key Learning Focus:**

**Phase A (Sessions 1–4 + MP1):**

- Choose a **realistic yet manageable domain** (tracker, dashboard, small SaaS‑like tool, automation utility, etc.) with clear users and outcomes  
- Write a short **design document** that sketches architecture, data stores, key APIs, and any background jobs or messaging flows  
- Decide which earlier building blocks to include (SQL/NoSQL, Redis, RabbitMQ/Kafka, CLI vs HTTP API, etc.) and how they fit together  
- **🎯 Capstone Scope Control**: Implement **ONE primary end‑to‑end flow** first (one or two main user journeys). Everything else is optional stretch goals. **Your capstone succeeds if ONE scenario works well.**  
- **Mini Project 1: Capstone MVP** – a working slice of the final project that exercises key technologies and patterns from previous levels

**Phase B (Sessions 6–9 + MP2):**

- Create high‑quality **developer documentation**: a clear README, architecture overview, and basic API docs or usage examples  
- Configure **CI/CD basics**: run tests and linters automatically on push/PR, and optionally publish a package or Docker image to a registry  
- Do a final **refactoring and polishing pass**: tidy modules, improve naming, ensure logs/metrics are meaningful, and package/shared components are reusable  
- Write a short **portfolio case study**: problem, approach, stack, challenges, and what was learned, plus a personal roadmap for next skills  
- **Mini Project 2: Capstone v1.0 Release** – tag a release, ensure CI passes, docs are up to date, and the project is ready to be shown to others

**Mini Projects:**

- **Capstone MVP** – the first fully working version of the capstone that demonstrates an end‑to‑end flow using the learner’s chosen stack  
- **Capstone v1.0 Release & Portfolio Entry** – a polished, documented, tested, and versioned project that can be linked in a CV or profile

**Learning Outcome:** "I can design, implement, document, test, package, and ship a small but realistic Python system that I'm proud to show others, and I know how to plan my next steps as a curious professional."

**Exit Criteria:**

To complete Level 18, you should have:

- ✅ A working capstone project with **ONE primary end‑to‑end flow** that works well
- ✅ Documentation (README, architecture overview) that another developer could use to understand and run your project
- ✅ CI/CD pipeline that runs tests and linting automatically
- ✅ A portfolio case study that explains what you built, why, and what you learned

**🎯 Capstone Scope Control (Critical):**

> **Your capstone succeeds if ONE end‑to‑end scenario works well.**

**Do:**

- ✅ Focus on **one primary user journey** (e.g., "User creates a task, views it, marks it complete")
- ✅ Make that flow **polished, tested, and documented**
- ✅ Add other features as **optional stretch goals** only after the core works

**Don't:**

- ❌ Try to build every feature you can imagine
- ❌ Add complexity "just because" (violates YAGNI)
- ❌ Burn out trying to make it perfect – **done is better than perfect**

**Reflection (Level 18):**

- What one user journey did I ship end-to-end?
- What would I cut if I had half the time?
- What is in my portfolio case study headline?
- What one ADR best explains my capstone architecture?

**Remember:** A small, well‑executed project is far more impressive than a large, half‑finished one.

---

## 📊 **Overall Learning Journey Map**

| Level | From → To                                  | Core Focus                           | Key Technologies                                    | Learning Mindset                           |
| ----- | ------------------------------------------ | ------------------------------------- | --------------------------------------------------- | ------------------------------------------ |
| 1     | Noob → Nerd                                | Python Basics                        | Python, VS Code                                     | "I can code!"                              |
| 2     | Nerd → Novice                              | Functions & Files                    | Functions, Error Handling, File I/O                 | "I can solve problems!"                    |
| 3     | Novice → Object Thinker                    | Core OOP                             | Classes, Objects                                    | "I can think in objects!"                  |
| 4     | Object Thinker → Design Learner            | OOP Design & Clean Code Intro        | Classes, Methods, Basic Testing                     | "I can design simple models!"              |
| 5     | Design Learner → Data Wrangler             | Files & Data Formats                 | CSV, JSON, Serialization                            | "I can wrangle data!"                      |
| 6     | Data Wrangler → DB Beginner                | Relational Databases                 | SQLite, SQL, CRUD                                   | "I can persist data safely!"               |
| 7     | DB Beginner → Integration Novice           | NoSQL & HTTP APIs (Intro)            | JSON APIs, NoSQL Concepts                           | "I can integrate with systems!"            |
| 8     | Integration Novice → Practitioner          | Clean Code & Tooling                 | CLI, Git, Testing, Debugging                        | "I write clean, reliable code!"            |
| 9     | Practitioner → Patterned Coder             | Design Patterns & Architecture       | Core Patterns, SOLID-lite                           | "I design systems that scale!"             |
| 10    | Patterned Coder → Stdlib Specialist        | Standard Library Mastery             | os, pathlib, datetime, collections                  | "I master Python's toolbox!"               |
| 11    | Stdlib Specialist → Pro Toolsmith          | Third-Party Ecosystem                | requests, openpyxl, click, rich, pytest             | "I use professional tools well!"           |
| 12    | Pro Toolsmith → Curious Learner            | Advanced Features & Packaging        | asyncio, multiprocessing, packaging                 | "I'm a curious Python expert!"             |
| 13    | Curious Learner → Data Platform Explorer   | Production Relational Databases      | SQL Server, PostgreSQL, SQL tools / light ORM       | "I can work with real production databases!" |
| 14    | Data Platform Explorer → Data Systems Builder | Document DBs & Caching            | Mongo-style Document DB, Redis                      | "I can choose and use the right data store!" |
| 15    | Data Systems Builder → Service Integrator  | Messaging, Streaming & Deep Testing  | RabbitMQ, Kafka, pytest (unit & integration tests)  | "I can integrate and test systems end-to-end!" |
| 16    | Service Integrator → Service Builder       | End-to-End Service Foundations       | HTTP APIs, DB integration, testing                  | "I can build a small, tested service!"     |
| 17    | Service Builder → Systems Crafter          | Service Hardening & Observability    | Logging, metrics, configuration, Docker basics      | "I can run and observe my services!"       |
| 18    | Systems Crafter → Curious Professional     | Capstone Project & Next-Step Roadmap | Packaging, CI/CD, documentation, portfolio building | "I keep growing as a curious professional!" |

---

## 🎯 **Key Learning Outcomes by Level**

### **Technical Skills Progression:**

- **Level 1:** Python basics, variables, operators, conditionals, loops, lists, dictionaries  
- **Level 2:** Functions, error handling, file operations, advanced data structures  
- **Level 3:** Core Object-Oriented Programming (classes, objects, attributes, methods)  
- **Level 4:** OOP design patterns at a beginner level and clean code principles (KISS, DRY, YAGNI)  
- **Level 5:** Working with files and data formats (CSV, JSON, basic serialization)  
- **Level 6:** Relational database fundamentals (SQLite, SQL, CRUD, simple joins)  
- **Level 7:** Introductory NoSQL concepts and HTTP/JSON API integration  
- **Level 8:** Practical clean-code habits, CLI tooling, Git workflows, and testing/debugging practices  
- **Level 9:** Design patterns and architectural thinking for console applications  
- **Level 10:** Python Standard Library mastery (os, pathlib, datetime, collections, itertools, logging)  
- **Level 11:** Professional third-party libraries (requests, openpyxl, click, rich, pytest, config tools)  
- **Level 12:** Advanced Python features (generators, threading, multiprocessing, asyncio intro, packaging) — *metaclasses: appendix/stretch only, not core sessions*  
- **Level 13:** Production relational databases (SQL Server, PostgreSQL, basic ORM usage)  
- **Level 14:** Document databases and caching (Mongo-style Document DB, Redis caching patterns)  
- **Level 15:** Messaging and streaming with robust testing (RabbitMQ, Kafka, advanced unit and integration testing)  
- **Level 16:** End-to-end service design (simple HTTP API plus database and tests)  
- **Level 17:** Service hardening and observability (configuration, logging, metrics, basic Docker/deployment)  
- **Level 18:** Capstone project and portfolio (shipping a real multi-component Python project with docs and CI/CD)

### **Mindset Transformation:**

- **Confidence Building:** From "I can't code" to "I can solve complex problems"
- **Best Practices:** From "make it work" to "make it maintainable"
- **Architecture Thinking:** From scripts to scalable systems
- **Innovation Mindset:** From following tutorials to creating with AI

---

## 🏛️ **Curriculum Architecture**

Formerly titled *Implementation Strategy* — this is the **rollout architecture** for the three program stages.

### **Stage 1 — Python Fundamentals (Levels 1–6)**

| Level | Capability focus | Spiral notes |
| --- | --- | --- |
| 1–2 | Language + programming | File I/O introduced L2 S8; deepened L5 |
| 3–4 | OOP + design | Refactor L1/L2 MPs; intro unit tests L4 |
| 5–6 | Data + SQLite | CSV/JSON pipelines; SQL CRUD |

**Immediate priority:** Level 3 curriculum authoring (Coming next after L1–L2 delivery catches up).

### **Stage 2 — Professional Python Development (Levels 7–12)**

| Level | Capability focus | Spiral notes |
| --- | --- | --- |
| 7 | Integration intro | HTTP/JSON, pseudo-NoSQL documents |
| 8 | Practitioner tooling | Git, CLI, pytest concept, **optional ADRs** |
| 9–10 | Design + stdlib | Patterns on existing CLI projects; then stdlib depth |
| 11–12 | Ecosystem + advanced | `requests` (professional), packaging; concurrency intro |

### **Stage 3 — Python Systems Engineering (Levels 13–18)**

**Lab-time expectation:** Each level remains **10 × 30 min guided** sessions, plus **guided labs** (often 5–10 hours/level) and **stretch** work. Indicative lab topics:

| Level | Guided labs (indicative) |
| --- | --- |
| 13 | Postgres/SQL Server setup, SQLite port, SQLAlchemy |
| 14 | Document DB feature, Redis cache patterns |
| 15 | RabbitMQ worker (+ optional Kafka stretch) |
| 16 | HTTP service + DB integration tests |
| 17 | Dockerfile, Compose stack, health/metrics |
| 18 | Capstone MVP → v1.0 release + portfolio case study |

**Portfolio checkpoints:** After Levels 8, 12, and 18 — learners should have a **clone-and-run** project suitable for CV/portfolio links.

### **Post-program — Specialization (optional)**

- Web backend, data engineering, DevOps/SRE, ML — chosen after L18 capstone
- Open-source contribution with ADR-aware README and tests
- Continued learning on domain-specific frameworks

---

## 📞 **About This Master Plan**

### **Powered by ShyvnTech & Swamy's Tech Skills Academy**

This master plan is the **authoritative roadmap** for the Python Software Engineering Journey — from absolute beginner to AI-aware, portfolio-ready professional. Each level builds on the previous; **three status axes**, **spiral labels**, and **realistic time bands** keep ambition high without misleading learners on workload.

**Start here:** [Level 1 plan](sessions/L1/_Plan.md) · [Session 1](sessions/L1/S1.md) · [Meetup status](meetup/L1/sessions.md)

Happy Coding! 🐍✨
