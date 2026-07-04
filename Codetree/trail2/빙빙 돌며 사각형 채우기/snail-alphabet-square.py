n, m = map(int, input().split())

# Please write your code here.
# check
grid = [[''] * m for _ in range(n)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

r, c = 0, 0
dir_idx = 0

for i in range(n * m):
    current_char = chr(65 + (i % 26))
    grid[r][c] = current_char

    nr = r + dr[dir_idx]
    nc = c + dc[dir_idx]
    
    if not (0 <= nr < n and 0 <= nc < m) or grid[nr][nc] != '':
        dir_idx = (dir_idx + 1) % 4
        nr = r + dr[dir_idx]
        nc = c + dc[dir_idx]

    r, c = nr, nc

for row in grid:
    print(*(row))