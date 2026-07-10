from src.namedtuple8.util import calculate_average

def test_calculate_average_three_students(monkeypatch):
    inputs = iter([
        "1 John 78",
        "2 Alice 90",
        "3 Bob 87"
    ])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    result = calculate_average(3, ["ID", "NAME", "MARKS"])
    assert result == 85.0


def test_calculate_average_single_student(monkeypatch):
    inputs = iter([
        "1 Tom 100"
    ])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    result = calculate_average(1, ["ID", "NAME", "MARKS"])
    assert result == 100.0


def test_calculate_average_two_students(monkeypatch):
    inputs = iter([
        "1 Sam 80",
        "2 Ram 60"
    ])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    result = calculate_average(2, ["ID", "NAME", "MARKS"])
    assert result == 70.0