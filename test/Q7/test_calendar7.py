from src.calendar7.util import find_day


def test_find_day_monday():
    assert find_day(8, 5, 2024) == "MONDAY"


def test_find_day_sunday():
    assert find_day(7, 6, 2025) == "SUNDAY"


def test_find_day_friday():
    assert find_day(7, 4, 2025) == "FRIDAY"


def test_find_day_leap_year():
    assert find_day(2, 29, 2024) == "THURSDAY"


def test_find_day_new_year():
    assert find_day(1, 1, 2026) == "THURSDAY"