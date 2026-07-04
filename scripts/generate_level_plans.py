#!/usr/bin/env python3
"""Generate aligned docs/sessions/L{3..18}/_Plan.md from master-plan metadata."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "sessions"

STAGES = {
    range(1, 7): "Part 1 — Python Fundamentals",
    range(7, 13): "Part 2 — Professional Python Development",
    range(13, 19): "Part 3 — Python Systems Engineering",
}


def stage_part(level: int) -> str:
    for levels, part in STAGES.items():
        if level in levels:
            return part
    raise ValueError(level)


def meetup_link(level: int) -> str | None:
    path = ROOT / "docs" / "meetup" / f"L{level}" / "sessions.md"
    return f"../../meetup/L{level}/sessions.md" if path.exists() else None


def delivery_status(level: int) -> str:
    link = meetup_link(level)
    if link:
        return f"All sessions pending ([meetup table]({link}))"
    return "Not started (meetup schedule TBD)"


def repository_status(level: int) -> str:
    if level <= 2:
        return "Implemented"
    if level == 3:
        return "Scaffolded — `_Plan.md` only; session docs and `src/L3/` pending"
    return "Planned — `_Plan.md` scaffold; session docs and practice code pending"


def curriculum_status(level: int) -> str:
    return "Draft"


def duration(level: int) -> str:
    if level == 13:
        return "~5 hours core guided instruction + ~6–10 h guided labs (setup, ORM, migrations)"
    if level in (1, 2):
        return "~5–6 hours core guided instruction (+ MPs)"
    return "~5 hours core guided instruction (+ MPs)"


def session_yaml(level: int, sessions: list[tuple[str | int, str]]) -> str:
    lines: list[str] = []
    for num, topic in sessions:
        num_str = str(num)
        mp = "(MP" in num_str
        file_num = num_str.split()[0]
        session_key = f'"{num}"' if mp or " " in num_str else num_str
        lines.append(f"  - session: {session_key}")
        lines.append(f'    topic: "{topic}"')
        lines.append('    duration: "30–45 min"' if mp else '    duration: "30 min"')
        lines.append('    type: "Project"' if mp else '    type: "Knowledge"')
        lines.append('    curriculum: "Draft"')
        lines.append('    delivery: "Pending"')
        lines.append(f'    file: "docs/sessions/L{level}/S{file_num}.md"')
    return "\n".join(lines)


def bullet_block(items: list[str], indent: int = 0) -> str:
    pad = " " * indent
    return "\n".join(f"{pad}* {item}" for item in items)


def render_level(data: dict) -> str:
    level: int = data["level"]
    from_to: str = data["from_to"]
    title: str = data["title"]
    tagline: str = data["tagline"]
    transform: str = data["transform"]
    outcome: str = data["outcome"]
    objectives: list[str] = data["objectives"]
    sessions: list[tuple[str | int, str]] = data["sessions"]
    phase_a_name: str = data["phase_a_name"]
    phase_b_name: str = data["phase_b_name"]
    phase_a_sessions: list[dict] = data["phase_a_sessions"]
    phase_b_sessions: list[dict] = data["phase_b_sessions"]
    exit_criteria: list[str] = data.get("exit_criteria", [])
    anti_patterns: list[str] = data.get("anti_patterns", [])
    reflection: list[str] = data.get("reflection", [])
    bridge: str | None = data.get("bridge")
    extra_sections: str = data.get("extra_sections", "")
    learning_outcome: str = data.get("learning_outcome", "")
    assessment: list[str] = data.get("assessment", [])
    next_steps: list[str] = data.get("next_steps", [])
    mp1: dict = data["mp1"]
    mp2: dict = data["mp2"]

    prev = f"docs/sessions/L{level - 1}/_Plan.md"
    nxt = (
        f"docs/sessions/L{level + 1}/_Plan.md"
        if level < 18
        else "docs/01_Python-Fundamentals-MasterPlan.md"
    )

    cross_refs = [
        "docs/01_Python-Fundamentals-MasterPlan.md",
    ]
    if meetup_link(level):
        cross_refs.append(f"docs/meetup/L{level}/sessions.md")

    yaml_cross = "\n".join(f'    - "{r}"' for r in cross_refs)
    yaml_obj = "\n".join(f'  - "{o}"' for o in objectives)

    session_rows = []
    for num, topic in sessions:
        mp = isinstance(num, str)
        phase = "A" if (isinstance(num, int) and num <= 5) or (mp and "MP 1" in str(num)) else "B"
        if isinstance(num, int) and num <= 4:
            phase = "A"
        elif isinstance(num, str) and "MP 1" in num:
            phase = "A"
        elif isinstance(num, int) and num >= 6:
            phase = "B"
        elif isinstance(num, str) and "MP 2" in num:
            phase = "B"
        dur = "30–45 min" if mp else "30 min"
        typ = "🛠️ Project" if mp else "📚 Knowledge"
        after = ""
        if isinstance(num, str) and "MP 1" in num:
            after = " *(after Session 4)*"
        if isinstance(num, str) and "MP 2" in num:
            after = " *(after Session 9)*"
        session_rows.append(
            f"| {phase} | {num} | {topic}{after} | {dur} | {typ} | Draft | Pending |"
        )

    def session_section(s: dict, mp: bool = False) -> str:
        icon = "🚀" if mp else "✅"
        kind = "Mini Project" if mp else "Session"
        num = s["num"]
        name = s["title"]
        body = bullet_block(s.get("bullets", []))
        feeds = s.get("feeds", "")
        feeds_line = f"\n\n📌 *{feeds}*" if feeds else ""
        doc = s.get("doc", f"docs/sessions/L{level}/S{num}.md")
        practice = s.get("practice", f"`src/L{level}/S{num}/` — planned")
        return f"""### {icon} {kind} {num}: {name} *(Draft · delivery: Pending)*

{body}

🧪 *Practice / deliverable*: {practice}  
📖 *Documentation*: planned [{doc.split('/')[-1]}]({doc.split('/')[-1]}){feeds_line}

