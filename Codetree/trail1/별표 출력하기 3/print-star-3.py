n = int(input())

for i in range(n, 0, -1):
    for j in range(i, n, 1):
        print(' ', end=' ')

    for i in range(i * 2 - 1):
        print('*', end=' ')

    print()