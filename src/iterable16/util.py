from itertools import combinations


def calculate_probability(letters, k):
    total = 0
    count = 0

    for comb in combinations(range(len(letters)), k):
        total += 1
        if any(letters[i] == "a" for i in comb):
            count += 1

    return count / total