---"""

    phase_a_body = "\n\n".join(
        session_section(s, mp=isinstance(s["num"], str) and "MP" in str(s["num"]))
        for s in phase_a_sessions
    )
    phase_b_body = "\n\n".join(
        session_section(s, mp=isinstance(s["num"], str) and "MP" in str(s["num"]))
        for s in phase_b_sessions
    )

    exit_block = ""
    if exit_criteria:
        exit_block = "### Exit criteria (before next level)\n\n" + bullet_block(exit_criteria) + "\n\n"

    anti_block = ""
    if anti_patterns:
        anti_block = "### Common anti-patterns (Level " + str(level) + ")\n\n" + bullet_block(anti_patterns) + "\n\n"

    refl_block = "### Reflection (Level " + str(level) + ")\n\n" + bullet_block(reflection) + "\n\n"

    bridge_block = f"📌 *Bridge:* {bridge}\n\n" if bridge else ""

    assessment_block = ""
    if assessment:
        assessment_block = "## 📊 **Assessment Criteria**\n\n" + bullet_block(assessment) + "\n\n---\n\n"

    next_block = ""
    if next_steps:
        next_block = "## 🎓 **Next Steps & Resources**\n\n" + bullet_block(next_steps) + "\n\n"

    mermaid_mp1 = mp1["short"]
    mermaid_mp2 = mp2["short"]

    extra_sections: str = data.get("extra_sections", "")

    plain_delivery_yaml = (
        f"All sessions pending (see docs/meetup/L{level}/sessions.md)"
        if meetup_link(level)
        else "Not started (meetup schedule TBD)"
    )
    plain_delivery_table = (
        f"All sessions pending ([meetup table](../../meetup/L{level}/sessions.md))"
        if meetup_link(level)
        else "Not started (meetup schedule TBD)"
    )

    return f"""---
learning_level: "{from_to}"
level_number: {level}
stage_part: "{stage_part(level)}"
prerequisites:
  - "{prev}"
total_duration: "{duration(level)}"
format: "2 phases × (4 sessions + 1 mini project) = 10 sessions total"
outcome: "{outcome}"
transformation_focus: "{transform}"
curriculum_status: "{curriculum_status(level)}"
delivery_status: "{plain_delivery_yaml}"
repository_status: "{repository_status(level)}"
master_plan: "docs/01_Python-Fundamentals-MasterPlan.md"
learning_objectives:
{yaml_obj}
related_topics:
  prerequisites:
    - "{prev}"
  builds_upon:
    - "{prev}"
  enables:
    - "{nxt}"
  cross_refs:
{yaml_cross}
sessions:
{session_yaml(level, sessions)}
---

# {title}

## {tagline}

> **Stage:** {stage_part(level)} (Levels {"1–6" if level <= 6 else "7–12" if level <= 12 else "13–18"}) · **Program:** [Python Software Engineering Journey](../../01_Python-Fundamentals-MasterPlan.md)
>
> 1. **Level:** {from_to}
> 1. **Format:** 2 phases × (4 sessions + 1 mini project) = 10 sessions total
> 1. **Outcome:** {outcome}
> 1. **Core guided time:** {duration(level)}

## Powered by ShyvnTech & Swamy's Tech Skills Academy

> **Transformation Focus:** {transform}

### Level {level} status (three axes)

| Axis | Status |
| --- | --- |
| **Curriculum** | Draft — level plan aligned to master plan; session docs pending |
| **Delivery** | {plain_delivery_table} |
| **Repository** | {repository_status(level)} |

{bridge_block}---

## 🎯 **Level {level} Learning Path ({from_to.split(' → ')[0]} → {from_to.split(' → ')[1]})**

| Phase | Session | Topic | Duration | Type | Curriculum | Delivery |
| ----- | ------- | ----- | -------- | ---- | ---------- | -------- |
{chr(10).join(session_rows)}

---

## 🗺️ **Visual Roadmap**

```mermaid
flowchart TB
  A["🎯 {from_to.split(' → ')[0]}"] --> PhaseA
  PhaseA --> PhaseB
  PhaseB --> K["🎓 {from_to.split(' → ')[1]}"]

  subgraph PhaseA["📘 {phase_a_name}"]
    B1["Session 1"]
    B2["Session 2"]
    B3["Session 3"]
    B4["Session 4"]
    B5["Session 5 (MP 1)<br>{mermaid_mp1}"]
    B1 --> B2 --> B3 --> B4 --> B5
  end

  subgraph PhaseB["📘 {phase_b_name}"]
    C1["Session 6"]
    C2["Session 7"]
    C3["Session 8"]
    C4["Session 9"]
    C5["Session 10 (MP 2)<br>{mermaid_mp2}"]
    C1 --> C2 --> C3 --> C4 --> C5
  end

  classDef startEnd fill:#eef6ff,stroke:#86a9cf,stroke-width:2px,color:#1f2a37
  classDef session fill:#f5faff,stroke:#a8bfdc,stroke-width:2px,color:#1f2a37
  classDef project fill:#ddeeff,stroke:#6f90bd,stroke-width:2px,color:#1f2a37

  class A,K startEnd
  class B1,B2,B3,B4,C1,C2,C3,C4 session
  class B5,C5 project
```

---

## 📅 **Phase A: {phase_a_name}**

{phase_a_body}

## 📅 **Phase B: {phase_b_name}**

{phase_b_body}

## 🎓 **Level {level} Learning Outcomes**

{learning_outcome}

{exit_block}{anti_block}{refl_block}{extra_sections}---

