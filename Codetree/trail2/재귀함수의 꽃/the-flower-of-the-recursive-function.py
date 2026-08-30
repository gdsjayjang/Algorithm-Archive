N = int(input())

# Please write your code here.
def func(n):
    if n <= 0:
        return

    print(n, end=' ')
    func(n-1)
    print(n, end=' ')

func(N)