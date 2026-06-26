n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 초기 범위에서 n-2까지.

cnt = 0
for i in range(n):
    for j in range(n-2):
        cnt = max(cnt, grid[i][j] + grid[i][j+1] + grid[i][j+2])

print(cnt)