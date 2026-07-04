---
learning_level: "Curious Learner → Data Platform Explorer"
level_number: 13
stage_part: "Part 3 — Python Systems Engineering"
prerequisites:
  - "docs/sessions/L12/_Plan.md"
total_duration: "~5 hours core guided instruction + ~6–10 h guided labs (setup, ORM, migrations)"
format: "2 phases × (4 sessions + 1 mini project) = 10 sessions total"
outcome: "2 Mini Projects: SQLite port and reusable data access layer"
transformation_focus: "Work with PostgreSQL/SQL Server, SQLAlchemy, migrations, and a reusable DAL."
curriculum_status: "Draft"
delivery_status: "Not started (meetup schedule TBD)"
repository_status: "Planned — `_Plan.md` scaffold; session docs and practice code pending"
master_plan: "docs/01_Python-Fundamentals-MasterPlan.md"
learning_objectives:
  - "Complete Phase A sessions and Mini Project 1 for Level 13"
  - "Complete Phase B sessions and Mini Project 2 for Level 13"
  - "Meet Level 13 exit criteria before advancing"
related_topics:
  prerequisites:
    - "docs/sessions/L12/_Plan.md"
  builds_upon:
    - "docs/sessions/L12/_Plan.md"
  enables:
    - "docs/sessions/L14/_Plan.md"
  cross_refs:
    - "docs/01_Python-Fundamentals-MasterPlan.md"
sessions:
  - session: 1
    topic: "SQL Server & PostgreSQL Overview: Architecture, Tools & Local Setup"
    duration: "30 min"
    type: "Knowledge"
    curriculum: "Draft"
    delivery: "Pending"
    file: "docs/sessions/L13/S1.md"
  - session: 2
    topic: "Connecting from Python: Drivers, Connection Strings & Parameterized Queries"
    duration: "30 min"
    type: "Knowledge"
    curriculum: "Draft"
    delivery: "Pending"
    file: "docs/sessions/L13/S2.md"
  - session: 3
    topic: "Schemas, Keys & Constraints in Production Databases"
    duration: "30 min"
    type: "Knowledge"
    curriculum: "Draft"
    delivery: "Pending"
    file: "docs/sessions/L13/S3.md"
  - session: 4
    topic: "Indexes & Query Performance 101 (Execution Plans at a Glance)"
    duration: "30 min"
    type: "Knowledge"
    curriculum: "Draft"
    delivery: "Pending"
    file: "docs/sessions/L13/S4.md"
  - session: "5 (MP 1)"
    topic: "Mini Project 1: Port a SQLite App to PostgreSQL or SQL Server"
    duration: "30–45 min"
    type: "Project"
    curriculum: "Draft"
    delivery: "Pending"
    file: "docs/sessions/L13/S5.md"
  - session: 6
    topic: "Working with SQLAlchemy (Core + Simple ORM Models)"
    duration: "30 min"
    type: "Knowledge"
    curriculum: "Draft"
    delivery: "Pending"
    file: "docs/sessions/L13/S6.md"
  - session: 7
    topic: "Environments & Migrations: Dev/Test/Prod, Alembic-Style Migration Basics"
    duration: "30 min"
    type: "Knowledge"
    curriculum: "Draft"
    delivery: "Pending"
    file: "docs/sessions/L13/S7.md"
  - session: 8
    topic: "Multi-Database Support & Vendor Differences"
    duration: "30 min"
    type: "Knowledge"
    curriculum: "Draft"
    delivery: "Pending"
    file: "docs/sessions/L13/S8.md"
  - session: 9
    topic: "Designing a Reusable Data Access Layer for a Small App"
    duration: "30 min"
    type: "Knowledge"
    curriculum: "Draft"
    delivery: "Pending"
    file: "docs/sessions/L13/S9.md"
  - session: "10 (MP 2)"
    topic: "Mini Project 2: Production-Style Data Layer Library / Module"
    duration: "30–45 min"
    type: "Project"
    curriculum: "Draft"
    delivery: "Pending"
    file: "docs/sessions/L13/S10.md"
---

# 🗄️ Level 13: Curious Learner → Data Platform Explorer — Production Relational Databases

## Connect Python to production-grade relational databases

