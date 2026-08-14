n = int(input())
arr = list(map(int, input().split()))

def func(arr):
    length = len(arr)
    for i in range(length):
        arr[i] = abs(arr[i])

    print(*arr)

func(arr)