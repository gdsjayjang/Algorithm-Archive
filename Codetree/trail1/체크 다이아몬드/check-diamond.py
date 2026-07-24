n = int(input())

for i in range(n):
    # 공백
    # i=0 -> 2, i=1 -> 1, i=2 -> 0
    for _ in range(n-1, i, -1):
        print(' ', end='')
    # 별
    # i=0 -> 1, i=1 -> 2, i=2 -> 3
    for _ in range(i+1):
        print('*', end=' ')

    print()

for j in range(n-1):
    # 공백
    # j=0 -> 1, j=1 -> 2
    for _ in range(j+1):
        print(' ', end='')
    # 별
    # j=0 -> 2, j=1 -> 1
    for _ in range(n-j, 1, -1):
        print('*', end=' ')
    print()
