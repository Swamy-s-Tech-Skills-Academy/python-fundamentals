# 🐍 Python Fundamentals: From clueless to curious

A comprehensive, transformation-focused Python curriculum designed to take you from complete beginner to confident Python programmer through 9 progressive levels.

> **Format:** Each level contains 5 hours of training (10 sessions × 30 minutes) culminating in 2 hands-on mini projects.

---

## 📋 **Repository Structure**

```text
python-fundamentals/
├── 📚 docs/
│   ├── images/                 # Screenshots and educational images
│   │   └── S1/                # Session 1 images (help screenshots, bytecode diagram)
│   └── sessions/
│       └── L1/                # Level 1: Noob → Nerd
│           ├── Plan.md        # Complete Level 1 curriculum plan
│           ├── req.md         # Level 1 requirements and structure
│           └── S1.md          # Session 1: Python Introduction & Environment Setup
├── 💻 src/
│   └── L1/
│       └── S1/                # Session 1 practice files
│           ├── 01_hello.py
│           ├── 02_interactive_hello.py
│           └── bytecode_demo.py
├── 🔧 scripts/               # Development and utility scripts
│   ├── docs-lint.ps1         # Markdown linting script
│   ├── docs-links.ps1        # Link validation script
│   └── show-tree.ps1         # Repository structure generator
├── ⚙️ .github/
│   ├── workflows/
│   │   └── docs-quality.yml  # CI/CD for documentation quality
│   └── copilot-instructions.md
├── 📄 README.md              # This file
├── 📄 LICENSE                # MIT License
└── 📋 Configuration files    # .markdownlint*, lychee.toml, .gitignore
```

---

## 🎯 **The 9-Level Python Journey**

| Level | Journey Stage                  | Focus                                                                                                                                                                              | Status             |
| ----- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| 1     | Noob → Nerd                    | _Environment setup, variables, data types, operators, conditionals, loops, debugging, lists, dictionaries, testing, 2 mini projects_. 📋 **[View Plan](docs/sessions/L1/Plan.md)** | 🟢 **In progress** |
| 2     | Nerd → Novice                  | _Curriculum under development_                                                                                                                                                     | ⏭️ Coming Next     |
| 3     | Novice → Learner               | _Curriculum under development_                                                                                                                                                     | 🔄 Future          |
| 4     | Learner → Beginner             | _Curriculum under development_                                                                                                                                                     | 🔄 Future          |
| 5     | Beginner → Practitioner        | _Curriculum under development_                                                                                                                                                     | 🔄 Future          |
| 6     | Practitioner → Skilled Coder   | _Curriculum under development_                                                                                                                                                     | 🔄 Future          |
| 7     | Skilled Coder → Specialist     | _Curriculum under development_                                                                                                                                                     | 🔄 Future          |
| 8     | Specialist → Professional      | _Curriculum under development_                                                                                                                                                     | 🔄 Future          |
| 9     | Professional → Curious Learner | _Curriculum under development_                                                                                                                                                     | 🔄 Future          |

---

## 🚧 **Current Implementation Status**

### **✅ Completed & Ready:**

- **📚 Level 1 Documentation:** Complete curriculum plan and structure
- **📖 Session 1:** Full content with practice files - [**View Session 1**](docs/sessions/L1/S1.md)
- **🔧 Development Infrastructure:** Documentation quality automation with CI/CD pipeline

### **🚧 In Development:**

- **📖 Session 2:** Variables & Data Types _(in progress)_
- **📖 Sessions 3-10:** Coming soon

### **📊 Repository Health:**

- ✅ **Documentation Quality:** Automated linting and link checking
- ✅ **Code Examples:** All Python files tested and working
- ✅ **CI/CD Pipeline:** Automated quality checks on PRs
- ✅ **Educational Structure:** Progressive 30-minute sessions

---

## 🚀 **Quick Start**

**📖 Start:** [`docs/sessions/L1/Plan.md`](docs/sessions/L1/Plan.md) - Level 1 complete guide

---

## 🌟 **Why This Journey Works**

### **🎯 Transformation-Focused Approach:**

- ✅ **Mindset Evolution**: Not just syntax learning - actual skill transformation
- ✅ **Bite-Sized Progress**: 30-minute sessions fit any schedule
- ✅ **Project-Driven**: Each level ends with concrete achievements
- ✅ **Growth Mindset**: From Noob to Curious Learner - continuous journey
- ✅ **9-Level Roadmap**: Clear progression with defined milestones
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
