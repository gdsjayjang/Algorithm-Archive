arr_2d = [
    list(map(int, input().split())) for _ in range(4)
]

cnt = 0
for i in range(4):
    for j in range(4):
        if arr_2d[i][j] % 5 == 0:
            cnt +=1

print(cnt)