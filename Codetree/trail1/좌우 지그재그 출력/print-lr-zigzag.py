n = int(input())
idx = 0

for i in range(n):
    if i % 2 == 0:
        for j in range(1, n + 1):
            print(i * n + j, end=' ')
    else:
        for j in range(n, 0, -1):
            print(i * n + j, end=' ')
    print()