> **Stage:** Part 3 — Python Systems Engineering (Levels 13–18) · **Program:** [Python Software Engineering Journey](../../01_Python-Fundamentals-MasterPlan.md)
>
> 1. **Level:** Curious Learner → Data Platform Explorer
> 1. **Format:** 2 phases × (4 sessions + 1 mini project) = 10 sessions total
> 1. **Outcome:** 2 Mini Projects: SQLite port and reusable data access layer
> 1. **Core guided time:** ~5 hours core guided instruction + ~6–10 h guided labs (setup, ORM, migrations)

## Powered by ShyvnTech & Swamy's Tech Skills Academy

> **Transformation Focus:** Work with PostgreSQL/SQL Server, SQLAlchemy, migrations, and a reusable DAL.

### Level 13 status (three axes)

| Axis | Status |
| --- | --- |
| **Curriculum** | Draft — level plan aligned to master plan; session docs pending |
| **Delivery** | Not started (meetup schedule TBD) |
| **Repository** | Planned — `_Plan.md` scaffold; session docs and practice code pending |

📌 *Bridge:* Port Level 6 SQLite apps; stretch: full migration automation optional.

---

## 🎯 **Level 13 Learning Path (Curious Learner → Data Platform Explorer)**

| Phase | Session | Topic | Duration | Type | Curriculum | Delivery |
| ----- | ------- | ----- | -------- | ---- | ---------- | -------- |
| A | 1 | SQL Server & PostgreSQL Overview: Architecture, Tools & Local Setup | 30 min | 📚 Knowledge | Draft | Pending |
| A | 2 | Connecting from Python: Drivers, Connection Strings & Parameterized Queries | 30 min | 📚 Knowledge | Draft | Pending |
| A | 3 | Schemas, Keys & Constraints in Production Databases | 30 min | 📚 Knowledge | Draft | Pending |
| A | 4 | Indexes & Query Performance 101 (Execution Plans at a Glance) | 30 min | 📚 Knowledge | Draft | Pending |
| A | 5 (MP 1) | Mini Project 1: Port a SQLite App to PostgreSQL or SQL Server *(after Session 4)* | 30–45 min | 🛠️ Project | Draft | Pending |
| B | 6 | Working with SQLAlchemy (Core + Simple ORM Models) | 30 min | 📚 Knowledge | Draft | Pending |
| B | 7 | Environments & Migrations: Dev/Test/Prod, Alembic-Style Migration Basics | 30 min | 📚 Knowledge | Draft | Pending |
| B | 8 | Multi-Database Support & Vendor Differences | 30 min | 📚 Knowledge | Draft | Pending |
| B | 9 | Designing a Reusable Data Access Layer for a Small App | 30 min | 📚 Knowledge | Draft | Pending |
| B | 10 (MP 2) | Mini Project 2: Production-Style Data Layer Library / Module *(after Session 9)* | 30–45 min | 🛠️ Project | Draft | Pending |

---

## 🗺️ **Visual Roadmap**

