n = int(input())

arr = [
    [0 for _ in range(n)] for _ in range(n)
]

# 1열 초기화
for i in range(n):
    arr[i][0] = 1

# 파스칼의 삼각형
for i in range(1, n):
    for j in range(1, n):
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

# 출력
for i in range(n):
    for j in range(i+1):
        print(arr[i][j], end=' ')
    print()