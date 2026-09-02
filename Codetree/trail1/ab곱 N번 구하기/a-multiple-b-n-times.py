n = int(input())

for _ in range(n):
    res = 1
    a, b = map(int, input().split())
    for i in range(a, b+1):
        res *= i
    print(res)