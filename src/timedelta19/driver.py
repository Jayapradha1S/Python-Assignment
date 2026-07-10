from util import time_delta

t = int(input())

for _ in range(t):
    t1 = input()
    t2 = input()

    print(time_delta(t1, t2))