n = int(input())

for i in range(n, 0, -1):
    for k in range(n-i):
        print(' ', end=' ')

    for j in range(i*2 - 1, 0, -1):
        print('*', end=' ')
    
    print()
    

for i in range(n-1):
    for k in range(n-i-2):
        print(' ', end=' ')

    for j in range(3 + (i*2)):
        print('*', end=' ')
    
    print()