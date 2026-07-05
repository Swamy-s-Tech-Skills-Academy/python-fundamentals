# Contributing to Python Fundamentals

Thank you for your interest in contributing to Python Fundamentals! This repository is part of Swamy's Tech Skills Academy and aims to provide high-quality, transformative educational content for Python learners.

---

## How to Contribute

We welcome contributions in many forms:

- Bug fixes — fix errors in documentation or code examples
- Documentation improvements — clarify explanations, fix typos, improve examples
- New practice exercises — add original practice problems aligned with session topics
- Additional learning resources — suggest helpful external resources
- Code improvements — enhance practice file examples
- Session content — help develop new sessions (following our strict guidelines)

---

## Before You Start

### Read Our Rules

Before contributing, please familiarize yourself with our content creation rules:

- **[AGENTS.md](AGENTS.md)** — How AI-assisted editors should navigate this repo, ReAct/CoT expectations, and update protocol
- **[skills.md](skills.md)** — Skills pointer and policy index; project skill at `.cursor/skills/python-fundamentals-curriculum/SKILL.md`
- **[Educational Content Rules](.cursor/rules/01_educational-content-rules.mdc)** — Zero-copy policy, transformative workflow, quality standards
- **[Repository Structure](docs/RepositoryStructure.md)** — File naming, directory structure, organization
- **[Quality Assurance](.cursor/rules/03_quality-assurance.mdc)** — Quality checklists and validation requirements

### Key Principles

1. **Python-only scope**: This repository is for the **Python Fundamentals** educational curriculum only
2. **Zero-Copy Policy**: All content must be original and transformative, not copied from other sources
3. **30-Minute Sessions**: Content should fit within focused 30-minute learning segments
4. **Beginner-Friendly**: All content should be accessible to complete beginners
5. **Working Code**: All Python examples must run without errors
6. **Session bucketing**: Default new content to planned/new sessions; do not inject into completed sessions without explicit approval
7. **`src/Working/` hands-off**: Do not edit Working sandbox files unless explicitly requested

---

## Getting Started

### 1. Fork and Clone

```bash
git clone https://github.com/YOUR_USERNAME/python-fundamentals.git
cd python-fundamentals
```

### 2. Create a Branch

```bash
git checkout -b feature/your-contribution-name
```

### 3. Make Your Changes

- Follow the file naming conventions (`01_name.py`, `S1.md`, etc.)
- Use the `L{level}/S{session}/` directory structure
- Ensure all code examples work
- Test your changes locally

### 4. Quality Checks

Before submitting, run our quality checks:

```powershell
ruff check src/L1 src/L2
python -m compileall -q src/L1 src/L2
pytest -q
./scripts/docs-lint.ps1
./scripts/docs-links.ps1
```

If your PR touches Python version policy, keep these files aligned:

- `README.md`
- `AGENTS.md`
- `pyproject.toml`
- `.github/workflows/python-quality.yml`

### 5. Commit and Push

```bash
git add .
git commit -m "Description of your changes"
git push origin feature/your-contribution-name
```

### 6. Open a Pull Request

- Use our [pull request template](.github/pull_request_template.md)
- Provide a clear description of your changes
- Reference any related issues

---

## Content Creation Guidelines

### For New Sessions

1. **Review Prerequisites**: Ensure all prerequisite concepts are covered in earlier sessions
2. **Follow Session Structure**: Use the template from existing sessions
3. **Create Practice Files**: Include working Python examples in `src/L{level}/S{session}/`
4. **Update Plans**: Update `_Plan.md` and Master Plan with new session details
5. **Quality Review**: Complete the quality assurance checklist

### For Code Examples

- All code must run without syntax errors
- Include clear comments explaining concepts
- Use beginner-friendly variable names
- Follow Python style guidelines (PEP 8)
- Add file headers with filename and session reference

### For Documentation

- Use clear, beginner-friendly language
- Include examples and analogies
- Follow markdown standards (see `.cursor/rules/04_markdown-standards.mdc`)
- Validate all file references
- Test all links

---

## Review Process

1. **Automated Checks**: GitHub Actions will run linting and link validation
2. **Content Review**: Maintainers will review for educational quality and compliance
3. **Feedback**: We may request changes to better align with our standards
4. **Approval**: Once approved, your contribution will be merged

---

## Questions?

- **Open an Issue**: Use our [issue templates](.github/ISSUE_TEMPLATE/) for bugs, features, or questions
- **Check Documentation**: Review `.cursor/rules/` for detailed guidelines

---

**Powered by [ShyvnTech](https://www.linkedin.com/company/shyvntech) & [Swamy's Tech Skills Academy](https://www.linkedin.com/company/swamy-s-tech-skills-academy)**
