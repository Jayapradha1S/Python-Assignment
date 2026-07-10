from util import find_max_of_min

n = list(map(int, input().split()))
row = n[0]
col = n[1]

print(find_max_of_min(row))