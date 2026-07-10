from src.word_order14.util import count_words


def test_count_words_normal(monkeypatch):
    inputs = iter([
        "bcdef",
        "abcdefg",
        "bcde",
        "bcdef"
    ])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    result = count_words(4)

    assert result == {
        "bcdef": 2,
        "abcdefg": 1,
        "bcde": 1
    }


def test_count_words_all_unique(monkeypatch):
    inputs = iter([
        "apple",
        "banana",
        "orange"
    ])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    result = count_words(3)

    assert result == {
        "apple": 1,
        "banana": 1,
        "orange": 1
    }


def test_count_words_all_same(monkeypatch):
    inputs = iter([
        "cat",
        "cat",
        "cat"
    ])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    result = count_words(3)

    assert result == {
        "cat": 3
    }


def test_count_words_empty(monkeypatch):
    inputs = iter([])

    monkeypatch.setattr("builtins.input", lambda: next(inputs))

    result = count_words(0)

    assert result == {}