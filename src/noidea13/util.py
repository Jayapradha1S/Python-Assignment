def calculate_happiness(arr, A, B):
    happiness = 0

    for i in arr:
        if i in A:
            happiness += 1
        elif i in B:
            happiness -= 1

    return happiness