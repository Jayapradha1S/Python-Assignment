from src.Percentage2.util import average


def test_average_student1(capsys):
    dt = {
        "Krishna": [67.0, 68.0, 69.0],
        "Arjun": [70.0, 98.0, 63.0],
        "Malika": [52.0, 56.0, 60.0]
    }

    average(dt, "Krishna")

    captured = capsys.readouterr()
    assert captured.out.strip() == "68.00"


def test_average_student2(capsys):
    dt = {
        "Jay": [80.0, 90.0, 100.0]
    }

    average(dt, "Jay")

    captured = capsys.readouterr()
    assert captured.out.strip() == "90.00"


def test_average_single_mark(capsys):
    dt = {
        "Ram": [75.0]
    }

    average(dt, "Ram")

    captured = capsys.readouterr()
    assert captured.out.strip() == "75.00"


def test_average_decimal_marks(capsys):
    dt = {
        "Alice": [89.5, 90.5]
    }

    average(dt, "Alice")

    captured = capsys.readouterr()
    assert captured.out.strip() == "90.00"


def test_name_not_found(capsys):
    dt = {
        "Tom": [60.0, 70.0]
    }

    average(dt, "Jerry")

    captured = capsys.readouterr()
    assert captured.out.strip() == ""