n = int(input())

idx = 1
for i in range(1, n+1):
    for j in range(1, i+1):
        print(idx, end=' ')
        idx += 1
    print()