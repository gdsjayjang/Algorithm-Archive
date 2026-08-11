N = int(input())
arr_2d = [[0 for _ in range(N)] for _ in range(N)]

for j in range(N):
    if j % 2 != 0:
        num = 1
        for i in range(N-1, -1, -1):
            arr_2d[i][j] = num
            num += 1
    if j % 2 == 0:
        num = 1
        for i in range(N):
            arr_2d[i][j] = num
            num += 1

for i in range(N):
    for j in range(N):
        print(arr_2d[i][j], end='')

    print()