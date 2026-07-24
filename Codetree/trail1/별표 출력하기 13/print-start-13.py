n = int(input())

for i in range(2*n):
    if i % 2 == 0:
        idx = (2*n-i)// 2 #
        # idx should be 5, 4, 3, 2, 1
        for _ in range(idx):
            print('*', end=' ')

    else:
        idx = i // 2 + 1
        for _ in range(idx):
            print('*', end=' ')
    print()
