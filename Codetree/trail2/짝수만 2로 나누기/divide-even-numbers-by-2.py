n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def func(arr):
    for i in range(n):
        if arr[i] % 2 == 0:
            arr[i] = int(arr[i] / 2)

    print(*arr)

func(arr)