{assessment_block}{next_block}✨ Happy Coding! 🐍
"""


# --- Level definitions (topics from master plan) ---

LEVELS: list[dict] = []

def add(level_data: dict) -> None:
    LEVELS.append(level_data)


DEFAULT_REFLECTION = [
    "What surprised me at this level?",
    "What was hardest — and what habit will I keep?",
    "What would I redesign in my mini project?",
    "What could I explain to a peer in five minutes?",
]

REFLECTION_ADR = DEFAULT_REFLECTION + ["What one ADR would I write for MP1 or MP2?"]

add({
    "level": 3,
    "from_to": "Novice → Object Thinker",
    "title": "🔢 Level 3: Novice → Object Thinker — Core OOP Fundamentals",
    "tagline": "From reusable scripts to small, well-modeled objects",
    "transform": "Introduce object-oriented thinking in a practical way — model real problems with small classes whose data and behavior belong together.",
    "outcome": "2 Mini Projects to shift from script thinking to object thinking",
    "objectives": [
        "Understand when classes help more than plain scripts or dictionaries",
        "Define classes and create objects with confidence",
        "Initialize and manage object state with __init__ and instance attributes",
        "Write instance methods that act on object state",
        "Model simple has-a relationships between objects",
        "Store and work with collections of objects",
        "Use __str__ and __repr__ to make objects easier to inspect",
        "Refactor an existing script into a small class-based design",
        "Complete 2 mini projects demonstrating beginner-friendly OOP design",
        "Be ready for Level 4: Object Thinker → Design Learner",
    ],
    "sessions": [
        (1, "Why OOP? From Scripts to Objects"),
        (2, "Defining Classes & Creating Objects"),
        (3, "`__init__`, Attributes & Basic Encapsulation"),
        (4, "Instance Methods & Working with Object State"),
        ("5 (MP 1)", "Mini Project 1: Object-Based Profile Manager"),
        (6, "Composing Multiple Objects (Has-a Relationships)"),
        (7, "Collections of Objects (Lists of Objects)"),
        (8, "User-Friendly Objects with `__str__` / `__repr__`"),
        (9, "Refactoring Scripts into Classes (OOP in Practice)"),
        ("10 (MP 2)", "Mini Project 2: Object-Oriented Task / Inventory App"),
    ],
    "phase_a_name": "Phase A: OOP Foundations",
    "phase_b_name": "Phase B: OOP in Practice",
    "mp1": {"short": "Profile Manager"},
    "mp2": {"short": "Task / Inventory App"},
    "bridge": "Refactor **L1 Profile Generator** and **L2 Contact Manager** from dict/file scripts into collaborating classes (MP1 target).",
    "learning_outcome": bullet_block([
        "Explain why a small class-based model can be clearer than a dictionary-only script",
        "Create objects, inspect attributes, and call methods without confusion",
        "Refactor a small script into 2–3 collaborating classes",
        "Use `__str__` to make objects print in a human-readable form",
        "Say: *I can model a small problem with classes and keep state and behavior together.*",
    ]),
    "exit_criteria": [
        "Refactor a dictionary-based script (e.g., contact manager) into 2–3 collaborating classes",
        "Explain why a specific attribute belongs on one class and not another",
        "Create objects, call their methods, and access attributes without errors",
        "Use `__str__` to make objects print in a human-readable format",
    ],
    "anti_patterns": [
        "**God Object** — one class stores everything and does everything",
        "**Anemic Model** — classes hold data but all behavior lives elsewhere",
        "**Premature Inheritance** — inheritance before composition and plain classes are understood",
        "**Classes for Everything** — simple logic forced into classes when state is unnecessary",
    ],
    "reflection": [
        "When did a class feel clearer than a dictionary for the same data?",
        "What attribute placement decision was hardest?",
        "How would you explain `__init__` to a peer using your MP1 project?",
    ],
    "phase_a_sessions": [
        {"num": 1, "title": "Why OOP? From Scripts to Objects", "bullets": [
            "Why data and behavior together can simplify some problems",
            "Script vs dictionary vs simple class mental models",
            "When OOP helps and when a plain function is enough",
        ], "feeds": "Feeds into MP1: choosing real-world things to model as objects"},
        {"num": 2, "title": "Defining Classes & Creating Objects", "bullets": [
            "Basic `class` syntax and creating instances",
            "Difference between a class and an object",
        ]},
        {"num": 3, "title": "__init__, Attributes & Basic Encapsulation", "bullets": [
            "Using `__init__` to set up object state",
            "Meaningful instance attributes and intro-level encapsulation",
        ]},
        {"num": 4, "title": "Instance Methods & Working with Object State", "bullets": [
            "Methods with `self`; reading and updating state through methods",
            "Avoiding global data everywhere",
        ]},
        {"num": "5 (MP 1)", "title": "Object-Based Profile Manager", "bullets": [
            "Create profile objects with named attributes and methods",
            "Store multiple profile objects in a list",
            "Refactor L1/L2 profile/contact ideas into classes",
        ], "practice": "`src/L3/S5/` — planned", "feeds": "Bridge from L1 Profile Generator and L2 Contact Manager"},
    ],
    "phase_b_sessions": [
        {"num": 6, "title": "Composing Multiple Objects (Has-a Relationships)", "bullets": [
            "Composition examples: Profile has GoalList; TaskBoard has Tasks",
            "What belongs inside another object vs stays separate",
        ]},
        {"num": 7, "title": "Collections of Objects", "bullets": [
            "Lists of objects; loop, filter, and update collections",
        ]},
        {"num": 8, "title": "User-Friendly Objects with __str__ / __repr__", "bullets": [
            "Readable `__str__`; lightweight `__repr__` for debugging",
        ]},
        {"num": 9, "title": "Refactoring Scripts into Classes", "bullets": [
            "Move grouped state and functions into a class design",
            "Stop before over-designing",
        ]},
        {"num": "10 (MP 2)", "title": "Object-Oriented Task / Inventory App", "bullets": [
            "Model tasks or inventory items as objects with methods",
            "Add, update, display, and remove entries via object behavior",
        ], "practice": "`src/L3/S10/` — planned"},
    ],
    "assessment": [
        "**Phase A:** Can explain when classes help, define classes, and build MP1 profile manager",
        "**Phase B:** Can compose objects, refactor scripts, and complete MP2 task/inventory app",
    ],
    "next_steps": [
        "OOP design and clean code (Level 4)",
        "Unit tests for classes (Level 4)",
        "Refactoring habits and code review (Level 4)",
    ],
})

# Continue with L4-L18 in same file - I'll append programmatically for brevity in script

def simple_sessions(topics: list[str]) -> list[tuple[int | str, str]]:
    base = [
        (1, topics[0]), (2, topics[1]), (3, topics[2]), (4, topics[3]),
        ("5 (MP 1)", topics[4]), (6, topics[5]), (7, topics[6]), (8, topics[7]),
        (9, topics[8]), ("10 (MP 2)", topics[9]),
    ]
    return base


def phase_sessions(level: int, topics: list[str], mp1_bullets: list[str], mp2_bullets: list[str]) -> tuple[list[dict], list[dict]]:
    a = []
    b = []
    for i, t in enumerate(topics[:4], start=1):
        a.append({"num": i, "title": t, "bullets": [f"Core concepts for {t} (see master plan)."]})
    a.append({"num": "5 (MP 1)", "title": topics[4].replace("Mini Project 1: ", ""), "bullets": mp1_bullets, "practice": f"`src/L{level}/S5/` — planned"})
    for i, t in enumerate(topics[5:9], start=6):
        b.append({"num": i, "title": t, "bullets": [f"Core concepts for {t} (see master plan)."]})
    b.append({"num": "10 (MP 2)", "title": topics[9].replace("Mini Project 2: ", ""), "bullets": mp2_bullets, "practice": f"`src/L{level}/S10/` — planned"})
    return a, b


LEVEL_SPECS = [
    (4, "Object Thinker → Design Learner", "🏗️ Level 4: Object Thinker → Design Learner — OOP Design & Clean Code Intro",
     "Turn basic OOP into good small designs and clean-code thinking",
     "2 Mini Projects applying design, refactoring, and first unit tests",
     "Move from working classes to intentional design, refactoring, and testable OOP.",
     "Phase A: From Requirements to Refactoring", "Phase B: Clean Code & Tested OOP",
     {"short": "Refactor to Classes"}, {"short": "Clean OOP App"},
     simple_sessions([
         "From Requirements to Classes (Thinking in Models)",
         "Designing Responsibilities & Avoiding God Classes",
         "Improving Class Interfaces (KISS for Methods & Classes)",
         "Intro to Refactoring: Making Existing Code Cleaner",
         "Mini Project 1: Refactor a Script into a Class Design",
         "Clean Code Principles: KISS, DRY, YAGNI (Applied)",
         "Reading & Reviewing Code: Finding Smells in OOP Code",
         "Intro Unit Tests for Classes (Arrange–Act–Assert)",
         "Organizing a Small OOP Project (Modules & Packages)",
         "Mini Project 2: Clean, Tested OOP Console Application",
     ]),
     ["Identify a code smell and refactor it", "Write a simple unit test for a class method", "Explain and split a God Object", "Apply KISS, DRY, or YAGNI to real code"],
     ["**Over-Engineering** — patterns before you feel the pain", "**Copy-Paste Refactoring** — duplication instead of shared logic", "**Premature Abstraction** — base classes just in case", "**If-Else Hell** — long chains that need clearer structure"],
     DEFAULT_REFLECTION,
     "Refactor a Level 2/3 script (data processor or profile manager) in MP1.",
     ["**Phase A:** Requirements → classes → MP1 refactor", "**Phase B:** Clean code, tests, modules → MP2 console app"],
     ["Files and data formats (Level 5)", "CSV/JSON pipelines (Level 5)"]),
    (5, "Design Learner → Data Wrangler", "📂 Level 5: Design Learner → Data Wrangler — Files & Data Formats",
     "Become fluent with real-world files and data formats",
     "2 Mini Projects for CSV/JSON cleaning and file-based reporting",
     "Read, clean, transform, and write text, CSV, and JSON data confidently.",
     "Phase A: File I/O & Structured Formats", "Phase B: Pipelines & File-Based Apps",
     {"short": "Data Cleaner"}, {"short": "Data Dashboard"},
     simple_sessions([
         "Reviewing File I/O: Text vs Binary, Paths, Encodings",
         "CSV Basics: Reading & Writing Tabular Data",
         "JSON Basics: Nested Structures & Config-Style Data",
         "From Raw Text to Structured Data (Parsing & Cleaning)",
         "Mini Project 1: CSV/JSON Data Cleaner & Reporter",
         "Building Simple Data Pipelines (Read → Transform → Write)",
         "Basic Serialization & Settings Files (Configs & States)",
         "Robust File Handling: Errors, Missing Data & Validation",
         "End-to-End File-Based Mini App (Putting It All Together)",
         "Mini Project 2: File-Based Data Dashboard / Reporter",
     ]),
     ["Read CSV, filter rows, write results", "Parse nested JSON and extract fields", "Handle missing or malformed data gracefully", "Explain when to use CSV vs JSON"],
     [],
     DEFAULT_REFLECTION,
     "Deepen file I/O from L2 S8; build on clean structure habits from L4.",
     ["**Phase A:** CSV/JSON foundations → MP1 cleaner", "**Phase B:** Pipelines and validation → MP2 dashboard"],
     ["Relational databases with SQLite (Level 6)"]),
    (6, "Data Wrangler → DB Beginner", "🗃️ Level 6: Data Wrangler → DB Beginner — Relational Databases with SQLite",
     "Build a relational database foundation and connect it to Python",
     "2 Mini Projects for SQL CLI and SQLite-backed record management",
     "Design simple schemas, write SQL, and connect Python to SQLite reliably.",
     "Phase A: Relational Concepts & SQL", "Phase B: Python + SQLite Integration",
     {"short": "SQLite CLI"}, {"short": "Record Manager"},
     simple_sessions([
         "Why Databases? From Files to Tables",
         "Tables, Rows & Keys: Designing a Simple Schema",
         "SQL Basics: SELECT, INSERT, UPDATE, DELETE",
         "Filtering & Ordering Data (WHERE, ORDER BY, LIMIT)",
         "Mini Project 1: CLI over a Single-Table SQLite DB",
         "Connecting Python to SQLite (sqlite3 Fundamentals)",
         "Parameterized Queries & Avoiding SQL Injection",
         "Simple Joins & Multi-Table Designs (Intro Only)",
         "Migrating a File-Based App to SQLite (End-to-End)",
         "Mini Project 2: SQLite-Backed Record Manager",
     ]),
     ["Design a schema with 2–3 related tables", "Write INSERT, SELECT, UPDATE, DELETE queries", "Use parameterized queries", "Explain database vs JSON/CSV trade-offs"],
     [],
     DEFAULT_REFLECTION,
     "Migrate a Level 5 file-based app to SQLite in later sessions.",
     ["**Phase A:** SQL fundamentals → MP1 single-table CLI", "**Phase B:** sqlite3 + migration → MP2 record manager"],
     ["NoSQL concepts and HTTP/JSON APIs (Level 7)"]),
    (7, "DB Beginner → Integration Novice", "🌐 Level 7: DB Beginner → Integration Novice — NoSQL & HTTP/JSON APIs",
     "Introduce document-style data and HTTP/JSON API integration",
     "2 Mini Projects for JSON document store and API-powered cached app",
     "Integrate external JSON APIs with local storage and document-style thinking.",
     "Phase A: Document-Style Data", "Phase B: HTTP APIs & Caching",
     {"short": "JSON Notes Store"}, {"short": "API Cached App"},
     simple_sessions([
         "From Tables to Documents: NoSQL Concepts with JSON",
         "Using JSON Files as a Simple Document Store",
         "Modeling Data in Documents (Keys, Collections, Nested Data)",
         "Query-Like Operations over In-Memory / File-Based Docs",
         "Mini Project 1: JSON-Backed NoSQL Notes / Profile Store",
         "HTTP & REST Basics: Requests, Responses, Status Codes",
         "Consuming JSON APIs with requests (GET + Query Params)",
         "Handling API Errors, Timeouts & Basic Response Validation",
         "Combining APIs with Local Storage (Caching Remote Data)",
         "Mini Project 2: API-Powered App with Local JSON Cache",
     ]),
     ["Explain when JSON documents beat relational tables", "Cache API data locally and discuss invalidation", "Handle API errors gracefully", "Make a GET request and parse JSON"],
     [],
     DEFAULT_REFLECTION,
     "Prepares for practitioner tooling spiral in Level 8.",
     ["**Phase A:** Document modeling → MP1 JSON store", "**Phase B:** HTTP + cache → MP2 API app"],
     ["Clean code, Git, CLI tooling, and testing (Level 8)"]),
    (8, "Integration Novice → Practitioner", "🧹 Level 8: Integration Novice → Practitioner — Clean Code & Tooling",
     "Become a working practitioner with clean code, CLI, Git, and tests",
     "2 Mini Projects: CLI wrapper and polished portfolio-ready CLI tool",
     "Structure, test, version-control, and polish small Python projects like real tools.",
     "Phase A: Clean Code & CLI Foundations", "Phase B: Testing, AI Pairing & Polish",
     {"short": "CLI Wrapper"}, {"short": "Polished CLI Tool"},
     simple_sessions([
         "Practical KISS/DRY/YAGNI on Real Code",
         "Building User-Friendly CLIs (argparse / click Intro)",
         "Structuring Projects: Folders, Modules, and Entry Points",
         "Git Basics: Commits, Branches, and Clean Histories",
         "Mini Project 1: CLI Wrapper Around an Existing Project",
         "Everyday Testing with pytest / unittest (No TDD Dogma)",
         "AI as Pair Programmer: Prompting for Refactoring & Code Review",
         "Formatting & Linting (black, isort, flake8 – Concept Intro)",
         "Polishing a Small Project: From Script to Mini Product",
         "Mini Project 2: Polished, Tested CLI Tool in Git Repo",
     ]),
     ["Create a Git repo with meaningful commits", "Write at least 3 pytest tests for real code", "Use AI suggestions critically and verify output", "Run black and flake8 and fix issues"],
     ["**Blind AI Trust** — using AI code without understanding", "**No Version Control** — skipping Git on small projects", "**Tests That Don't Test** — tests that always pass", "**Over-Configuration** — hours tuning tools instead of shipping"],
     REFLECTION_ADR,
     "**Portfolio checkpoint:** MP2 should be a clone-and-run CLI in a Git repo. Spiral reinforcement of pytest/Git/formatting after L4/L7.",
     ["**Phase A:** CLI + Git → MP1 wrapper", "**Phase B:** Tests + polish → MP2 portfolio CLI"],
     ["Design patterns and architecture (Level 9)"],
     """### AI usage guidelines (Level 8)

