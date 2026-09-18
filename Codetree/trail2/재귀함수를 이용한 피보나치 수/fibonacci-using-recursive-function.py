N = int(input())

# Please write your code here.
def func(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    
    return func(n-2) + func(n-1)

print(func(N))