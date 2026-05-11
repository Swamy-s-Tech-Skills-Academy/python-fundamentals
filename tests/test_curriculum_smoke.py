"""Smoke tests that keep pytest green for curriculum scripts.

These tests intentionally validate repository health at a high level without
changing the behavior of lesson scripts.
"""

from __future__ import annotations

import py_compile
from pathlib import Path


def _formal_python_files() -> list[Path]:
    roots = [Path("src/L1"), Path("src/L2")]
    files: list[Path] = []
    for root in roots:
        files.extend(sorted(root.rglob("*.py")))
    return files


def test_formal_curriculum_contains_python_files() -> None:
    files = _formal_python_files()
    assert files, "Expected python files under src/L1 and src/L2"


def test_all_formal_curriculum_files_compile() -> None:
    for file_path in _formal_python_files():
        py_compile.compile(str(file_path), doraise=True)
