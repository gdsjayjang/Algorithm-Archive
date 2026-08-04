n = int(input())

arr = [
    list(0 for _ in range(n)) for _ in range(n)
]

cnt = 1
flag = 1
for j in range(n-1, -1, -1):
    if flag == 1:
        for i in range(n-1, -1, -1):    
            arr[i][j] = cnt
            i -= 1
            cnt += 1
    else:
        for i in range(n): 
            arr[i][j] = cnt
            i += 1
            cnt += 1
    flag *= -1

for row in arr:
    print(*row, end='')
    print()