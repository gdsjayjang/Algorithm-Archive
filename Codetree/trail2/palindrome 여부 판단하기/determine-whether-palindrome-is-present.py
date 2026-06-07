A = input()

# Please write your code here.
def func(str):
    new_str = str[::-1]

    return new_str

new_str = func(A)

if A == new_str:
    print('Yes')
else:
    print('No')