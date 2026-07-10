import numpy

numpy.set_printoptions(legacy='1.13')

def perform_operations(ls):
    ar = numpy.array(ls)
    print(numpy.floor(ar))
    print(numpy.ceil(ar))
    print(numpy.rint(ar))