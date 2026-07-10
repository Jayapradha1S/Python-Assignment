from src.Question1.util import execute


def test_append():
    lst = []
    execute(lst, "append 5")
    assert lst == [5]


def test_insert():
    lst = [1, 3]
    execute(lst, "insert 1 2")
    assert lst == [1, 2, 3]


def test_remove():
    lst = [1, 2, 3]
    execute(lst, "remove 2")
    assert lst == [1, 3]


def test_pop():
    lst = [1, 2, 3]
    execute(lst, "pop")
    assert lst == [1, 2]


def test_sort():
    lst = [3, 1, 2]
    execute(lst, "sort")
    assert lst == [1, 2, 3]


def test_reverse():
    lst = [1, 2, 3]
    execute(lst, "reverse")
    assert lst == [3, 2, 1]


def test_print(capsys):
    lst = [1, 2, 3]
    execute(lst, "print")

    captured = capsys.readouterr()
    assert captured.out.strip() == "[1, 2, 3]"