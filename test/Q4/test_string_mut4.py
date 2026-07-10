from src.string_mut4 import mutate_string


def test_mutate_middle_character():
    assert mutate_string("abracadabra", 5, "k") == "abrackdabra"


def test_mutate_first_character():
    assert mutate_string("hello", 0, "H") == "Hello"


def test_mutate_last_character():
    assert mutate_string("python", 5, "s") == "pythos"


def test_single_character_string():
    assert mutate_string("a", 0, "b") == "b"


def test_replace_with_same_character():
    assert mutate_string("apple", 1, "p") == "apple"