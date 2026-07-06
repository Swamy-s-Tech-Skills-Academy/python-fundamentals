---
learning_level: "Data Systems Builder → Service Integrator"
level_number: 15
stage_part: "Part 3 — Python Systems Engineering"
prerequisites:
  - "docs/sessions/L14/_Plan.md"
total_duration: "~5 hours core guided instruction (+ MPs)"
format: "2 phases × (4 sessions + 1 mini project) = 10 sessions total"
outcome: "2 Mini Projects: RabbitMQ worker and message-driven service with full test suite"
transformation_focus: "Build async flows with unit, integration, and contract tests at boundaries."
curriculum_status: "Draft"
delivery_status: "Not started (meetup schedule TBD)"
repository_status: "Planned — `_Plan.md` scaffold; session docs and practice code pending"
master_plan: "docs/01_Python-Fundamentals-MasterPlan.md"
learning_objectives:
  - "Complete Phase A sessions and Mini Project 1 for Level 15"
  - "Complete Phase B sessions and Mini Project 2 for Level 15"
  - "Meet Level 15 exit criteria before advancing"
related_topics:
  prerequisites:
    - "docs/sessions/L14/_Plan.md"
  builds_upon:
    - "docs/sessions/L14/_Plan.md"
  enables:
    - "docs/sessions/L16/_Plan.md"
  cross_refs:
    - "docs/01_Python-Fundamentals-MasterPlan.md"
sessions:
  - session: 1
    topic: "Messaging & Streaming 101: Queues, Topics & When to Use Them"
    duration: "30 min"
    type: "Knowledge"
    curriculum: "Draft"
    delivery: "Pending"
    file: "docs/sessions/L15/S1.md"
  - session: 2
    topic: "RabbitMQ from Python: Producers, Consumers & Acknowledgements"
    duration: "30 min"
    type: "Knowledge"
    curriculum: "Draft"
    delivery: "Pending"
    file: "docs/sessions/L15/S2.md"
  - session: 3
    topic: "Kafka from Python: Topics, Partitions & Simple Consumer Groups"
    duration: "30 min"
    type: "Knowledge"
    curriculum: "Draft"
    delivery: "Pending"
    file: "docs/sessions/L15/S3.md"
  - session: 4
    topic: "Designing Message-Driven Flows for a Small Application"
    duration: "30 min"
    type: "Knowledge"
    curriculum: "Draft"
    delivery: "Pending"
    file: "docs/sessions/L15/S4.md"
  - session: "5 (MP 1)"
    topic: "Mini Project 1: RabbitMQ-Backed Background Worker for an Existing Feature"
    duration: "30 min"
    type: "Project"
    curriculum: "Draft"
    delivery: "Pending"
    file: "docs/sessions/L15/S5.md"
  - session: 6
    topic: "Advanced Unit Testing: Mocks, Fakes & Testing Around Message Boundaries"
    duration: "30 min"
    type: "Knowledge"
    curriculum: "Draft"
    delivery: "Pending"
    file: "docs/sessions/L15/S6.md"
  - session: 7
    topic: "Integration Testing with Real Infrastructure (DB + RabbitMQ + Kafka via Containers)"
    duration: "30 min"
    type: "Knowledge"
    curriculum: "Draft"
    delivery: "Pending"
    file: "docs/sessions/L15/S7.md"
  - session: 8
    topic: "Contract & Schema Testing for Messages (Payload Validation & Backwards Compatibility)"
    duration: "30 min"
    type: "Knowledge"
    curriculum: "Draft"
    delivery: "Pending"
    file: "docs/sessions/L15/S8.md"
  - session: 9
    topic: "End-to-End Scenarios & Debugging Asynchronous Flows"
    duration: "30 min"
    type: "Knowledge"
    curriculum: "Draft"
    delivery: "Pending"
    file: "docs/sessions/L15/S9.md"
  - session: "10 (MP 2)"
    topic: "Mini Project 2: Message-Driven Mini Service with Full Test Suite"
    duration: "30 min"
    type: "Project"
    curriculum: "Draft"
    delivery: "Pending"
    file: "docs/sessions/L15/S10.md"
---

# 📡 Level 15: Data Systems Builder → Service Integrator — Messaging & Deep Testing

## Design message-driven services with RabbitMQ/Kafka and robust tests

