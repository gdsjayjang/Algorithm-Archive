n = int(input())

# Please write your code here.
def func(N):
    ten = N // 10
    one = N % 10
    sum = ten + one

    if (N % 2 == 0) and (sum % 5 == 0):
        print('Yes')
    else:
        print('No')

func(n)