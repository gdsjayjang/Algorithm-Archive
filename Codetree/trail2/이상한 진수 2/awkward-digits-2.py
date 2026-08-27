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


# # others
# import sys

# INT_MIN = -sys.maxsize

# # 변수 선언 및 입력
# binary = list(map(int, list(input())))
# length = len(binary)

# # 각 i번째 자릿수를 바꾸었을 때의 십진수 값을 구해줍니다.
# ans = INT_MIN
# for i in range(length):
#     # i번째 자릿수를 바꿉니다.
#     binary[i] = 1 - binary[i]
    
#     # 십진수로 변환합니다.
#     num = 0
#     for j in range(length):
#         num = num * 2 + binary[j]
    
#     ans = max(ans, num)
    
#     # i번째 자릿수를 원래대로 돌려놓습니다.
#     binary[i] = 1 - binary[i]

# # 출력
# print(ans)