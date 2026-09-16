a, b = map(int, input().split())

arr = [0] * 10
arr[0], arr[1] = a, b

for i in range(2, 10):
    arr[i] = (arr[i-2] + arr[i-1]) % 10

print(*arr, sep=' ')
