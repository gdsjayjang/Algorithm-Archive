N = int(input())

# Please write your code here.
def func(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return func(n-2) + n

print(func(N))