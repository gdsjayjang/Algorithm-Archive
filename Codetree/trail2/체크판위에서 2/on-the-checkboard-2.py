R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.
# 1) 좌표에 대한 조건
#     0 < r1 < r2 < R-1
#     0 < c1 < c2 < C-1
# 2) 색에 대한 조건
#      grid[0][0] != grid[r1][c1] and grid[r1][c1] != grid[r2][c2] and grid[r2][c2] != grid[R-1][C-1]

cnt = 0
for r1 in range(1, R-1):
    for c1 in range(1, C-1):
        for r2 in range(r1+1, R-1):
            for c2 in range(c1+1, C-1):
                if grid[0][0] != grid[r1][c1] and grid[r1][c1] != grid[r2][c2] and grid[r2][c2] != grid[R-1][C-1]:
                    cnt += 1
print(cnt)