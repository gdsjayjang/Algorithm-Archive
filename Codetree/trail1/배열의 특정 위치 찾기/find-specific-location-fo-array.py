arr = list(map(int, input().split()))

arr1 = arr[1::2]
arr2 = arr[2::3]

print(sum(arr1), f'{sum(arr2)/len(arr2):.1f}')