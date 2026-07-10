import numpy

def find_max_of_min(row):
    ls = []

    for i in range(0, row):
        a = list(map(int, input().split()))
        ls.append(a)

    arr = numpy.array(ls)
    a = numpy.min(arr, axis=1)
    return max(a)