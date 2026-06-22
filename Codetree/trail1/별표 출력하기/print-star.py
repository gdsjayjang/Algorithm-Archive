n = int(input())

for i in range(n):
    flag = i
    for j in range(flag+1):
        print('*', end=' ')
    print()

for i in range(n-1, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()