n, m = map(int, input().split())

# Please write your code here.
arr = [
    [0 for _ in range(m)] for _ in range(n)
]

idx = 0
for j in range(m):
    if j % 2 == 0:
        for i in range(n):
            arr[i][j] = idx
            idx += 1
    else:
        for i in range(n-1,-1,-1):
            arr[i][j] = idx
            idx += 1

for row in arr:
    print(*row, sep=' ')