a, b = map(int, input().split())

# Please write your code here.
def func(a, b):
    res = a
    for i in range(b-1):
        res *= a
    return res

print(func(a, b))