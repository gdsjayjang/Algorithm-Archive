n = int(input())

# 첫
for i in range(n):
    print('  ' * (n-i-1), end='')
    print('@ ' * (i+1), end='')
    print()

for j in range(n-1):
    # j = 0, 1
    # 2*n-3 = 1
    print('@ ' * (n-j-1), end='')
    print()