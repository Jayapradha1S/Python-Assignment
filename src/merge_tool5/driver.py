from util import remove_duplicates

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        sub = string[i:i+k]
        print(remove_duplicates(sub))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)