* ✅ **Use AI for:** explaining code, generating test cases, refactor suggestions, finding bugs
* ✅ **Always:** review AI output critically and verify with tests or examples
* ❌ **Don't:** copy-paste AI code without understanding or skip manual practice

"""),
    (9, "Practitioner → Patterned Coder", "🏛️ Level 9: Practitioner → Patterned Coder — Design Patterns & Architecture",
     "Learn practical design patterns and architectural habits",
     "2 Mini Projects applying patterns and layered console design",
     "Apply a small set of patterns and layering where they improve clarity and extension.",
     "Phase A: Core Patterns Intro", "Phase B: Layering & SOLID-Lite",
     {"short": "Pattern Refactor"}, {"short": "Patterned Console App"},
     simple_sessions([
         "Why Patterns? When & When Not to Use Them",
         "Strategy Pattern: Swappable Behaviours Without if Everywhere",
         "Factory / Creator Functions: Centralizing Object Creation",
         "Observer / Pub-Sub (Intro to Event-Driven Thinking)",
         "Mini Project 1: Refactor to Use One Core Pattern",
         "Separation of Concerns & Layering (UI / Logic / Data)",
         "Decorator vs Inheritance: Extending Behaviour Safely",
         "SOLID-Lite: SRP & Open/Closed in Small Python Projects",
         "Putting It Together: A Patterned, Layered Console Application",
         "Mini Project 2: Patterned Console App / Plugin-Style Tool",
     ]),
     ["Refactor using Strategy, Factory, or Observer where it helps", "Explain when a pattern helps vs adds complexity", "Separate UI from business logic", "Explain the system to a new teammate in 3 minutes"],
     ["**Pattern Overload** — patterns everywhere just because", "**Premature Abstraction** — interfaces before concrete implementations", "**Anemic Domain Model** — logic only in services", "**Tight Coupling** — concrete dependencies everywhere"],
     REFLECTION_ADR,
     None,
     ["**Phase A:** Strategy/Factory/Observer → MP1 refactor", "**Phase B:** Layering + SOLID-lite → MP2 patterned app"],
     ["Standard library mastery (Level 10)"],
     """### Architecture narrative (Level 9+)

