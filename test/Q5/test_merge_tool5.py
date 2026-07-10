from src.merge_tool5.util import remove_duplicates


def test_remove_duplicates_normal():
    assert remove_duplicates("AABCAAADA") == "ABCD"


def test_remove_duplicates_all_same():
    assert remove_duplicates("AAAAAA") == "A"


def test_remove_duplicates_no_duplicates():
    assert remove_duplicates("ABCDE") == "ABCDE"


def test_remove_duplicates_empty_string():
    assert remove_duplicates("") == ""


def test_remove_duplicates_mixed_characters():
    assert remove_duplicates("1122334455") == "12345"