```mermaid
flowchart TB
  A["🎯 Curious Learner"] --> PhaseA
  PhaseA --> PhaseB
  PhaseB --> K["🎓 Data Platform Explorer"]

  subgraph PhaseA["📘 Phase A: Production RDBMS Foundations"]
    B1["Session 1"]
    B2["Session 2"]
    B3["Session 3"]
    B4["Session 4"]
    B5["Session 5 (MP 1)<br>SQLite Port"]
    B1 --> B2 --> B3 --> B4 --> B5
  end

  subgraph PhaseB["📘 Phase B: ORM, Migrations & DAL"]
    C1["Session 6"]
    C2["Session 7"]
    C3["Session 8"]
    C4["Session 9"]
    C5["Session 10 (MP 2)<br>Data Layer Module"]
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

## 📅 **Phase A: Phase A: Production RDBMS Foundations**

### ✅ Session 1: SQL Server & PostgreSQL Overview: Architecture, Tools & Local Setup *(Draft · delivery: Pending)*

* Core concepts for SQL Server & PostgreSQL Overview: Architecture, Tools & Local Setup (see master plan).

🧪 *Practice / deliverable*: `src/L13/S1/` — planned  
📖 *Documentation*: planned `docs/sessions/L13/S1.md`

---

### ✅ Session 2: Connecting from Python: Drivers, Connection Strings & Parameterized Queries *(Draft · delivery: Pending)*

* Core concepts for Connecting from Python: Drivers, Connection Strings & Parameterized Queries (see master plan).

🧪 *Practice / deliverable*: `src/L13/S2/` — planned  
📖 *Documentation*: planned `docs/sessions/L13/S2.md`

---

### ✅ Session 3: Schemas, Keys & Constraints in Production Databases *(Draft · delivery: Pending)*

* Core concepts for Schemas, Keys & Constraints in Production Databases (see master plan).

🧪 *Practice / deliverable*: `src/L13/S3/` — planned  
📖 *Documentation*: planned `docs/sessions/L13/S3.md`

---

### ✅ Session 4: Indexes & Query Performance 101 (Execution Plans at a Glance) *(Draft · delivery: Pending)*

* Core concepts for Indexes & Query Performance 101 (Execution Plans at a Glance) (see master plan).

🧪 *Practice / deliverable*: `src/L13/S4/` — planned  
📖 *Documentation*: planned `docs/sessions/L13/S4.md`

---

### 🚀 Mini Project 5 (MP 1): Port a SQLite App to PostgreSQL or SQL Server *(Draft · delivery: Pending)*

* Deliverable aligned to Mini Project 1: Port a SQLite App to PostgreSQL or SQL Server (see master plan).

🧪 *Practice / deliverable*: `src/L13/S5/` — planned  
📖 *Documentation*: planned `docs/sessions/L13/S5 (MP 1).md`

---

## 📅 **Phase B: Phase B: ORM, Migrations & DAL**

### ✅ Session 6: Working with SQLAlchemy (Core + Simple ORM Models) *(Draft · delivery: Pending)*

* Core concepts for Working with SQLAlchemy (Core + Simple ORM Models) (see master plan).

🧪 *Practice / deliverable*: `src/L13/S6/` — planned  
📖 *Documentation*: planned `docs/sessions/L13/S6.md`

---

### ✅ Session 7: Environments & Migrations: Dev/Test/Prod, Alembic-Style Migration Basics *(Draft · delivery: Pending)*

* Core concepts for Environments & Migrations: Dev/Test/Prod, Alembic-Style Migration Basics (see master plan).

🧪 *Practice / deliverable*: `src/L13/S7/` — planned  
📖 *Documentation*: planned `docs/sessions/L13/S7.md`

---

### ✅ Session 8: Multi-Database Support & Vendor Differences *(Draft · delivery: Pending)*

* Core concepts for Multi-Database Support & Vendor Differences (see master plan).

🧪 *Practice / deliverable*: `src/L13/S8/` — planned  
📖 *Documentation*: planned `docs/sessions/L13/S8.md`

---

### ✅ Session 9: Designing a Reusable Data Access Layer for a Small App *(Draft · delivery: Pending)*

* Core concepts for Designing a Reusable Data Access Layer for a Small App (see master plan).

🧪 *Practice / deliverable*: `src/L13/S9/` — planned  
📖 *Documentation*: planned `docs/sessions/L13/S9.md`

---

### 🚀 Mini Project 10 (MP 2): Production-Style Data Layer Library / Module *(Draft · delivery: Pending)*

* Deliverable aligned to Mini Project 2: Production-Style Data Layer Library / Module (see master plan).

🧪 *Practice / deliverable*: `src/L13/S10/` — planned  
📖 *Documentation*: planned `docs/sessions/L13/S10 (MP 2).md`

---

## 🎓 **Level 13 Learning Outcomes**

* Complete Level 13 session outcomes and both mini projects
* Apply concepts from the master plan with original examples
* Be ready for Level 14

### Reflection (Level 13)

* What surprised me at this level?
* What was hardest — and what habit will I keep?
* What would I redesign in my mini project?
* What could I explain to a peer in five minutes?
* What one ADR would I write for MP1 or MP2?

---

## 📊 **Assessment Criteria**

* **Phase A:** production DB setup → MP1 port
* **Phase B:** SQLAlchemy + DAL → MP2 module

---

## 🎓 **Next Steps & Resources**

* Document databases and caching (Level 14)

✨ Happy Coding! 🐍