Practice explaining your design:

* Why does each component exist?
* What breaks if we remove it?
* Can you explain the system to a new teammate in 3 minutes?

"""),
    (10, "Patterned Coder → Stdlib Specialist", "🧰 Level 10: Patterned Coder → Stdlib Specialist — Standard Library Mastery",
     "Master core Python stdlib modules for everyday problems",
     "2 Mini Projects powered by stdlib file, datetime, collections, logging, and regex tools",
     "Reach for built-in modules before reinventing common solutions.",
     "Phase A: Filesystem, Time & Collections", "Phase B: System, Subprocess & Logging",
     {"short": "Stdlib Utility"}, {"short": "System / Log Toolkit"},
     simple_sessions([
         "Filesystem Essentials with os and pathlib",
         "Dates & Times with datetime and time",
         "Smart Collections: collections (Counter, defaultdict, etc.)",
         "Efficient Iteration with itertools",
         "Mini Project 1: File & Data Utility Powered by Stdlib",
         "System & Environment Info with sys and platform",
         "Running Other Programs Safely with subprocess",
         "Structured Logging with logging",
         "Text & Pattern Matching with re (Regex Intro)",
         "Mini Project 2: Stdlib-Powered System / Log Toolkit",
     ]),
     ["Use pathlib cross-platform", "Use datetime for parse/format/arithmetic", "Use Counter or defaultdict to simplify processing", "Explain stdlib vs custom code trade-offs"],
     [],
     REFLECTION_ADR,
     None,
     ["**Phase A:** os/pathlib/datetime/collections → MP1 utility", "**Phase B:** subprocess/logging/re → MP2 toolkit"],
     ["Third-party ecosystem (Level 11)"]),
    (11, "Stdlib Specialist → Pro Toolsmith", "🔌 Level 11: Stdlib Specialist → Pro Toolsmith — Third-Party Ecosystem",
     "Use curated third-party libraries like a professional Python developer",
     "2 Mini Projects: API-to-Excel CLI and fully tooled CLI app",
     "Integrate requests, openpyxl, click, rich, pytest, and config tools in clean repos.",
     "Phase A: Dependencies & Data Tools", "Phase B: CLI UX & Quality Tooling",
     {"short": "API-to-Excel CLI"}, {"short": "Tooled CLI App"},
     simple_sessions([
         "Third-Party Libraries 101: pip, venvs & Choosing Dependencies",
         "HTTP & JSON APIs with requests (GET + Params + JSON)",
         "Working with Excel & Tabular Data using openpyxl",
         "Configuration & Secrets: .env, configparser, Basic Validation",
         "Mini Project 1: API-to-Excel Reporter CLI",
         "Building Polished CLIs with click",
         "Better Terminal UX with rich and Progress with tqdm",
         "Everyday Testing with pytest (Basics & Parametrized Tests)",
         "Formatting & Linting in Practice (black, isort, flake8 Intro)",
         "Mini Project 2: Fully Tooled CLI App in a Clean Repo",
     ]),
     ["Call a JSON API with requests and handle errors", "Write 3+ pytest tests with parametrization or fixtures", "Build a click CLI with commands and options", "Explain third-party vs stdlib choices"],
     [],
     REFLECTION_ADR,
     None,
     ["**Phase A:** requests/openpyxl/config → MP1 reporter", "**Phase B:** click/rich/pytest → MP2 portfolio CLI"],
     ["Advanced features and packaging capstone (Level 12)"]),
    (12, "Pro Toolsmith → Curious Learner", "🚀 Level 12: Pro Toolsmith → Curious Learner — Advanced Features & Packaging",
     "Explore advanced Python features and packaging; Stage 2 capstone",
     "2 Mini Projects: concurrent/async mini tool and installable capstone package",
     "Understand when advanced features help and how to package and share your work.",
     "Phase A: Generators & Concurrency Intro", "Phase B: Performance & Packaging",
     {"short": "Concurrent Fetcher"}, {"short": "Installable Package"},
     simple_sessions([
         "When to Reach for Advanced Features (Trade-offs & Pitfalls)",
         "Generators, Iterators & Lazy Evaluation (Beyond for Loops)",
         "Concurrency Basics: threading vs multiprocessing",
         "Asyncio Intro: async/await and Event Loops (Conceptual)",
         "Mini Project 1: Simple Concurrent / Async Fetcher or Worker",
         "Measuring Performance with timeit and cProfile",
         "Practical Optimization: Hot Spots, Caching & Small Refactors",
         "Packaging & Distribution: pyproject.toml, Wheels & venv Basics",
         "Sharing Your Work: Publishing, Docs, and Next-Step Roadmaps",
         "Mini Project 2: Installable Capstone Package / CLI Tool",
     ]),
     ["Explain generators vs regular functions", "Explain threading vs multiprocessing conceptually", "Create a simple installable package with pyproject.toml", "Measure performance with timeit and find a bottleneck"],
     [],
     REFLECTION_ADR,
     "**Stage 2 portfolio checkpoint:** MP2 installable package showcases Levels 1–12 skills.",
     ["**Phase A:** generators/concurrency → MP1 worker", "**Phase B:** packaging → MP2 installable tool"],
     ["Production relational databases (Level 13)"]),
    (13, "Curious Learner → Data Platform Explorer", "🗄️ Level 13: Curious Learner → Data Platform Explorer — Production Relational Databases",
     "Connect Python to production-grade relational databases",
     "2 Mini Projects: SQLite port and reusable data access layer",
     "Work with PostgreSQL/SQL Server, SQLAlchemy, migrations, and a reusable DAL.",
     "Phase A: Production RDBMS Foundations", "Phase B: ORM, Migrations & DAL",
     {"short": "SQLite Port"}, {"short": "Data Layer Module"},
     simple_sessions([
         "SQL Server & PostgreSQL Overview: Architecture, Tools & Local Setup",
         "Connecting from Python: Drivers, Connection Strings & Parameterized Queries",
         "Schemas, Keys & Constraints in Production Databases",
         "Indexes & Query Performance 101 (Execution Plans at a Glance)",
         "Mini Project 1: Port a SQLite App to PostgreSQL or SQL Server",
         "Working with SQLAlchemy (Core + Simple ORM Models)",
         "Environments & Migrations: Dev/Test/Prod, Alembic-Style Migration Basics",
         "Multi-Database Support & Vendor Differences",
         "Designing a Reusable Data Access Layer for a Small App",
         "Mini Project 2: Production-Style Data Layer Library / Module",
     ]),
     [],
     [],
     REFLECTION_ADR,
     "Port Level 6 SQLite apps; stretch: full migration automation optional.",
     ["**Phase A:** production DB setup → MP1 port", "**Phase B:** SQLAlchemy + DAL → MP2 module"],
     ["Document databases and caching (Level 14)"]),
    (14, "Data Platform Explorer → Data Systems Builder", "🧱 Level 14: Data Platform Explorer → Data Systems Builder — Document DBs & Caching",
     "Model data for document databases and integrate Redis caching",
     "2 Mini Projects: document-backed feature and hybrid data stack demo",
     "Choose the right store for the job: RDBMS, document DB, and Redis together.",
     "Phase A: Document Databases", "Phase B: Redis & Hybrid Stacks",
     {"short": "Document Feature"}, {"short": "Hybrid Stack Demo"},
     simple_sessions([
         "Document Databases 101: Collections, Documents & When to Use Them",
         "Hands-On with a Mongo-Style Document DB from Python (CRUD & Simple Queries)",
         "Modeling in a Document DB: Embedding vs Referencing & Basic Aggregations",
         "Indexes, Query Patterns & Evolving Schemas in Document DBs",
         "Mini Project 1: Document-Backed Feature for an Existing App",
         "Redis Fundamentals: Keys, Expiry & Basic Data Structures",
         "Caching Patterns with Redis: Read-Through, Write-Through & TTL-Based Caches",
         "Combining Relational + Document DB + Redis in a Small System",
         "Connection Management, Timeouts & Configuration for Doc DB + Redis",
         "Mini Project 2: Hybrid Data Stack Demo (RDBMS + Document DB + Redis Cache)",
     ]),
     [],
     [],
     REFLECTION_ADR,
     None,
     ["**Phase A:** document modeling → MP1 feature", "**Phase B:** Redis cache → MP2 hybrid demo"],
     ["Messaging, streaming, and deep testing (Level 15)"]),
    (15, "Data Systems Builder → Service Integrator", "📡 Level 15: Data Systems Builder → Service Integrator — Messaging & Deep Testing",
     "Design message-driven services with RabbitMQ/Kafka and robust tests",
     "2 Mini Projects: RabbitMQ worker and message-driven service with full test suite",
     "Build async flows with unit, integration, and contract tests at boundaries.",
     "Phase A: Messaging & Streaming Basics", "Phase B: Testing Async Systems",
     {"short": "RabbitMQ Worker"}, {"short": "Message-Driven Service"},
     simple_sessions([
         "Messaging & Streaming 101: Queues, Topics & When to Use Them",
         "RabbitMQ from Python: Producers, Consumers & Acknowledgements",
         "Kafka from Python: Topics, Partitions & Simple Consumer Groups",
         "Designing Message-Driven Flows for a Small Application",
         "Mini Project 1: RabbitMQ-Backed Background Worker for an Existing Feature",
         "Advanced Unit Testing: Mocks, Fakes & Testing Around Message Boundaries",
         "Integration Testing with Real Infrastructure (DB + RabbitMQ + Kafka via Containers)",
         "Contract & Schema Testing for Messages (Payload Validation & Backwards Compatibility)",
         "End-to-End Scenarios & Debugging Asynchronous Flows",
         "Mini Project 2: Message-Driven Mini Service with Full Test Suite",
     ]),
     [],
     [],
     REFLECTION_ADR,
     None,
     ["**Phase A:** RabbitMQ/Kafka basics → MP1 worker", "**Phase B:** integration + contract tests → MP2 service"],
     ["End-to-end HTTP services (Level 16)"]),
    (16, "Service Integrator → Service Builder", "🌐 Level 16: Service Integrator → Service Builder — End-to-End Service Foundations",
     "Build a small HTTP service with layers, tests, and documentation",
     "2 Mini Projects: CRUD microservice and end-to-end documented service",
     "Expose HTTP/JSON APIs backed by real databases with clear layering.",
     "Phase A: HTTP API Foundations", "Phase B: Layered Service & Tests",
     {"short": "CRUD Microservice"}, {"short": "End-to-End Service"},
     simple_sessions([
         "From Scripts to Services: HTTP, REST & Resource Modeling Basics",
         "Designing API Endpoints & Request/Response Schemas (JSON Contracts)",
         "Implementing a Simple CRUD API with a Python Web Framework",
         "Hooking the API to the Data Layer (DB Repositories + Basic Validation)",
         "Mini Project 1: CRUD Microservice for an Existing Domain (Tasks/Contacts/etc.)",
         "Service Structure: Routers/Controllers, Services & Repositories",
         "Basic Security & Guardrails: Simple Auth, Input Validation & Error Handling",
         "Testing the Service: Unit Tests for Logic, Functional Tests for Endpoints",
         "Running the Service Locally: Environments, Config & Simple Documentation",
         "Mini Project 2: End-to-End Service with DB, Tests & API Documentation",
     ]),
     [],
     [],
     REFLECTION_ADR,
     "Integrates data layers from Levels 6, 13, and 14.",
     ["**Phase A:** REST + CRUD → MP1 microservice", "**Phase B:** layers + tests → MP2 documented service"],
     ["Service hardening and observability (Level 17)"]),
    (17, "Service Builder → Systems Crafter", "🛡️ Level 17: Service Builder → Systems Crafter — Service Hardening & Observability",
     "Harden services with logging, metrics, config, and Docker-based stacks",
     "2 Mini Projects: hardened service and containerized observable mini stack",
     "Run Python services with production-like configuration, health checks, and observability.",
     "Phase A: Hardening & Observability Basics", "Phase B: Docker & Production-Like Ops",
     {"short": "Hardened Service"}, {"short": "Containerized Stack"},
     simple_sessions([
         "Service Hardening 101: Failure Modes, Timeouts & Retries",
         "Structured Logging & Log Levels for Services",
         "Configuration Management: Env Vars, Config Files & 12-Factor Basics",
         "Health Checks & Basic Metrics (Counters, Timers, Gauges)",
         "Mini Project 1: Harden an Existing Service (Timeouts, Logs, Health Endpoint)",
         "Docker for Python Services: Writing a Simple, Production-Friendly Dockerfile",
         "Docker Compose: Running Service + DB/Redis/RabbitMQ Together Locally",
         "Observability in Containers: Logs, Metrics & Simple Dashboards",
         "Production-Like Environments: Resource Limits, Readiness & Rollout Basics",
         "Mini Project 2: Containerized, Observable Mini Stack (Service + Infra)",
     ]),
     [],
     [],
     REFLECTION_ADR,
     "Harden the Level 16 service in MP1; compose full stack in MP2.",
     ["**Phase A:** logging/metrics/health → MP1 hardened service", "**Phase B:** Docker Compose → MP2 observable stack"],
     ["Capstone project and portfolio (Level 18)"]),
    (18, "Systems Crafter → Curious Professional", "🏁 Level 18: Systems Crafter → Curious Professional — Capstone & Portfolio",
     "Ship a capstone project with docs, tests, CI/CD, and portfolio storytelling",
     "2 Mini Projects: capstone MVP and v1.0 portfolio release",
     "Consolidate the full journey into one realistic, documented, tested system.",
     "Phase A: Capstone Design & MVP", "Phase B: Docs, CI/CD & Portfolio",
     {"short": "Capstone MVP"}, {"short": "Capstone v1.0 Release"},
     simple_sessions([
         "Choosing & Scoping Your Capstone (Domain, Users, Success Criteria)",
         "Writing a Lightweight Design Doc (Architecture, Data, Interfaces)",
         "Integrating Building Blocks: DB, Caching, Messaging & HTTP APIs",
         "Capstone Implementation Sprint 1 (Core Functionality)",
         "Mini Project 1: Capstone MVP (End-to-End Happy Path Working)",
         "Docs & Developer Experience: README, API Docs & Quickstart",
         "CI/CD Basics: Automated Tests, Linting & Simple Deployment Pipeline (e.g. GitHub Actions)",
         "Polishing & Refactoring: Code Quality Pass, Logging/Metrics Review, Packaging for Reuse",
         "Storytelling & Next Steps: Writing a Portfolio Case Study & Future Learning Roadmap",
         "Mini Project 2: Capstone v1.0 Release (Tagged, Documented & Showcased in Portfolio)",
     ]),
     [
         "A working capstone with ONE primary end-to-end flow",
         "Documentation another developer could use to run the project",
         "CI/CD pipeline running tests and linting automatically",
         "A portfolio case study explaining what you built and learned",
     ],
     [
         "**Scope creep** — building every feature instead of one polished journey",
         "**Perfection paralysis** — never shipping because the capstone is never done",
         "**Undocumented stack** — code works but nobody else can run it",
         "**No tests on the happy path** — the one flow you demo is untested",
     ],
     [
         "What one user journey did I ship end-to-end?",
         "What would I cut if I had half the time?",
         "What is in my portfolio case study headline?",
         "What one ADR best explains my capstone architecture?",
     ],
     "**Program capstone:** succeed with ONE end-to-end scenario; stretch goals only after the core works.",
     ["**Phase A:** design + MVP → MP1 happy path", "**Phase B:** docs + CI/CD → MP2 v1.0 release"],
     ["Post-program specialization tracks (optional — see master plan)"],
     """### Capstone scope control (critical)

