# Pull Request

## Description

**What does this PR do?**

- [ ] Bug fix
- [ ] New feature
- [ ] Documentation improvement
- [ ] Code example enhancement
- [ ] New session content
- [ ] Other: `...`

**Brief description of changes:**

---

## Related Issues

Closes #(issue number)

---

## Files Changed

**Documentation:** `docs/...`  
**Practice Code:** `src/...`  
**Configuration:** `.github/...`, `.cursor/...`

---

## Quality Checklist

### Content Quality

- [ ] Zero-copy policy verified (no verbatim text from sources)
- [ ] Content is transformative and original
- [ ] 30-minute session compliance (if applicable)
- [ ] Beginner-friendly language and explanations
- [ ] Session bucketing respected (no new content in completed sessions without approval)

### Technical Quality

- [ ] All Python code runs without errors
- [ ] File naming follows conventions (`01_`, `02_`, `_Plan.md`)
- [ ] Directory structure uses `L{level}/S{session}/` format
- [ ] Python baseline aligned across `README.md`, `AGENTS.md`, `pyproject.toml`, workflows
- [ ] `ruff check src/L1 src/L2` passes
- [ ] `pytest -q` passes (if tests touched)
- [ ] Markdown linting: `./scripts/docs-lint.ps1`
- [ ] Link validation: `./scripts/docs-links.ps1`

### Documentation Updates

- [ ] Updated `_Plan.md` if adding new sessions
- [ ] Updated `docs/RepositoryStructure.md` if layout or inventory changed
- [ ] Updated `AGENTS.md` / `CLAUDE.md` if agent policies changed

---

## Testing

**How was this tested?**

```text
(Describe test results or paste output)
```

---

## Pre-Submission Checklist

- [ ] I've read [CONTRIBUTING.md](../CONTRIBUTING.md)
- [ ] I've reviewed [.cursor/rules/01_educational-content-rules.mdc](../.cursor/rules/01_educational-content-rules.mdc)
- [ ] I've tested my changes locally

---

**Thank you for contributing to Python Fundamentals!**
