# 🐍 Python Fundamentals: From clueless to curious

A comprehensive, transformation-focused Python curriculum designed to take you from complete beginner to confident Python programmer through 12 progressive levels.

> **Format:** Each level contains 5 hours of training (10 sessions × 30 minutes) culminating in 2 hands-on mini projects.

---

## 📋 **Repository Structure**

📖 **See:** [docs/RepositoryStructure.md](docs/RepositoryStructure.md) — Complete structure documentation (single source of truth)

---

## 🎯 **The 12-Level Python Journey**

| Level | Journey Stage                        | Focus                                                                                                                                                                              | Status         |
| ----- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| 1     | Noob → Nerd                          | _Environment setup, variables, data types, operators, conditionals, loops, debugging, lists, dictionaries, testing, 2 mini projects_. 📋 **[View Plan](docs/sessions/L1/_Plan.md)** | ✅ **Complete** |
| 2     | Nerd → Novice                        | _Sets, tuples, list comprehensions, functions, error handling, file I/O, modules, 2 mini projects_. 📋 **[View Plan](docs/sessions/L2/_Plan.md)** | ✅ **Complete** |
| 3     | Novice → Object Thinker              | _Core OOP fundamentals: classes, objects, methods, encapsulation._                                                                                                                | 🔄 Future      |
| 4     | Object Thinker → Design Learner      | _OOP design & beginner clean code: simple patterns in classes, basic testing, and refactoring habits._                                                                           | 🔄 Future      |
| 5     | Design Learner → Data Wrangler       | _Files and data formats: CSV, JSON, basic serialization, and file‑driven mini‑projects._                                                                                         | 🔄 Future      |
| 6     | Data Wrangler → DB Beginner          | _Relational databases with SQLite: schema design, CRUD, simple joins, and Python integration._                                                                                   | 🔄 Future      |
| 7     | DB Beginner → Integration Novice     | _Intro to NoSQL concepts and HTTP/JSON APIs; integrating external data sources safely._                                                                                          | 🔄 Future      |
| 8     | Integration Novice → Practitioner    | _Clean code practices, CLI tooling, Git workflows, and systematic testing/debugging._                                                                                            | 🔄 Future      |
| 9     | Practitioner → Patterned Coder       | _Core design patterns and lightweight architecture for console and small apps._                                                                                                  | 🔄 Future      |
| 10    | Patterned Coder → Stdlib Specialist  | _Python Standard Library mastery (os/pathlib, datetime, collections/itertools, logging, etc.)._                                                                                 | 🔄 Future      |
| 11    | Stdlib Specialist → Pro Toolsmith    | _Key third‑party libraries: requests, openpyxl, click/rich, pytest, config tools, and modern Python tooling._                                                                   | 🔄 Future      |
| 12    | Pro Toolsmith → Curious Learner      | _Advanced Python features (asyncio, multiprocessing), performance profiling, packaging, and professional/career practices._                                                      | 🔄 Future      |

---

## 🚧 **Current Implementation Status**

### **✅ Completed & Ready:**

- **📚 Levels 1 & 2 Documentation:** Complete curriculum plans with all 10 sessions each
- **📖 Level 1 & Level 2 Sessions:** Full content with practice files  
  - [**View Level 1 Session 1**](docs/sessions/L1/01_S1.md)  
  - [**View Level 2 Session 1**](docs/sessions/L2/01_S1.md)
- **🚀 Mini Projects:** Calculator (L1 MP1), Profile Generator (L1 MP2), Data Processor (L2 MP1), and Contact Manager (L2 MP2) complete
- **🔧 Development Infrastructure:** Documentation quality automation with CI/CD pipeline

### **🚧 In Development:**

- **📖 Levels 3–9:** Curriculum design and implementation _(planned/under development)_

### **📊 Repository Health:**

- ✅ **Documentation Quality:** Automated linting and link checking
- ✅ **Code Examples:** All Python files tested and working
- ✅ **CI/CD Pipeline:** Automated quality checks on PRs
- ✅ **Educational Structure:** Progressive 30-minute sessions

---

## 🚀 **Quick Start**

