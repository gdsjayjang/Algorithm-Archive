a, b, c = map(int, input().split())

# Please write your code here.
n = a * b * c

def func(n):
    result = 0

    if n == 0:
        return result

    div = n % 10
    mod = n // 10

    result += div

    return result + func(mod)

print(func(n))


# # others
# n = a * b * c

# def func(n):
#     if n == 0:
#         return 0

#     mod = n % 10
#     div = n // 10
#     return mod + func(div)

# print(func(n))