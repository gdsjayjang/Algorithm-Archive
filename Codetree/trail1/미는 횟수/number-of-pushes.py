a = input()
b = input()

n = len(a)
cnt = 1
for i in range(0, n):
    slice = a[:-1]
    init = a[-1]
    a = init+slice
    if a != b:
        cnt += 1
    else:
        break

if cnt < n:
    print(cnt)
else:
    print(-1)