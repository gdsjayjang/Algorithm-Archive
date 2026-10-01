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


# # others
# # 변수 선언 및 입력
# n = int(input())
# arr = list(map(int, input().split()))


# def insertion_sort():
#     for i in range(1, n):
#         j, key = i - 1, arr[i]
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key


# insertion_sort()

# for elem in arr:
#     print(elem, end=" ")