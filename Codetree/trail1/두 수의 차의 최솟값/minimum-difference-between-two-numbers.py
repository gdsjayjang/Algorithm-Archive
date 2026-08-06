n = int(input())
arr = list(map(int, input().split()))

res = 100
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        diff = abs(arr[i] - arr[j])
        if res > diff:
            res = diff

print(res)
