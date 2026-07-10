from util import calculate_average

n = int(input())
column = input().split()

avg = calculate_average(n, column)
print(avg)