> **Stage:** Part 3 — Python Systems Engineering (Levels 13–18) · **Program:** [Python Software Engineering Journey](../../01_Python-Fundamentals-MasterPlan.md)
>
> 1. **Level:** Data Systems Builder → Service Integrator
> 1. **Format:** 2 phases × (4 sessions + 1 mini project) = 10 sessions total
> 1. **Outcome:** 2 Mini Projects: RabbitMQ worker and message-driven service with full test suite
> 1. **Core guided time:** ~5 hours core guided instruction (+ MPs)

## Powered by ShyvnTech & Swamy's Tech Skills Academy

> **Transformation Focus:** Build async flows with unit, integration, and contract tests at boundaries.

### Level 15 status (three axes)

| Axis | Status |
| --- | --- |
| **Curriculum** | Draft — level plan aligned to master plan; session docs pending |
| **Delivery** | Not started (meetup schedule TBD) |
| **Repository** | Planned — `_Plan.md` scaffold; session docs and practice code pending |

---

## 🎯 **Level 15 Learning Path (Data Systems Builder → Service Integrator)**

| Phase | Session | Topic | Duration | Type | Curriculum | Delivery |
| ----- | ------- | ----- | -------- | ---- | ---------- | -------- |
| A | 1 | Messaging & Streaming 101: Queues, Topics & When to Use Them | 30 min | 📚 Knowledge | Draft | Pending |
| A | 2 | RabbitMQ from Python: Producers, Consumers & Acknowledgements | 30 min | 📚 Knowledge | Draft | Pending |
| A | 3 | Kafka from Python: Topics, Partitions & Simple Consumer Groups | 30 min | 📚 Knowledge | Draft | Pending |
| A | 4 | Designing Message-Driven Flows for a Small Application | 30 min | 📚 Knowledge | Draft | Pending |
| A | 5 (MP 1) | Mini Project 1: RabbitMQ-Backed Background Worker for an Existing Feature *(after Session 4)* | 30 min | 🛠️ Project | Draft | Pending |
| B | 6 | Advanced Unit Testing: Mocks, Fakes & Testing Around Message Boundaries | 30 min | 📚 Knowledge | Draft | Pending |
| B | 7 | Integration Testing with Real Infrastructure (DB + RabbitMQ + Kafka via Containers) | 30 min | 📚 Knowledge | Draft | Pending |
| B | 8 | Contract & Schema Testing for Messages (Payload Validation & Backwards Compatibility) | 30 min | 📚 Knowledge | Draft | Pending |
| B | 9 | End-to-End Scenarios & Debugging Asynchronous Flows | 30 min | 📚 Knowledge | Draft | Pending |
| B | 10 (MP 2) | Mini Project 2: Message-Driven Mini Service with Full Test Suite *(after Session 9)* | 30 min | 🛠️ Project | Draft | Pending |

---

## 🗺️ **Visual Roadmap**

