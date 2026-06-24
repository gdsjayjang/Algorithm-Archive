n = int(input())

# Please write your code here.
arr = []
if n == 0:
    print(0)
else:
    while n != 1:
        arr.append(n % 2)
        n = n // 2

    arr.append(1)
    print(*arr[::-1], sep='')