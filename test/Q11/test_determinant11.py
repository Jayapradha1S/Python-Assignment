import pytest
from src.determinant11.util import find_determinant


def test_find_determinant_2x2(monkeypatch):
    inputs = iter([
        "1 2",
        "3 4"
    ])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    assert find_determinant(2) == pytest.approx(-2.0)


def test_find_determinant_identity_matrix(monkeypatch):
    inputs = iter([
        "1 0 0",
        "0 1 0",
        "0 0 1"
    ])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    assert find_determinant(3) == pytest.approx(1.0)


def test_find_determinant_diagonal_matrix(monkeypatch):
    inputs = iter([
        "2 0",
        "0 5"
    ])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    assert find_determinant(2) == pytest.approx(10.0)