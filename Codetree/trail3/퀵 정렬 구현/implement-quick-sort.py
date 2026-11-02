n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

result = quick_sort(arr)
print(*result)