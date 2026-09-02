start, end = map(int, input().split())

# Please write your code here.
cnt = 0
for i in range(start, end+1):
    res = 0
    for j in range(1, i):
        if i % j == 0:
            res += j
    if res == i:
        cnt += 1
print(cnt)