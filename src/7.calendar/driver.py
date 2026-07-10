from util import find_day

month, date, year = list(map(int, input().split()))

print(find_day(month, date, year))