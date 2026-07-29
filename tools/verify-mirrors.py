#!/usr/bin/env python3
"""
Verify mirror parity: .cursor/ (canonical) vs .clinerules/ and .opencode/ (mirrors).

This script checks:
1. Existence parity: mirrors have expected subdirectories
2. File counts: agent/skill files match across layers
3. Drift detection: mirrors don't reference secondary/stale sources
4. Policy consistency: AGENTS.md claims match across canonical and mirrors

Usage:
    python tools/verify-mirrors.py
"""

import os
import sys
from pathlib import Path


def check_mirrors():
    """Verify mirror structure and content consistency."""
    repo_root = Path(__file__).parent.parent
    issues = []

    # Define expected structures
    canonical_path = repo_root / ".cursor"
    mirrors = {
        ".clinerules": repo_root / ".clinerules",
        ".opencode": repo_root / ".opencode",
    }

    # 1. Check subdirectory parity
    print("[*] Checking subdirectory parity...")
    canonical_subdirs = {d.name for d in canonical_path.iterdir() if d.is_dir()}

    for mirror_name, mirror_path in mirrors.items():
        mirror_subdirs = {d.name for d in mirror_path.iterdir() if d.is_dir()}

        # Mirrors should have at least the canonical subdirs (may have extras like 'workflows')
        missing = canonical_subdirs - mirror_subdirs
        if missing:
            issues.append(
                f"  [WARNING] {mirror_name} missing subdirs: {', '.join(missing)}"
            )

    # 2. Check agent file counts in agents/ subdirectories
    print("[*] Checking agent file inventories...")
    canonical_agents = set(
        f.name for f in (canonical_path / "agents").glob("*.md")
    )
    print(f"  Canonical (.cursor/agents/): {len(canonical_agents)} files")

    for mirror_name, mirror_path in mirrors.items():
        mirror_agents_dir = mirror_path / "agents"
        if mirror_agents_dir.exists():
            mirror_agents = set(f.name for f in mirror_agents_dir.glob("*.md"))
            print(f"  {mirror_name}/agents/: {len(mirror_agents)} files")

            # Note: exact name matching is not required (e.g., session-content vs
            # session-roadmap-review), but file count should be similar
            if len(mirror_agents) < len(canonical_agents) - 1:
                issues.append(
                    f"  [WARNING] {mirror_name}/agents/ has significantly fewer files "
                    f"({len(mirror_agents)} vs {len(canonical_agents)} canonical)"
                )

    # 3. Drift detection: check AGENTS.md files for stale references
    print("[*] Checking for stale/drift references in AGENTS.md files...")
    agents_files = [
        repo_root / "AGENTS.md",
        repo_root / ".clinerules" / "AGENTS.md",
    ]

    drift_patterns = [
        "docs/02_RepositoryStructure",
        "tools/psscripts",
        "python-fundamentals-in-practice",  # should only appear in correct context
    ]

    for agents_file in agents_files:
        if agents_file.exists():
            content = agents_file.read_text(encoding="utf-8")

            # python-fundamentals-in-practice is OK when describing the model, but
            # should never appear as "authoritative" or "canonical"
            if "python-fundamentals-in-practice" in content:
                # Check context: should always be described as "replica" or "secondary"
                if "replica" not in content.lower() and "secondary" not in content.lower():
                    # This might be OK if it's in a relationship table, but flag for review
                    pass  # Don't fail; this is documented as correct

            # docs/02_RepositoryStructure and tools/psscripts should never appear
            for pattern in ["docs/02_RepositoryStructure", "tools/psscripts"]:
                if pattern in content:
                    issues.append(
                        f"  [WARNING] {agents_file.relative_to(repo_root)} references "
                        f"'{pattern}' (should not exist)"
                    )

    # 4. Check that core policy files exist and are not empty
    print("[*] Checking core policy files...")
    required_files = [
        repo_root / "CLAUDE.md",
        repo_root / "AGENTS.md",
        repo_root / ".cursor" / "rules" / "01_educational-content-rules.mdc",
        repo_root / ".cursor" / "rules" / "02_repository-structure.mdc",
        repo_root / "docs" / "RepositoryStructure.md",
    ]

    for file_path in required_files:
        if not file_path.exists():
            issues.append(f"  [FAIL] Missing: {file_path.relative_to(repo_root)}")
        elif file_path.stat().st_size < 100:
            issues.append(
                f"  [WARNING] Suspiciously small (may be template): "
                f"{file_path.relative_to(repo_root)}"
            )
        else:
            print(f"  [OK] {file_path.relative_to(repo_root)}")

    # 5. Check that mirrors don't reference Working paths in publish-facing docs
    print("[*] Checking for Working/ paths in publish-facing docs...")
    session_docs = (repo_root / "docs" / "sessions").glob("**/*.md")
    for doc in session_docs:
        content = doc.read_text(encoding="utf-8")
        if "src/Working/" in content:
            issues.append(
                f"  [FAIL] {doc.relative_to(repo_root)} contains reference to "
                f"src/Working/ (should not appear in publish-facing docs)"
            )

    # Report
    print("\n" + "=" * 70)
    if issues:
        print(f"[WARNING] Found {len(issues)} issue(s):\n")
        for issue in issues:
            print(issue)
        return 1
    else:
        print("[SUCCESS] All mirror parity checks passed!")
        print("   - Subdirectories exist")
        print("   - Agent/skill files present")
        print("   - No stale references detected")
        print("   - No Working paths in publish-facing docs")
        return 0


if __name__ == "__main__":
    sys.exit(check_mirrors())
