def secondmax(ls):
    max1 = 0
    smax = 0

    for i in ls:
        if i > max1:
            max1 = i
        elif max1 > i and i > smax:
            smax = i

    print(smax)