n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.
dxy = [
    (0, 1), (1, 0), (0, -1), (-1, 0)
]
x, y = 0, 0
d = 0
arr[0][0] = 1

def isin(nx, ny):
    return (0 <= nx < n) and (0 <= ny < m)

for cnt in range(2, n*m + 1):
    nx = x + dxy[d][0]
    ny = y + dxy[d][1]

    if not isin(nx, ny) or arr[nx][ny] != 0:
        # 90도 회전 (d+1)
        d = (d + 1) % 4
    
    x += dxy[d][0]
    y += dxy[d][1]

    arr[x][y] = cnt

for row in arr:
    print(*row)