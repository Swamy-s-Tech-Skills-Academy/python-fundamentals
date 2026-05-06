---
learning_level: "Nerd → Novice"
level_number: 2
prerequisites:
  - "docs/sessions/L1/_Plan.md"
total_duration: "~6–7 hours"
format: "2 phases × (4 sessions + 1 mini project) = 10 sessions total"
outcome: "2 Mini Projects to develop problem-solving skills"
transformation_focus: "Evolving from someone who can write basic code to someone who can solve real problems with reusable functions and proper error handling"
learning_objectives:
  - "Work with advanced data structures (sets, tuples)"
  - "Use list comprehensions effectively"
  - "Define and use functions for code reusability"
  - "Handle errors gracefully with try/except blocks"
  - "Read from and write to text files"
  - "Organize code into modules"
  - "Organize code into reusable functions"
  - "Complete 2 mini projects demonstrating problem-solving skills"
  - "Be ready for Level 3: Novice → Object Thinker"
related_topics:
  prerequisites:
    - "docs/sessions/L1/_Plan.md"
  builds_upon:
    - "docs/sessions/L1/_Plan.md"
  enables:
    - "docs/01_Python-Fundamentals-MasterPlan.md"
  cross_refs: []
sessions:
  - session: 1
    topic: "Advanced Data Structures: Sets & Tuples"
    duration: "30 min"
    type: "Knowledge"
    status: "Ready"
    file: "docs/sessions/L2/S1.md"
  - session: 2
    topic: "List Comprehensions"
    duration: "30 min"
    type: "Knowledge"
    status: "Ready"
    file: "docs/sessions/L2/S2.md"
  - session: 3
    topic: "Functions: Definition & Basics"
    duration: "30 min"
    type: "Knowledge"
    status: "Ready"
    file: "docs/sessions/L2/S3.md"
  - session: 4
    topic: "Error Handling: try/except Basics"
    duration: "30 min"
    type: "Knowledge"
    status: "Ready"
    file: "docs/sessions/L2/S4.md"
  - session: "MP1"
    topic: "Mini Project 1: Data Processor"
    duration: "30–45 min"
    type: "Project"
    status: "Ready"
    file: "docs/sessions/L2/S5.md"
  - session: 5
    topic: "Functions: Parameters & Return Values"
    duration: "30 min"
    type: "Knowledge"
    status: "Ready"
    file: "docs/sessions/L2/S6.md"
  - session: 6
    topic: "Functions: Scope & Code Organization"
    duration: "30 min"
    type: "Knowledge"
    status: "Ready"
    file: "docs/sessions/L2/S7.md"
  - session: 7
    topic: "File Handling: Reading & Writing Text Files"
    duration: "30 min"
    type: "Knowledge"
    status: "Ready"
    file: "docs/sessions/L2/S8.md"
  - session: 8
    topic: "Modules Deep Dive & Code Organization"
    duration: "30 min"
    type: "Knowledge"
    status: "Ready"
    file: "docs/sessions/L2/S9.md"
  - session: "MP2"
    topic: "Mini Project 2: Contact Manager"
    duration: "30–45 min"
    type: "Project"
    status: "Ready"
    file: "docs/sessions/L2/S10.md"
---

# 🔧 Level 2: Nerd → Novice - Python Fundamentals

## From curious to capable: Building problem-solving skills with functions and files

> 1. **Level:** Nerd → Novice *(building on Level 1, learning functions, error handling, file operations)*
> 1. **Format:** 2 phases × (4 sessions + 1 mini project) = 10 sessions total
> 1. **Outcome:** 2 Mini Projects to develop problem-solving skills  
> 1. **Total Duration:** ~6–7 hours (10 × 30–45 min)

## Powered by ShyvnTech & Swamy's Tech Skills Academy

> **Transformation Focus**: This level transforms you from someone who can write basic code to someone who can solve real problems. You'll learn to write reusable functions, handle errors gracefully, and work with files - essential skills for any Python programmer.

---

## 🎯 **Level 2 Learning Path (Nerd → Novice)**

| Phase | Session | Topic                                                 | Duration  | Type         | Status         |
| ----- | ------- | ----------------------------------------------------- | --------- | ------------ | -------------- |
| A     | 1       | Advanced Data Structures: Sets & Tuples                | 30 min    | 📚 Knowledge | ✅ Ready 📂    |
| A     | 2       | List Comprehensions                                    | 30 min    | 📚 Knowledge | ✅ Ready 📂    |
| A     | 3       | Functions: Definition & Basics                         | 30 min    | 📚 Knowledge | ✅ Ready 📂    |
| A     | 4       | Error Handling: try/except Basics                      | 30 min    | 📚 Knowledge | ✅ Ready 📂    |
| A     | 🚀 MP1  | Mini Project 1: Data Processor *(after Session 4)*   | 30–45 min | 🛠️ Project  | ✅ Ready 📂    |
| B     | 5       | Functions: Parameters & Return Values                 | 30 min    | 📚 Knowledge | ✅ Ready 📂    |
| B     | 6       | Functions: Scope & Code Organization                   | 30 min    | 📚 Knowledge | ✅ Ready 📂    |
| B     | 7       | File Handling: Reading & Writing Text Files           | 30 min    | 📚 Knowledge | ✅ Ready 📂    |
| B     | 8       | Modules Deep Dive & Code Organization                 | 30 min    | 📚 Knowledge | ✅ Ready 📂    |
| B     | 🚀 MP2  | Mini Project 2: Contact Manager *(after 8)*           | 30–45 min | 🛠️ Project  | ✅ Ready 📂    |

