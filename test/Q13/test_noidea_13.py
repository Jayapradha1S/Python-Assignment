from src.noidea13.util import calculate_happiness


def test_calculate_happiness_positive():
    arr = [1, 5, 3]
    A = {3, 1}
    B = {5, 7}

    assert calculate_happiness(arr, A, B) == 1


def test_calculate_happiness_zero():
    arr = [1, 2, 3]
    A = {1}
    B = {3}

    assert calculate_happiness(arr, A, B) == 0


def test_calculate_happiness_negative():
    arr = [4, 5, 6]
    A = {1, 2}
    B = {4, 5, 6}

    assert calculate_happiness(arr, A, B) == -3


def test_calculate_happiness_all_positive():
    arr = [1, 2, 3]
    A = {1, 2, 3}
    B = {4, 5}

    assert calculate_happiness(arr, A, B) == 3


def test_calculate_happiness_empty_array():
    arr = []
    A = {1, 2}
    B = {3, 4}

    assert calculate_happiness(arr, A, B) == 0