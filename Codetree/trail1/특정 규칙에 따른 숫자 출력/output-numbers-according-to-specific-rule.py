n = int(input())

num = 1
for i in range(n):
    for _ in range(i):
        print(' ', end=' ')
    
    for _ in range(n-i):
        print(num, end=' ')
        num += 1
    
    if num > 9:
        num = 1
    print()