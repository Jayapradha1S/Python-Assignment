from src.std12.util import calculate_statistics


def test_calculate_statistics_2x2(monkeypatch, capsys):
    inputs = iter([
        "1 2",
        "3 4"
    ])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    calculate_statistics(2)

    captured = capsys.readouterr()
    expected = (
        "[1.5 3.5]\n"
        "[1. 1.]\n"
        "1.118033988749895"
    )
    assert captured.out.strip() == expected


def test_calculate_statistics_3x2(monkeypatch, capsys):
    inputs = iter([
        "1 2",
        "3 4",
        "5 6"
    ])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    calculate_statistics(3)

    captured = capsys.readouterr()
    expected = (
        "[1.5 3.5 5.5]\n"
        "[2.66666667 2.66666667]\n"
        "1.707825127659933"
    )
    assert captured.out.strip() == expected


def test_calculate_statistics_single_row(monkeypatch, capsys):
    inputs = iter([
        "2 4 6"
    ])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    calculate_statistics(1)

    captured = capsys.readouterr()
    expected = (
        "[4.]\n"
        "[0. 0. 0.]\n"
        "1.632993161855452"
    )
    assert captured.out.strip() == expected