---

## 🗺️ **Visual Roadmap**

```mermaid
flowchart TB
    A[🎯 Nerd] --> PhaseA
    PhaseA --> PhaseB
    PhaseB --> K[🎓 Novice]

    subgraph PhaseA[📘 Phase A: Advanced Foundations]
        B1[📚 Session 1<br/>Sets & Tuples]
        B2[📚 Session 2<br/>List Comprehensions]
        B3[🔧 Session 3<br/>Functions Basics]
        B4[🛡️ Session 4<br/>Error Handling]
        B5[🚀 MP1<br/>Mini Project 1: Data Processor]
        B1 --> B2 --> B3 --> B4 --> B5
    end

    subgraph PhaseB[📘 Phase B: File Operations & Advanced Functions]
        C1[🔧 Session 5<br/>Functions: Parameters]
        C2[🔧 Session 6<br/>Functions: Scope]
        C3[📁 Session 7<br/>Text File I/O]
        C4[📦 Session 8<br/>Modules Deep Dive]
        C5[🚀 MP2<br/>Mini Project 2: Contact Manager]
        C1 --> C2 --> C3 --> C4 --> C5
    end

    classDef startEnd fill:#e1f5fe,stroke:#01579b,stroke-width:3px,color:#000
    classDef session fill:#f3e5f5,stroke:#4a148c,stroke-width:2px,color:#000
    classDef project fill:#e8f5e8,stroke:#1b5e20,stroke-width:3px,color:#000

    class A,K startEnd
    class B1,B2,B3,B4,C1,C2,C3,C4 session
    class B5,C5 project
```

ASCII fallback:

```text
[🎯 Nerd]
    |
    v
[📘 Phase A: Advanced Foundations]
    ├─ [📚 Session 1: Sets & Tuples]
    ├─ [📚 Session 2: List Comprehensions]
    ├─ [🔧 Session 3: Functions Basics]
    ├─ [🛡️ Session 4: Error Handling]
    └─ [🚀 MP1: Mini Project 1: Data Processor]
    |
    v
[📘 Phase B: File Operations & Advanced Functions]
    ├─ [🔧 Session 5: Functions: Parameters]
    ├─ [🔧 Session 6: Functions: Scope]
    ├─ [📁 Session 7: Text File I/O]
    ├─ [📦 Session 8: Modules Deep Dive]
    └─ [🚀 MP2: Mini Project 2: Contact Manager]
    |
    v
[🎓 Novice]
```

---

## 📅 **Session-by-Session Breakdown**

## 📅 **Phase A: Advanced Foundations + Mini Project 1**

### 🔄 Session 1: Advanced Data Structures: Sets & Tuples

* **Sets**: Unique collections, set operations (union, intersection, difference)
* **Tuples**: Immutable sequences, when to use tuples vs lists
* Creating and manipulating sets and tuples
* Converting between data structures
* Practical use cases: removing duplicates, coordinate pairs, fixed data

🧪 *Mini Practice*: Remove duplicates from a list, store coordinate pairs, work with unique collections.  
📌 *Feeds into Mini Project 1*: Using sets for unique data, tuples for structured data.

---

### 🔄 Session 2: List Comprehensions

* What are list comprehensions and why use them?
* Basic syntax: `[expression for item in iterable]`
* Adding conditions: `[expression for item in iterable if condition]`
* Nested list comprehensions
* When to use comprehensions vs loops
* Performance considerations

🧪 *Mini Practice*: Transform lists elegantly, filter data, create new lists from existing ones.  
📌 *Feeds into Mini Project 1*: Processing and transforming data efficiently.

---

### 🔄 Session 3: Functions: Definition & Basics

* What are functions and why use them?
* Defining functions with `def`
* Calling functions
* Function naming conventions
* Code reusability and DRY principle
* Functions vs scripts

🧪 *Mini Practice*: Create reusable functions for common tasks, organize code into functions.  
📌 *Feeds into Mini Project 1*: Breaking down problems into functions.

---

### 🔄 Session 4: Error Handling: try/except Basics

* Why error handling matters
* `try/except` block syntax
* Handling specific exceptions
* `else` and `finally` clauses
* Common exceptions: `ValueError`, `TypeError`, `FileNotFoundError`
* Graceful error handling vs program crashes

