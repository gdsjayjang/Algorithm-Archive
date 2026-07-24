# n = int(input())
n = 5
for i in range(2*n):
    if i % 2 ==0:
        # i=0; 1
        # i=2; 2
        # i=4; 3
        # i=6; 4
        # i=8; 5
        idx = int((i+2)/2)
        for j in range(idx):
            print('*', end=' ')
    else:
        # i=1; 5
        # i=3; 4
        # i=5; 3
        # i=7; 2
        # i=9; 1
        idx = int((2*n-i)/2)
        for k in range(idx, -1, -1):
            print('*', end=' ')
    print()