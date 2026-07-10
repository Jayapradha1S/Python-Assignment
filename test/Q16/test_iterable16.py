import pytest
from src.iterable16.util import calculate_probability


def test_sample_case():
    letters = ["a", "a", "c", "d"]
    assert calculate_probability(letters, 2) == pytest.approx(0.8333333333)


def test_all_a():
    letters = ["a", "a", "a"]
    assert calculate_probability(letters, 2) == pytest.approx(1.0)


def test_no_a():
    letters = ["b", "c", "d", "e"]
    assert calculate_probability(letters, 2) == pytest.approx(0.0)


def test_single_selection():
    letters = ["a", "b", "c"]
    assert calculate_probability(letters, 1) == pytest.approx(1 / 3)


def test_select_all():
    letters = ["a", "b", "c", "d"]
    assert calculate_probability(letters, 4) == pytest.approx(1.0)