n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def func(n):
    if n == 1:
        return arr[0]

    return max(arr[n-1], func(n-1))

print(func(n))