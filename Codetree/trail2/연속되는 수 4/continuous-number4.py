n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
cnt, res = 0, 0
for i in range(1, n):
    if arr[i-1] < arr[i]:
        cnt += 1
    else:
        cnt = 0
    res = max(res, cnt)
print(res+1)