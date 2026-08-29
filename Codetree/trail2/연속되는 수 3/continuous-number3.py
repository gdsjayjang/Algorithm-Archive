N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
cnt = 0
res = 0
for i in range(1, N):
    if arr[i-1] * arr[i] > 0:
        cnt += 1
    else:
        cnt = 0
    res = max(res, cnt)

print(res+1)