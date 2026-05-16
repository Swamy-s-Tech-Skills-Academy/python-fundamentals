# 🤖 Copilot Instructions for Python Fundamentals Project

**Project:** Python Fundamentals Curriculum  
**Owner:** Swamy's Tech Skills Academy  
**Purpose:** Educational content development and maintenance

---

## 🚨 **CRITICAL RULES - READ FIRST**

### **1. 🛡️ DO NOT CORRUPT EXISTING FILES**

- **NEVER** make changes that break existing content
- **ALWAYS** preserve the original structure and formatting
- **VERIFY** changes are minimal and necessary before applying
- **TEST** understanding by reading the full context before editing
- **ASK FOR CONFIRMATION** if changes seem extensive or risky

### **2. 📖 UNDERSTAND BEFORE ACTING**

- **READ** the entire file or section before making any edits
- **ANALYZE** the existing structure and content quality
- **RESPECT** the pedagogical flow and curriculum design
- **PRESERVE** all educational content, examples, and explanations

### **3. 🎯 MAKE PRECISE, TARGETED CHANGES**

- **IDENTIFY** the exact issue to be fixed
- **ISOLATE** the specific text that needs modification
- **MINIMIZE** the scope of changes
- **MAINTAIN** surrounding context and formatting

### **4. 🚫 ZERO-COPY POLICY (Non-Negotiable)**

- **NEVER** copy text verbatim from books, articles, websites, videos, or third-party materials
- **NEVER** mirror a source's outline, section order, headings, or example sequence
- **NEVER** use "light paraphrasing" — must transform completely
- **ALWAYS** create diagrams in Mermaid-first style with ASCII fallback (never embed copyrighted figures)
- **ALWAYS** write fresh, minimal code from first principles
- Brief quotations allowed ONLY with quotation marks and source citation
- **Goal**: Create transformative educational content, not just reformative

**See `.cursor/rules/01_educational-content-rules.mdc` for complete Zero-Copy Policy and Transformative Workflow details.**

### **5. 🔒 INTERNAL CONTENT INTAKE POLICY (Source Notes + Working Samples)**

- **BORROW** concepts, misconceptions, and exercise patterns only; do not reuse exact wording, order, or narration.
- Treat `source-material/` files as internal, read-only instructor notes; rewrite all curriculum text in a fresh structure and voice.
- Promote sandbox examples from `src/Working/` only after cleanup, renaming, and alignment with session outcomes — and only when Swamy explicitly asks you to edit or promote those Working files.
- Keep published session references on formal paths (`src/L{level}/S{session}/`) and never on sandbox paths.
- Apply normal quality gates to imported ideas: clarity, technical correctness, and beginner-level pedagogy.
- This policy is internal operating guidance and should not be written into publish-facing curriculum docs.

### **6. 🗂️ SESSION BUCKETING SAFETY (New Content Placement)**

- Treat `docs/meetup/L1/sessions.md` (status table) as the placement guard for Level 1 meetup updates.
- New content from `source-material/` or `src/Working/` must be added to planned/new sessions by default.
- Do **not** inject new educational content into already completed sessions unless the user explicitly approves it.
- If status is ambiguous, stop and ask for permission before placing content.

### **7. 🛑 HANDS-OFF: `src/Working/` (unless Swamy requests it)**

