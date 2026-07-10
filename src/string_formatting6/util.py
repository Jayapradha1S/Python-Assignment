def print_formatted(n):
    # your code goes here
    for i in range(1, n + 1):
        print(f"{i}  {oct(i)[2:]}  {hex(i)[2:].upper()}   {bin(i)[2:]}")