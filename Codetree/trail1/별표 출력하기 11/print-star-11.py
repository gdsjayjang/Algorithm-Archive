n = int(input())

for i in range(2*n+1): # i=0,1,2,...,6
    for j in range(2*n+1):
        if i % 2 == 0 or j % 2 == 0:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()