> **Your capstone succeeds if ONE end-to-end scenario works well.**

* ✅ Focus on **one primary user journey** first
* ✅ Make that flow polished, tested, and documented
* ❌ Do not add complexity \"just because\" (YAGNI)

"""),
]

for spec in LEVEL_SPECS:
    (level, from_to, title, tagline, outcome, transform, pa, pb, mp1, mp2, sessions,
     exit_c, anti, refl, bridge, assess, next_s) = spec[:17]
    extra = spec[17] if len(spec) > 17 else ""
    topics = [s[1] for s in sessions]
    mp1_b = [f"Deliverable aligned to {topics[4]} (see master plan)."]
    mp2_b = [f"Deliverable aligned to {topics[9]} (see master plan)."]
    pa_s, pb_s = phase_sessions(level, topics, mp1_b, mp2_b)
    objectives = [
        f"Complete Phase A sessions and Mini Project 1 for Level {level}",
        f"Complete Phase B sessions and Mini Project 2 for Level {level}",
        f"Meet Level {level} exit criteria before advancing",
    ]
    if level == 18:
        objectives = [
            "Scope and ship ONE primary end-to-end capstone flow",
            "Document, test, and CI/CD the capstone for portfolio use",
            "Write a case study and personal learning roadmap",
        ]
    add({
        "level": level,
        "from_to": from_to,
        "title": title,
        "tagline": tagline,
        "transform": transform,
        "outcome": outcome,
        "objectives": objectives,
        "sessions": sessions,
        "phase_a_name": pa,
        "phase_b_name": pb,
        "mp1": mp1,
        "mp2": mp2,
        "bridge": bridge,
        "learning_outcome": bullet_block([
            f"Complete Level {level} session outcomes and both mini projects",
            "Apply concepts from the master plan with original examples",
            f"Be ready for {'Level ' + str(level + 1) if level < 18 else 'post-program specialization'}",
        ]),
        "exit_criteria": exit_c,
        "anti_patterns": anti,
        "reflection": refl,
        "phase_a_sessions": pa_s,
        "phase_b_sessions": pb_s,
        "assessment": assess,
        "next_steps": next_s,
        "extra_sections": extra,
    })


def main() -> None:
    for data in LEVELS:
        level = data["level"]
        out_dir = OUT / f"L{level}"
        out_dir.mkdir(parents=True, exist_ok=True)
        content = render_level(data)
        (out_dir / "_Plan.md").write_text(content, encoding="utf-8")
        print(f"Wrote L{level}/_Plan.md")


if __name__ == "__main__":
    main()
