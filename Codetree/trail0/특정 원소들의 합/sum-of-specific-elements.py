arr_2d = [list(map(int, input().split())) for _ in range(4)]

sum = 0
for i in range(4):
    for j in range(4):
        if j <= i:
            sum += arr_2d[i][j]

print(sum)

# another
# for i in range(4):
#     for j in range(i + 1):
#         sum_val += arr_2d[i][j]