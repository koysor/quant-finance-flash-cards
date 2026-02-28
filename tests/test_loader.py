"""Test suite for card parsing, math protection, and loading logic."""
import pytest
import os
from pathlib import Path
from app.loader import _protect_math, _parse_card

def test_protect_math_basic():
    """Verify that backslashes in math are doubled."""
    text = r"Let $x = \frac{1}{2}$ and $y = \sigma^2$."
    # _protect_math should double the backslashes in $...$ and $$...$$
    protected = _protect_math(text)
    assert r"Let $x = \\frac{1}{2}$ and $y = \\sigma^2$." == protected

def test_protect_math_display():
    """Verify display math protection."""
    text = "Some math:\n$$\n\\mu = 0\n$$"
    protected = _protect_math(text)
    assert "Some math:\n$$\n\\\\mu = 0\n$$" == protected

def test_parse_card_valid(tmp_path):
    """Test parsing a valid card."""
    card_content = """# Test Card
**Topic:** Calculus
**Tags:** test, math
**Created:** 2026-02-28
**Author:** Test Author

---

## Definition
Testing.
"""
    cards_dir = tmp_path / "cards"
    topic_dir = cards_dir / "calculus"
    topic_dir.mkdir(parents=True)
    card_file = topic_dir / "test-card.md"
    card_file.write_text(card_content, encoding="utf-8")

    import app.loader
    original_cards_dir = app.loader.CARDS_DIR
    app.loader.CARDS_DIR = cards_dir
    try:
        card = _parse_card(card_file)
        assert card["id"] == "calculus/test-card"
        assert card["name"] == "Test Card"
        assert card["topic"] == "Calculus"
        assert card["tags"] == "test,math"
    finally:
        app.loader.CARDS_DIR = original_cards_dir

def test_parse_card_missing_topic(tmp_path):
    """Verify that missing Topic raises ValueError."""
    card_content = """# Test Card
**Tags:** test, math

---

## Definition
Testing.
"""
    cards_dir = tmp_path / "cards"
    topic_dir = cards_dir / "calculus"
    topic_dir.mkdir(parents=True)
    card_file = topic_dir / "bad-card.md"
    card_file.write_text(card_content, encoding="utf-8")
    
    import app.loader
    original_cards_dir = app.loader.CARDS_DIR
    app.loader.CARDS_DIR = cards_dir
    try:
        with pytest.raises(ValueError, match=r"Missing '\*\*Topic:\*\*'"):
            _parse_card(card_file)
    finally:
        app.loader.CARDS_DIR = original_cards_dir

def test_parse_card_missing_tags(tmp_path):
    """Verify that missing Tags raises ValueError."""
    card_content = """# Test Card
**Topic:** Calculus

---

## Definition
Testing.
"""
    cards_dir = tmp_path / "cards"
    topic_dir = cards_dir / "calculus"
    topic_dir.mkdir(parents=True)
    card_file = topic_dir / "bad-card.md"
    card_file.write_text(card_content, encoding="utf-8")
    
    import app.loader
    original_cards_dir = app.loader.CARDS_DIR
    app.loader.CARDS_DIR = cards_dir
    try:
        with pytest.raises(ValueError, match=r"Missing '\*\*Tags:\*\*'"):
            _parse_card(card_file)
    finally:
        app.loader.CARDS_DIR = original_cards_dir
