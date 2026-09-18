inp = input()
len_n = len(inp)
n = int(input())

if len_n > n:
    print(inp[ : len_n-n-1 : -1])
else:
    print(inp[::-1])