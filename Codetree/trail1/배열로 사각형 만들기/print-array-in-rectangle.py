n =5

arr = [
    [0 for _ in range(n)] for _ in range(n)
]

# 1행 초기화
for i in range(n):
    arr[0][i] = 1

# 1열 초기화
for i in range(n):
    arr[i][0] = 1

# 값 채우기
for i in range(1, n):
    for j in range(1, n):
        arr[i][j] = arr[i-1][j] + arr[i][j-1]

for row in arr:
    print(*row, sep=' ')