**📖 Start:** [`docs/sessions/L1/_Plan.md`](docs/sessions/L1/_Plan.md) - Level 1 complete guide

---

## 🌟 **Why This Journey Works**

### **🎯 Transformation-Focused Approach:**

- ✅ **Mindset Evolution**: Not just syntax learning - actual skill transformation
- ✅ **Bite-Sized Progress**: 30-minute sessions fit any schedule
- ✅ **Project-Driven**: Each level ends with concrete achievements
- ✅ **Growth Mindset**: From Noob to Curious Learner - continuous journey
- ✅ **12-Level Roadmap**: Clear progression with defined milestones
- ✅ **Real-World Skills**: Practical coding that builds confidence

---

## 📞 **Get Support**

**Questions? Issues? Feedback?**

- 🐛 **Report Issues:** Create an issue in this repository
- 💬 **Discussions:** Join discussions in this repository  
- 📧 **Contact:** Swamy's Tech Skills Academy

---

## 📚 **Additional Resources**

- 🌐 **Official Python Tutorial:** [docs.python.org/tutorial](https://docs.python.org/tutorial/)
- 📖 **Python.org Beginner's Guide:** [python.org/about/gettingstarted](https://python.org/about/gettingstarted/)
- 🎥 **Python Installation Video:** Search "Python installation [your OS]"
- 💬 **Community:** r/learnpython, Python Discord, Stack Overflow

---

## 🛠️ **Development & Quality Assurance**

### **Documentation Quality Checks (Local)**

Run Markdown lint against README and all documentation before opening a PR:

```powershell
# From repo root - lint all markdown files
npx --yes markdownlint-cli2 "README.md" "docs/**/*.md" ".github/**/*.md"
```

This uses the repository's `.markdownlint.json` configuration automatically.

**Shortcut on Windows (PowerShell):**

```powershell
# Lint documentation
./scripts/docs-lint.ps1

# Auto-fix formatting issues where possible
./scripts/docs-lint.ps1 -Fix
```

### **Link Validation (Lychee)**

Run link checker to validate all links in documentation:

```powershell
# Validate all links (recommended; matches CI behavior)
docker run --rm -w /input -v "${PWD}:/input" lycheeverse/lychee:latest --config lychee.toml --no-progress README.md docs/**/*.md .github/**/*.md
```

**Shortcut on Windows (PowerShell):**

```powershell
# Validate all links
./scripts/docs-links.ps1

# Extract links only (does not validate)
./scripts/docs-links.ps1 -DumpOnly
```

### **CI/CD Quality Workflow**

GitHub Actions automatically runs documentation quality checks on:

- **Pull Requests** that modify documentation
- **Pushes** to main branch that modify documentation
- **Manual triggers** via GitHub UI

**Manual Trigger:**

1. Open GitHub → Actions → "Docs Quality" workflow
2. Click "Run workflow" (no inputs required)
3. View markdownlint + Lychee results; download the `lychee-report` artifact for details

### **Repository Structure Generation**

Generate current repository structure for documentation:

```powershell
# Generate structure tree and save to file
.\scripts\show-tree.ps1 -Path "." -Depth 4 -OutFile "scripts\repo-structure.txt"

# View structure in terminal
.\scripts\show-tree.ps1 -Path "." -Depth 4
```

---

## 🤝 **Contributing**

We welcome contributions! Whether it's:

- 🐛 Bug fixes
- 📝 Documentation improvements
- 💡 New practice exercises
- 🎯 Additional learning resources

---

## 📞 **About & Get In Touch**

### [ShyvnTech](https://www.linkedin.com/company/shyvntech) & [Swamy's Tech Skills Academy](https://www.linkedin.com/company/swamy-s-tech-skills-academy)

_Ready to become curious about Python? Let's begin your transformation!_ 🚀

**Ready to take your Python skills to the next level? Join our advanced courses and workshops!**

- 🌐 Visit our website for more courses
- 📧 Contact us for custom training programs
- 🏆 Get certified in Python fundamentals
- 👥 Join our learning community

Happy Coding! 🐍✨
