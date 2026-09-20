N = int(input())

# Please write your code here.
def func(n):
    sum = 0
    if n % 2 == 1:
        for i in range(1, n+1, 2):
            sum += i
    else:
        for i in range(2, n+1, 2):
            sum += i
    return sum

print(func(N))