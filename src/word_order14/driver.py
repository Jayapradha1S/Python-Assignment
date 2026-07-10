from util import count_words

n = int(input())

d = count_words(n)

print(len(d))
print(*d.values())