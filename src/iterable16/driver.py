from util import calculate_probability

n = int(input())
letters = input().split()
k = int(input())

result = calculate_probability(letters, k)
print(f"{result:.4f}")