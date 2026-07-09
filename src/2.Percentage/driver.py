from util import average

n = int(input())

dt = {}
for i in range(1, n + 1):
    str2 = input()
    list2 = str2.split()
    key = list2[0]
    list2.remove(key)
    value = list(map(float, list2))
    dt[key] = value

name = input()

average(dt, name)