from src.min_max10.util import find_max_of_min


def test_find_max_of_min_case1(monkeypatch):
    inputs = iter([
        "2 5",
        "3 7"
    ])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    assert find_max_of_min(2) == 3


def test_find_max_of_min_case2(monkeypatch):
    inputs = iter([
        "1 2 3",
        "4 5 6",
        "7 8 9"
    ])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    assert find_max_of_min(3) == 7


def test_find_max_of_min_single_row(monkeypatch):
    inputs = iter([
        "10 20 30"
    ])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    assert find_max_of_min(1) == 10