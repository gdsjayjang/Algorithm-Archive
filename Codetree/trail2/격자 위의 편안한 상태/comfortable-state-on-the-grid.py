n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
# check
grid = [[0] * n for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for r, c in points:
    curr_r = r - 1
    curr_c = c - 1

    grid[curr_r][curr_c] = 1

    colored_neighbors = 0

    for i in range(4):
        nr = curr_r + dr[i]
        nc = curr_c + dc[i]

        if 0 <= nr < n and 0 <= nc < n:
            if grid[nr][nc] == 1:
                colored_neighbors += 1

    if colored_neighbors == 3:
        print(1)
    else:
        print(0)