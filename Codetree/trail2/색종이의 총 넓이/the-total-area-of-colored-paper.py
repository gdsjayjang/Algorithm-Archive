n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
OFFSET = 100
grid = [[0] * 200 for _ in range(200)]

for x, y in points:
    nx = x + OFFSET
    ny = y + OFFSET
    
    for i in range(nx, nx + 8):
        for j in range(ny, ny + 8):
            grid[i][j] = 1

total_area = 0
for i in range(200):
    for j in range(200):
        if grid[i][j] == 1:
            total_area += 1

print(total_area)