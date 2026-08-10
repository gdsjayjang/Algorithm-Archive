a, b = map(int, input().split())
res = str(a + b)

cnt = 0
for i in res:
    if i == '1':
        cnt += 1

print(cnt)