from util import can_stack

t = int(input())

for i in range(t):
    n = int(input())
    cubes = list(map(int, input().split()))

    if can_stack(cubes):
        print("Yes")
    else:
        print("No")