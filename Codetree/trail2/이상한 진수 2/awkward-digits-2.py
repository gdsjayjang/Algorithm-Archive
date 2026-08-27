a = input()

# Please write your code here.
arr = list(a)
n_arr = len(arr)

arr_copy = arr.copy()
ten_max = 0

# 뒤집기
for i in range(n_arr):
    if arr_copy[i] == '0':
        arr_copy[i] = '1'
    else:
        arr_copy[i] = '0'

    # 십진수로 변환
    reverse_arr = arr_copy[::-1].copy()
    ten = 0
    for k in range(n_arr):
        ten += int(reverse_arr[k]) * (2**k)
    if ten_max < ten:
        ten_max = ten

    # arr 초기화
    arr_copy = arr.copy()
print(ten_max)