- **Do not** create, edit, move, rename, or delete anything under `src/Working/` **unless Swamy explicitly asks** for that Working path or folder in the current task.
- Use `src/L{level}/S{session}/` and `docs/sessions/` for routine curriculum fixes; read **`docs/RepositoryStructure.md`** (section **src/Working/**) only for routing context when advising on promotion.
- Mass refactors or repo-wide formatting must **not** touch `src/Working/` unless the task scope names it.

### **8. ✅ FORMAL PYTHON QUALITY SCOPE**

- Treat blocking Python quality checks as scoped to formal curriculum paths: `src/L1` and `src/L2`.
- Do not treat `src/Working/` quality findings as blocking unless Swamy explicitly includes Working paths in scope.

---

## 📋 **PROJECT STRUCTURE OVERVIEW**

> **📋 Single Source of Truth**: For the most detailed and up-to-date repository structure, see [`docs/RepositoryStructure.md`](../docs/RepositoryStructure.md). This section provides a quick overview for AI assistants.
> **🐍 Python File Templates**: For approved Python file shapes, see [`docs/PythonFileTemplates.md`](../docs/PythonFileTemplates.md). Use it when creating or refactoring lesson scripts, Working samples, helper modules, or app entry points.

### **Current Organization:**

```text
python-fundamentals/
├── docs/
│   ├── 01_Python-Fundamentals-MasterPlan.md  # Complete course master plan (roadmap)
│   ├── images/              # Educational images and screenshots
│   │   └── S1/              # Session 1 images
│   ├── RepositoryStructure.md
│   └── sessions/
│       ├── L1/              # Level 1: Noob → Nerd
│       │   ├── _Plan.md
│       │   ├── S1.md
│       │   └── ...
│       └── L2/              # Level 2: Nerd → Novice
│           ├── _Plan.md
│           ├── S1.md
│           └── ...
├── src/
│   ├── L1/
│   │   ├── S1/              # Session 1 practice files
│   │   │   ├── 01_hello.py
│   │   │   ├── 02_interactive_hello.py
│   │   │   └── bytecode_demo.py
│   │   ├── S2/ ... S4/      # Sessions 2–4 practice files
│   │   ├── S5/              # Session 5 – Mini Project 1 files
│   │   │   ├── 01_PEP8_naming_and_spacing.py
│   │   │   ├── 02_del_and_bool_arithmetic.py
│   │   │   ├── 03_simple_calculator.py
│   │   │   └── calculator_utils.py
│   │   ├── S6/ ... S9/      # Sessions 6–9 practice files
│   │   └── S10/             # Session 10 – Mini Project 2 files
│   │       └── profile_generator.py
│   ├── L2/                  # Level 2 practice files
│   │   ├── S1/ ... S4/      # Sessions 1–4 practice files
│   │   ├── S5/              # Session 5 – Mini Project 1 files
│   │   ├── S6/ ... S9/      # Sessions 6–9 practice files
│   │   └── S10/             # Session 10 – Mini Project 2 files
│   └── Working/             # Sandbox — see docs/RepositoryStructure.md (hands-off unless Swamy asks)
│       ├── module3/         # Foundational drafts (promote into formal session folders)
│       ├── module4/         # Foundational drafts (promote into formal session folders)
│       └── module5/         # Foundational drafts (promote into formal session folders)
└── README.md                # Project overview and quick start
```

### **File Relationships:**

- `docs/sessions/L1/S1.md` ↔ `src/L1/S1/` (practice files)
- `docs/sessions/L2/S1.md` ↔ `src/L2/S1/` (practice files)
- `docs/sessions/L1/_Plan.md` → Overall curriculum structure
- `docs/sessions/L2/_Plan.md` → Overall curriculum structure
- `docs/01_Python-Fundamentals-MasterPlan.md` → Master roadmap across all levels
- `README.md` → Entry point with navigation links
- `docs/RepositoryStructure.md` (**src/Working/**) → routing from staging (`module3/`, `module4/`, `module5/`) to formal `src/L{level}/S{session}/` (do not edit Working files unless Swamy requests)

---

## 🗂️ `src/Working/` — Sandbox Staging Area

`src/Working/` is the **live-coding and experiment zone** — used during teaching sessions to write and run code informally. Files here may later be **promoted** into the formal `src/L{level}/S{session}/` structure.

| `src/Working/` | `src/L{level}/S{session}/` |
|---|---|
| Informal staging (`module3/`, `module4/`, `module5/`; see `docs/RepositoryStructure.md`; **hands-off unless Swamy asks**) | Formal, numbered, tested practice files |
| Flexible file names (`hello_world.py`, `sample1.py`) | `01_name.py` convention, polished |
| Work-in-progress | Production-quality curriculum |

### Promotion workflow

1. Identify which `L{level}/S{session}/` the file belongs to.
2. Rename to `01_name.py` (or next available number).
3. Add standard file header, clean comments, verify it runs.
4. Move to `src/L{level}/S{session}/`.
5. Reference the new file in the matching `docs/sessions/L{level}/S{session}.md`.

### Standard file template

The `main(argv)` / `HELP_TEXT` / `raise SystemExit` pattern (see `src/Working/module4/01_sample.py` or `src/L1/S6/08_boolean_logic_precedence.py`) is the **preferred template** for Working drafts and promoted files. For the full policy, including teaching-script and helper/app exceptions, see [`docs/PythonFileTemplates.md`](../docs/PythonFileTemplates.md):

```python
"""Module docstring explaining what the file demonstrates."""

import sys

HELP_TEXT = """..."""

def main(argv: list[str]) -> int:
    # implementation
    return 0

raise SystemExit(main(sys.argv))
```

### Rules for Copilot / AI assistants

- ✅ `src/Working/` files are informal — apply relaxed quality expectations
- ✅ When asked to promote / bucket a Working file, follow the promotion workflow
- ❌ Do **not** reference `src/Working/` paths in `docs/sessions/` — only promoted `src/L{level}/S{session}/` paths belong there
- ❌ Do **not** apply CI lint failures on Working files as blockers

---

## 🎓 **CURRICULUM PHILOSOPHY**

### **Educational Approach:**

- **30-minute sessions** - Realistic time constraints
- **Content splitting policy** - For session/lesson educational content, when content exceeds 1000 lines, ALWAYS SPLIT into multiple parts (never trim/condense); roadmap/governance docs (e.g., `docs/01_Python-Fundamentals-MasterPlan.md`) are exempt unless explicitly requested
- **Progressive complexity** - Each session builds on previous
- **Hands-on practice** - Every concept has practical application
- **Visual learning** - Emojis, diagrams, and clear formatting
- **Beginner-focused** - No assumptions about prior knowledge

**See `.cursor/rules/01_educational-content-rules.mdc` for complete 30-minute session and splitting policy details.**

### **Content Quality Standards:**

- **Pedagogically sound** - Based on learning theory
- **Technically accurate** - All code examples work correctly
- **Professionally presented** - Industry-standard documentation
- **Accessible** - Clear language and multiple learning styles

---

## 🧠 **CoT/ReAct METHODOLOGY**

### **For Content CREATION (THINK → REASON → ACT → VERIFY):**

| Phase | Steps |
|-------|-------|
| **THINK** | Understand objective → Decompose into chunks → Sequence logically → Anticipate misconceptions |
| **REASON** | Check prerequisites → Map connections → Design examples → Identify pitfalls |
| **ACT** | Write content → Create code examples → Add diagrams → Design exercises |
| **VERIFY** | Is it clear? → Complete? → Progressive? → Original? |

### **For Content REVIEW (OBSERVE → ANALYZE → REASON → VERIFY → ACT):**

| Phase | Steps |
|-------|-------|
| **OBSERVE** | Scan and catalog ALL files in scope |
| **ANALYZE** | Open and examine EVERY file individually |
| **REASON** | Apply logical reasoning to identify issues |
| **VERIFY** | Cross-check findings and validate compliance |
| **ACT** | Document findings and update content |

### **Decision Framework:**

```text
CREATION: THINK → REASON → ACT → VERIFY → (iterate if needed)
REVIEW:   OBSERVE → ANALYZE → REASON → VERIFY → ACT
```

### **Reasoning in Educational Content:**

**CRITICAL**: All code examples and explanations must show the "Why" behind decisions, not just the "What".

**✅ DO**: Include explicit reasoning for code design decisions

- Show why a data structure was chosen
- Explain alternative approaches and trade-offs
- Make the thought process visible to learners

**❌ AVOID**: Stating facts without reasoning

- Don't just say "use a dictionary" - explain WHY
- Don't skip the reasoning chain from problem to solution

**See `.cursor/rules/01_educational-content-rules.mdc` for full CoT/ReAct details and reasoning examples.**

---

## 🔧 **EDITING GUIDELINES**

### **When Making Changes:**

#### **✅ SAFE EDITS:**

- Fixing typos and spelling errors
- Correcting broken links
- Updating file paths that are demonstrably wrong
- Fixing character encoding issues (corrupted emojis)
- Adding missing sections that are clearly incomplete

#### **⚠️ CAREFUL EDITS:**

- Modifying code examples (ensure they still work)
- Changing file structure references
- Updating installation instructions
- Modifying pedagogical explanations

#### **🚫 AVOID:**

- Large-scale content reorganization without explicit request
- Changing the pedagogical approach or learning sequence
- Removing or significantly altering existing explanations
- Modifying time allocations or session structure
- Changing the emoji-based navigation system

### **Before Any Edit:**

1. **Read the full context** - Understand what you're changing
2. **Identify the specific problem** - What exactly needs fixing?
3. **Plan minimal changes** - What's the smallest fix that works?
4. **Preserve surrounding content** - Don't alter unrelated text
5. **Verify the change makes sense** - Does it improve the content?

### **File Path Corrections:**

- Current structure uses `L1/S1/` hierarchy
- Update references from old `S1/` to new `L1/S1/` structure
- Maintain consistency between documentation and code locations

---

## 📝 **COMMON TASKS**

### **Path Updates:**

```markdown
# OLD (incorrect)
src/S1/01_hello.py

# NEW (correct)
src/L1/S1/01_hello.py
```

### **Character Encoding Fixes:**

```markdown
# BROKEN
print("🚀 Advanced Python Preview")

# FIXED  
print("🚀 Advanced Python Preview")
```

### **Link Corrections:**

```text
# OLD (incorrect)
docs/sessions/S1.md
docs/sessions/L1/01_S1.md

# NEW (correct)
docs/sessions/L1/S1.md
```

### **File Reference Validation:**

**CRITICAL**: All file references must:

- ✅ Keep Python practice file prefixes (`01_`, `02_`, etc.) and use exact existing session doc names (`S1.md`, `S5.md`, `S10.md`, etc.)
- ✅ Use correct `L{level}/S{session}/` directory structure
- ✅ Match actual file names exactly
- ✅ Be verified before committing

**Common Errors to Avoid:**

- ❌ Wrong session doc name: `01_S1.md` → ✅ `S1.md`
- ❌ Missing level identifier: `sessions/S1/` → ✅ `sessions/L1/S1.md`
- ❌ Incorrect path structure: `src/S1/` → ✅ `src/L1/S1/`

**See `.cursor/rules/04_markdown-standards.mdc` for detailed file reference validation patterns.**

---

## 🎯 **QUALITY CHECKLIST**

Before submitting any changes, verify:

- [ ] **Content preserved** - No educational material lost
- [ ] **Structure intact** - Formatting and organization maintained
- [ ] **Links work** - All file references are correct and match actual file names exactly
- [ ] **File references validated** - All references use `L{level}/S{session}/` structure
- [ ] **Code examples** - All Python code is syntactically correct
- [ ] **Reasoning quality** - Code design decisions include explicit reasoning (why this approach?)
- [ ] **Consistency** - Changes align with overall project structure
- [ ] **Readability** - Changes improve rather than degrade clarity

**See `.cursor/rules/03_quality-assurance.mdc` for complete quality checklist.**

---

## 🚨 **EMERGENCY PROCEDURES**

### **If You Accidentally Corrupt Content:**

1. **STOP immediately** - Don't make additional changes
2. **INFORM the user** - Be transparent about what happened
3. **SUGGEST restoration** - Recommend reverting to previous version
4. **LEARN from the mistake** - Understand what went wrong

### **If Unsure About Changes:**

1. **ASK for clarification** - Better to check than assume
2. **DESCRIBE your plan** - Explain what you intend to change
3. **REQUEST confirmation** - Get approval before proceeding
4. **OFFER alternatives** - Suggest different approaches if needed

---

## 💡 **SUCCESS PRINCIPLES**

1. **Precision over Speed** - Take time to understand before acting
2. **Preservation over Innovation** - Maintain existing quality
3. **Communication over Assumption** - Ask questions when uncertain
4. **Incremental over Wholesale** - Make small, targeted changes
5. **Verification over Trust** - Double-check all modifications

---

## 📞 **WHEN IN DOUBT**

**ALWAYS:**

- Read more context
- Ask for clarification
- Make smaller changes
- Preserve existing content
- Communicate your concerns

**NEVER:**

- Make assumptions about what's needed
- Change content you don't fully understand
- Rush through complex modifications
- Ignore the existing pedagogical structure
- Make changes without clear justification

---

## 🔗 **Related Documentation**

- **📋 Repository Structure (Single Source of Truth)**: [`docs/RepositoryStructure.md`](../docs/RepositoryStructure.md) - **Authoritative repository structure documentation**
- **Cursor AI Rules**: `.cursor/rules/` - Comprehensive modular rules for Cursor AI
  - See `.cursor/rules/README.md` for overview of all rule files
  - Rules cover: educational content, repository structure, quality assurance, markdown standards, primary directives, cross-level integration
- **Main README**: `README.md` - Project overview and quick start guide
- **Level 1 Plan**: `docs/sessions/L1/_Plan.md` - Complete Level 1 curriculum plan

**Note**:

- `docs/RepositoryStructure.md` is the **single source of truth** for repository structure
- `.cursor/rules/` and `.github/copilot-instructions.md` should reference `docs/RepositoryStructure.md` for structure details
- Both provide guidance for AI assistants working with this repository

---

**Remember: This is educational content that transforms beginners into programmers. Every word matters, every example counts, and every student's learning journey depends on the quality and integrity of this curriculum.**

**🎯 When in doubt, preserve and ask. When certain, proceed with precision.**
