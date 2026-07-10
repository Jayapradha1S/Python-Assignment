from src.string_formatting6.util import print_formatted


def test_print_formatted_1(capsys):
    print_formatted(1)

    captured = capsys.readouterr()
    expected = "1  1  1   1"
    assert captured.out.strip() == expected


def test_print_formatted_2(capsys):
    print_formatted(2)

    captured = capsys.readouterr()
    expected = (
        "1  1  1   1\n"
        "2  2  2   10"
    )
    assert captured.out.strip() == expected


def test_print_formatted_3(capsys):
    print_formatted(3)

    captured = capsys.readouterr()
    expected = (
        "1  1  1   1\n"
        "2  2  2   10\n"
        "3  3  3   11"
    )
    assert captured.out.strip() == expected