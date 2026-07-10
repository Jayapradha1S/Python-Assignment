import numpy as np

def calculate_statistics(row):
    ls = []

    for i in range(0, row):
        a = list(map(float, input().split()))
        ls.append(a)

    arr = np.array(ls)

    print(np.mean(arr, axis=1))
    print(np.var(arr, axis=0))
    print(np.std(arr, axis=None))