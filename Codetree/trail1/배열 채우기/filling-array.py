a = list(map(int, input().split()))
arr = [0] * 10

cnt = 0
for i in a:
    if i == 0:
        break
    cnt += 1

print(*a[cnt-1::-1])