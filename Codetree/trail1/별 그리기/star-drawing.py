n = int(input())

# Please write your code here.
for i in range(n):
    # 공백 2 1 0
    print(' ' * (n-i-1), end='')

    # 별표 1 3 5 7
    print('*' * (2*i+1), end='')

    print()

# j = 0, 1
for j in range(n-1):
    # 공백 1 2
    print(' ' * (j+1), end='')

    # 별표 3 1
    print('*' * (2*(n-j-1)-1), end='')

    print()
