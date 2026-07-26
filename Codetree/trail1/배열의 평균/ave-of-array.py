arr = [
    list(map(int, input().split())) for _ in range(2)
]


ga = len(arr) # 행
se = len(arr[0]) # 열

# 가로 평균
for i in range(ga):
    print(f'{sum(arr[i])/se:.1f}', end=' ')
print()

# 세로 평균
for j in range(se):
    temp = 0
    for i in range(ga):
        temp += arr[i][j]
    print(f'{temp/ga:.1f}', end=' ')
print()

# 전체 평균
result = 0
for i in arr:
    result += sum(i)
print(result/(ga*se))