```mermaid
flowchart TB
  A["🎯 Data Systems Builder"] --> PhaseA
  PhaseA --> PhaseB
  PhaseB --> K["🎓 Service Integrator"]

  subgraph PhaseA["📘 Phase A: Messaging & Streaming Basics"]
    B1["Session 1"]
    B2["Session 2"]
    B3["Session 3"]
    B4["Session 4"]
    B5["Session 5 (MP 1)<br>RabbitMQ Worker"]
    B1 --> B2 --> B3 --> B4 --> B5
  end

  subgraph PhaseB["📘 Phase B: Testing Async Systems"]
    C1["Session 6"]
    C2["Session 7"]
    C3["Session 8"]
    C4["Session 9"]
    C5["Session 10 (MP 2)<br>Message-Driven Service"]
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

## 📅 **Phase A: Phase A: Messaging & Streaming Basics**

### ✅ Session 1: Messaging & Streaming 101: Queues, Topics & When to Use Them *(Draft · delivery: Pending)*

* Core concepts for Messaging & Streaming 101: Queues, Topics & When to Use Them (see master plan).

🧪 *Practice / deliverable*: `src/L15/S1/` — planned  
📖 *Documentation*: planned `docs/sessions/L15/S1.md`

---

### ✅ Session 2: RabbitMQ from Python: Producers, Consumers & Acknowledgements *(Draft · delivery: Pending)*

* Core concepts for RabbitMQ from Python: Producers, Consumers & Acknowledgements (see master plan).

🧪 *Practice / deliverable*: `src/L15/S2/` — planned  
📖 *Documentation*: planned `docs/sessions/L15/S2.md`

---

### ✅ Session 3: Kafka from Python: Topics, Partitions & Simple Consumer Groups *(Draft · delivery: Pending)*

* Core concepts for Kafka from Python: Topics, Partitions & Simple Consumer Groups (see master plan).

🧪 *Practice / deliverable*: `src/L15/S3/` — planned  
📖 *Documentation*: planned `docs/sessions/L15/S3.md`

---

### ✅ Session 4: Designing Message-Driven Flows for a Small Application *(Draft · delivery: Pending)*

* Core concepts for Designing Message-Driven Flows for a Small Application (see master plan).

🧪 *Practice / deliverable*: `src/L15/S4/` — planned  
📖 *Documentation*: planned `docs/sessions/L15/S4.md`

---

### 🚀 Mini Project 5 (MP 1): RabbitMQ-Backed Background Worker for an Existing Feature *(Draft · delivery: Pending)*

* Deliverable aligned to Mini Project 1: RabbitMQ-Backed Background Worker for an Existing Feature (see master plan).

🧪 *Practice / deliverable*: `src/L15/S5/` — planned  
📖 *Documentation*: planned `docs/sessions/L15/S5 (MP 1).md`

---

## 📅 **Phase B: Phase B: Testing Async Systems**

### ✅ Session 6: Advanced Unit Testing: Mocks, Fakes & Testing Around Message Boundaries *(Draft · delivery: Pending)*

* Core concepts for Advanced Unit Testing: Mocks, Fakes & Testing Around Message Boundaries (see master plan).

🧪 *Practice / deliverable*: `src/L15/S6/` — planned  
📖 *Documentation*: planned `docs/sessions/L15/S6.md`

---

### ✅ Session 7: Integration Testing with Real Infrastructure (DB + RabbitMQ + Kafka via Containers) *(Draft · delivery: Pending)*

* Core concepts for Integration Testing with Real Infrastructure (DB + RabbitMQ + Kafka via Containers) (see master plan).

🧪 *Practice / deliverable*: `src/L15/S7/` — planned  
📖 *Documentation*: planned `docs/sessions/L15/S7.md`

---

### ✅ Session 8: Contract & Schema Testing for Messages (Payload Validation & Backwards Compatibility) *(Draft · delivery: Pending)*

* Core concepts for Contract & Schema Testing for Messages (Payload Validation & Backwards Compatibility) (see master plan).

🧪 *Practice / deliverable*: `src/L15/S8/` — planned  
📖 *Documentation*: planned `docs/sessions/L15/S8.md`

---

### ✅ Session 9: End-to-End Scenarios & Debugging Asynchronous Flows *(Draft · delivery: Pending)*

* Core concepts for End-to-End Scenarios & Debugging Asynchronous Flows (see master plan).

🧪 *Practice / deliverable*: `src/L15/S9/` — planned  
📖 *Documentation*: planned `docs/sessions/L15/S9.md`

---

### 🚀 Mini Project 10 (MP 2): Message-Driven Mini Service with Full Test Suite *(Draft · delivery: Pending)*

* Deliverable aligned to Mini Project 2: Message-Driven Mini Service with Full Test Suite (see master plan).

🧪 *Practice / deliverable*: `src/L15/S10/` — planned  
📖 *Documentation*: planned `docs/sessions/L15/S10 (MP 2).md`

---

## 🎓 **Level 15 Learning Outcomes**

* Complete Level 15 session outcomes and both mini projects
* Apply concepts from the master plan with original examples
* Be ready for Level 16

### Reflection (Level 15)

* What surprised me at this level?
* What was hardest — and what habit will I keep?
* What would I redesign in my mini project?
* What could I explain to a peer in five minutes?
* What one ADR would I write for MP1 or MP2?

---

## 📊 **Assessment Criteria**

* **Phase A:** RabbitMQ/Kafka basics → MP1 worker
* **Phase B:** integration + contract tests → MP2 service

---

## 🎓 **Next Steps & Resources**

* End-to-end HTTP services (Level 16)

✨ Happy Coding! 🐍
