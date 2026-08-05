n, m = map(int, input().split())

arr = [
    [0 for _ in range(n)] for _ in range(n)
]

for i in range(m):
    row, col = map(int, input().split())
    arr[row-1][col-1] = row * col

for row in arr:
    print(*row)