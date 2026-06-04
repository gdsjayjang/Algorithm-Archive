a, b = map(int, input().split())

# Please write your code here.
def func(n):
    ten = n // 10
    one = n % 10

    if n % 2 == 0:
        return False
    if one == 5:
        return False
    if (n % 3 == 0) and (n % 9 != 0):
        return False
    return True

cnt = 0
for i in range(a, b+1):
    if func(i) == True:
        cnt += 1

print(cnt)