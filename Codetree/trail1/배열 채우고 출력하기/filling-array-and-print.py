arr = list(input().split())

for i in range(len(arr), 0, -1):
    print(arr[i-1], end='')