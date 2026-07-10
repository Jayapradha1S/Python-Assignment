def count_words(n):
    d = {}

    for i in range(n):
        word = input()

        if word in d:
            d[word] += 1
        else:
            d[word] = 1

    return d