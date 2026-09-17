n = int(input())
arr = [0] * 100
arr[0] = 1
arr[1] = n

for i in range(0,100):
    arr[i+2] = arr[i] + arr[i+1]
    print(arr[i], end=' ')
    if arr[i] > 100:
        break