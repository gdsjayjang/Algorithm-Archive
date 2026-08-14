n = int(input())

def func(n):
    n -= 1
    print('HelloWorld')

    if n == 0:
        return

    func(n)

func(n)