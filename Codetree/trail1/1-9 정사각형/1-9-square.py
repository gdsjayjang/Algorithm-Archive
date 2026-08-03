n = int(input())

cnt = 1
for _ in range(n):
    for _ in range(n):
        if cnt > 9:
            cnt = 1
        print(cnt, end='')
        cnt += 1
    print()