n = int(input())

arr = [
    map(int, input().split()) for _ in range(n)
]

cnt = 0
arr_mean = [0] * n
for i in range(n):
    arr_mean[i] = sum(arr[i]) / 4
    if arr_mean[i] >= 60:
        cnt += 1
        print('pass')
    else:
        print('fail')

print(cnt)