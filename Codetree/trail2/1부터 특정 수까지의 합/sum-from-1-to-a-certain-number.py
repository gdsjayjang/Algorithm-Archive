n = int(input())

# Please write your code here.
def func(int):
    sum = 0
    for i in range(1, int+1):
        sum += i
    res = sum // 10

    return res

print(func(n))