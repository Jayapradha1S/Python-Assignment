from src.runnerup3.util import secondmax


def test_secondmax_normal(capsys):
    secondmax([2, 3, 6, 6, 5])

    captured = capsys.readouterr()
    assert captured.out.strip() == "5"


def test_secondmax_distinct(capsys):
    secondmax([10, 20, 30, 40])
    captured = capsys.readouterr()
    assert captured.out.strip() == "30"


def test_secondmax_two_elements(capsys):
    secondmax([8, 5])

    captured = capsys.readouterr()
    assert captured.out.strip() == "5"


def test_secondmax_unsorted(capsys):
    secondmax([7, 1, 9, 4])

    captured = capsys.readouterr()
    assert captured.out.strip() == "7"