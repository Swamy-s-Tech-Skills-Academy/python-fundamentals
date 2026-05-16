"""Targeted behavioral checks for the curriculum mini projects."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]


def load_module(relative_path: str, module_name: str):
    """Load a lesson script from a file path for direct function testing."""
    module_path = REPO_ROOT / relative_path
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    assert spec is not None
    assert spec.loader is not None

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_simple_calculator_rejects_invalid_operation(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    calculator = load_module("src/L1/S5/03_simple_calculator.py", "simple_calculator_invalid_operation")
    answers = iter(["x"])
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(answers))

    assert calculator.main(["03_simple_calculator.py"]) == 0

    output = capsys.readouterr().out
    assert "Invalid operation" in output


def test_simple_calculator_rejects_invalid_number_text(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    calculator = load_module("src/L1/S5/03_simple_calculator.py", "simple_calculator_invalid_number")
    answers = iter(["+", "abc", "5"])
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(answers))

    assert calculator.main(["03_simple_calculator.py"]) == 0

    output = capsys.readouterr().out
    assert "Invalid number input" in output


def test_simple_calculator_blocks_divide_by_zero(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    calculator = load_module("src/L1/S5/03_simple_calculator.py", "simple_calculator_divide_by_zero")
    answers = iter(["/", "10", "0"])
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(answers))

    assert calculator.main(["03_simple_calculator.py"]) == 0

    output = capsys.readouterr().out
    assert "Cannot divide by zero." in output


def test_profile_generator_requires_name(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    profile_generator = load_module("src/L1/S10/profile_generator.py", "profile_generator_required_name")
    monkeypatch.setattr("builtins.input", lambda _prompt="": "")

    assert profile_generator.create_profile() is None

    output = capsys.readouterr().out
    assert "Name cannot be empty" in output


def test_profile_generator_prevents_duplicate_names(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    profile_generator = load_module("src/L1/S10/profile_generator.py", "profile_generator_duplicate_name")
    profile_generator.profiles.append(
        {"name": "Swamy", "age": 30, "city": "Hyderabad", "hobbies": ["Reading"], "goals": ["Teach Python"]}
    )
    monkeypatch.setattr("builtins.input", lambda _prompt="": "swamy")

    assert profile_generator.create_profile() is None

    output = capsys.readouterr().out
    assert "already exists" in output


def test_profile_generator_display_profile_shows_expected_sections(capsys: pytest.CaptureFixture[str]) -> None:
    profile_generator = load_module("src/L1/S10/profile_generator.py", "profile_generator_display_profile")
    profile = {
        "name": "Asha",
        "age": 22,
        "city": "Hyderabad",
        "hobbies": ["Reading", "Drawing"],
        "goals": ["Become a Python developer"],
    }

    profile_generator.display_profile(profile)

    output = capsys.readouterr().out
    assert "PROFILE CARD" in output
    assert "Name:" in output
    assert "🎨 Hobbies" in output
    assert "🎯 Goals" in output
    assert "Asha" in output


def test_data_processor_uses_sample_scores_for_invalid_text(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    data_processor = load_module("src/L2/S5/data_processor.py", "data_processor_invalid_text")
    monkeypatch.setattr("builtins.input", lambda _prompt="": "85, ninety, 92")

    scores = data_processor.get_scores()

    assert scores == [85, 90, 85, 92, 90, 88, 85, 75, 95, 88]
    output = capsys.readouterr().out
    assert "Using sample data instead." in output


def test_data_processor_processes_scores_and_displays_summary(capsys: pytest.CaptureFixture[str]) -> None:
    data_processor = load_module("src/L2/S5/data_processor.py", "data_processor_summary")
    scores = [60, 70, 70, 80]

    unique, tuples, passing, average = data_processor.process_scores(scores)

    assert unique == {60, 70, 80}
    assert sorted(tuples) == [(60, 1), (70, 2), (80, 1)]
    assert sorted(passing) == [70, 80]
    assert average == pytest.approx(70.0)

    data_processor.display_results(scores, unique, tuples, passing, average)
    output = capsys.readouterr().out
    assert "Total unique scores: 3" in output
    assert "Average score: 70.00" in output


def test_contact_manager_requires_name_when_adding_contact(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    contact_manager = load_module("src/L2/S10/contact_manager.py", "contact_manager_required_name")
    monkeypatch.setattr("builtins.input", lambda _prompt="": "")

    contacts = contact_manager.add_contact([])

    assert contacts == []
    output = capsys.readouterr().out
    assert "Name is required" in output


def test_contact_manager_supports_save_search_tag_and_delete_flow(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    contact_manager = load_module("src/L2/S10/contact_manager.py", "contact_manager_flow")
    contacts_file = tmp_path / "contacts.txt"
    contacts = [
        {"name": "Alice", "phone": "555-1111", "email": "alice@example.com", "tags": {"friend", "work"}},
        {"name": "Bob", "phone": "555-2222", "email": "", "tags": {"family"}},
    ]

    assert contact_manager.save_contacts(contacts_file, contacts) is True

    loaded_contacts = contact_manager.load_contacts(contacts_file)
    assert loaded_contacts == [
        {"name": "Alice", "phone": "555-1111", "email": "alice@example.com", "tags": {"friend", "work"}},
        {"name": "Bob", "phone": "555-2222", "email": "", "tags": {"family"}},
    ]

    assert contact_manager.search_contacts(loaded_contacts, "alice") == [loaded_contacts[0]]
    assert contact_manager.get_contacts_by_tag(loaded_contacts, "WORK") == [loaded_contacts[0]]
    assert contact_manager.get_all_tags(loaded_contacts) == {"friend", "work", "family"}

    remaining = contact_manager.delete_contact(loaded_contacts, "Alice")
    assert remaining == [{"name": "Bob", "phone": "555-2222", "email": "", "tags": {"family"}}]

    output = capsys.readouterr().out
    assert "Saved 2 contact(s)" in output
    assert "deleted successfully" in output
