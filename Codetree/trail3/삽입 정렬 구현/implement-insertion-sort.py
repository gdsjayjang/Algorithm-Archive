n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(1, n):
    for j in range(0, i):
        temp = arr[i]
        if arr[j] > arr[i]:
            arr[i] = arr[j]
            arr[j] = temp

print(*arr, sep=' ')
