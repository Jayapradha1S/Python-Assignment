from src.textalgn18.util import print_logo


def test_logo_thickness_1(capsys):
    print_logo(1)

    captured = capsys.readouterr()

    assert "H" in captured.out
    assert captured.out.count("H") > 0


def test_logo_thickness_3(capsys):
    print_logo(3)

    captured = capsys.readouterr()

    assert "HHH" in captured.out
    assert captured.out.count("\n") > 0


def test_logo_contains_middle_belt(capsys):
    print_logo(5)

    captured = capsys.readouterr()

    assert "HHHHHHHHHHHHHHHHHHHHHHHHH" in captured.out