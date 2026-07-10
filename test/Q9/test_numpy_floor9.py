from src.numpy_floor9.util import perform_operations


def test_perform_operations(capsys):
    perform_operations([1.1, 2.5, 3.9])

    captured = capsys.readouterr()
    expected = (
        "[ 1.  2.  3.]\n"
        "[ 2.  3.  4.]\n"
        "[ 1.  2.  4.]"
    )
    assert captured.out.strip() == expected


def test_perform_operations_negative(capsys):
    perform_operations([-1.5, -2.1])

    captured = capsys.readouterr()
    expected = (
        "[-2. -3.]\n"
        "[-1. -2.]\n"
        "[-2. -2.]"
    )
    assert captured.out.strip() == expected


def test_perform_operations_integer(capsys):
    perform_operations([1.0, 2.0])

    captured = capsys.readouterr()
    expected = (
        "[ 1.  2.]\n"
        "[ 1.  2.]\n"
        "[ 1.  2.]"
    )
    assert captured.out.strip() == expected