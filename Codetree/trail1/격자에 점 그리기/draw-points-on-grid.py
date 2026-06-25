n, m = map(int, input().split())

grid = [[0] * n for _ in range(n)]

cnt = 1
for i in range(m):
    a, b = map(int, input().split())
    grid[a-1][b-1] = cnt
    cnt += 1

for i in range(n):
    print(*grid[i])