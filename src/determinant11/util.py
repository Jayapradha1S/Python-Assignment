import numpy

def find_determinant(n):
    ls = []

    for i in range(n):
        inp = list(map(float, input().split()))
        ls.append(inp)

    arr = numpy.array(ls)
    return numpy.linalg.det(arr)