🧪 *Mini Practice*: Handle user input errors, file errors, type conversion errors.  
📌 *Feeds into Mini Project 1*: Making programs robust with error handling.

---

### 🚀 Mini Project 1: Data Processor

**Goal:** Build a data processing application that uses sets, tuples, list comprehensions, and error handling.

**Features:**

* Process a list of data (e.g., student scores, product prices)
* Remove duplicates using sets
* Transform data using list comprehensions
* Store structured data using tuples
* Handle errors gracefully (invalid input, empty data)
* Organize code into reusable functions
* Display processed results

🧪 *Deliverable*: `src/L2/S5/data_processor.py`

🎯 *Stretch Goals*:

* Add data filtering options
* Calculate statistics (average, min, max)
* Export results to a formatted string

---

## 📅 **Phase B: File Operations & Advanced Functions**

### 🔄 Session 5: Functions: Parameters & Return Values

* Function parameters: positional, keyword, default values
* Multiple parameters and parameter order
* Return values: single and multiple returns
* Returning tuples for multiple values
* `None` and when functions don't return
* Function documentation with docstrings

🧪 *Mini Practice*: Create functions with different parameter types, return multiple values.  
📌 *Feeds into Mini Project 2*: Building functions that work with file data.

---

### 🔄 Session 6: Functions: Scope & Code Organization

* Variable scope: local vs global
* When to use global variables (rarely!)
* Best practices for function design
* Organizing code into multiple functions
* Function composition: calling functions from functions
* Code readability and maintainability

🧪 *Mini Practice*: Organize code into logical functions, understand variable visibility.  
📌 *Feeds into Mini Project 2*: Structuring a file-based application with multiple functions.

---

### 🔄 Session 7: File Handling: Reading & Writing Text Files

* Opening files: `open()` function
* File modes: `'r'`, `'w'`, `'a'`, `'x'`
* Reading files: `read()`, `readline()`, `readlines()`
* Writing files: `write()`, `writelines()`
* Context managers: `with` statement (best practice)
* File paths and working with directories
* Error handling for file operations
* Practical examples: reading configuration, writing logs

🧪 *Mini Practice*: Read from text files, write to text files, handle file errors.  
📌 *Feeds into Mini Project 2*: Reading and writing text data files.

---

### 🔄 Session 8: Modules Deep Dive & Code Organization

* Creating your own modules
* `__name__` and `__main__`: Understanding module execution
* Importing from your own modules
* Organizing code into multiple files
* Best practices for module design
* Code organization: when to split into modules
* Combining functions and modules for larger projects

🧪 *Mini Practice*: Create a module with utility functions, import and use it.  
📌 *Feeds into Mini Project 2*: Structuring a multi-file application.

---

### 🚀 Mini Project 2: Contact Manager

**Goal:** Build a practical application that reads from and writes to text files, uses well-organized functions, and demonstrates modular code structure.

**Features:**

* Read data from a text file
* Process the data using functions
* Display results or statistics
* Write processed data to a new text file
* Handle file errors gracefully
* Organize code into multiple functions
* (Optional) Split code into a module
* Use proper error handling throughout

🧪 *Deliverable*: `src/L2/S10/contact_manager.py`

🎯 *Stretch Goals*:

* Organize code into a separate module file
* Add data filtering/searching capabilities
* Create a simple menu system
* Support multiple input/output file formats

---

## 🎓 **Level 2 Learning Outcomes**

By completing Level 2, you will:

* ✅ Work with advanced data structures (sets, tuples) confidently
* ✅ Use list comprehensions to write elegant, efficient code
* ✅ Define and use functions for code reusability
* ✅ Handle errors gracefully with try/except blocks
* ✅ Read from and write to text files
* ✅ Organize code into modules
* ✅ Organize code into reusable, well-structured functions
* ✅ Understand variable scope and best practices
* ✅ Complete 2 mini projects demonstrating problem-solving skills
* ✅ Be ready for **Level 3: Novice → Object Thinker**

---

## 📊 **Assessment Criteria**

* **Phase A**: Can work with sets/tuples, use list comprehensions, define functions, handle errors → Complete Data Processor Project
* **Phase B**: Can use advanced function features, read/write text files, organize code into modules → Complete Contact Manager Project

**Mini Project Success Indicators:**

* Data Processor works with sets, tuples, list comprehensions, and handles errors gracefully.
* Contact Manager reads/writes text files correctly, uses well-organized functions, and demonstrates modular code structure.

---

## 🎓 **Next Steps & Resources**

After Level 2, you're ready to explore:

* Object-Oriented Programming (classes and objects)
* Advanced error handling and custom exceptions
* Working with CSV and JSON file formats (Level 4)
* Working with databases
* Building more complex applications

**Tools Recommended:**

* Python 3.13+
* VS Code with Python extension
* Text editor for working with files
* Sample CSV/JSON files for practice

✨ Happy Coding! 🐍
