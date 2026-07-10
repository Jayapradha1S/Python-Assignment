from util import calculate_happiness

n, m = map(int, input().split())

arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(calculate_happiness(arr, A, B))