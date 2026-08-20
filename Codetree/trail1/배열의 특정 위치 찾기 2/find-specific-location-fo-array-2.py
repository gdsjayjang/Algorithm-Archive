arr = list(map(int, input().split()))

oddsum = sum(arr[1::2])
evensum = sum(arr[::2])

res = abs(oddsum-evensum)
print(res)