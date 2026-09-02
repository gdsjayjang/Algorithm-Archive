n = int(input())

for i in range(1, n+1):
    res = i
    for j in range(n):
        print(res, end=' ')
        res += n
    print()