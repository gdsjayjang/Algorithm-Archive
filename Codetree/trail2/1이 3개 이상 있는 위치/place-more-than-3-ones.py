n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 상하좌우
dxys = [(-1, 0), (1, 0), (0, -1), (0, 1)]

cnt = 0

def isin(nx, ny):
    return 0<=nx<n and 0<=ny<n

for x in range(n):
    for y in range(n):
        sum = 0
        for dx, dy in dxys:
            nx = x + dx
            ny = y + dy
            # print('x, y, nx, ny', x, y, nx, ny)
            if isin(nx, ny) and grid[nx][ny] == 1:
                sum += 1
        if sum >= 3:
            cnt += 1
print(cnt)