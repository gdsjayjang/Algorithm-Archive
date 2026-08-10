a = list(input())
b = list(input())

arr_a = []
arr_b = []

for i in a:
    if i.isdigit():
        arr_a.append(i)

for j in b:
    if j.isdigit():
        arr_b.append(j)

print(int(''.join(arr_a)) + int(''.join(arr_b)))


# # others
# # 문자열을 구현하여 입력받습니다.
# a = input()
# b = input()

# str1 = ""
# str2 = ""
    
# # a의 정수로 변환 가능한 부분을 다른 문자열로 옮깁니다.
# for elem in a:
#     if ord(elem) <= ord('9') and ord(elem) >= ord('0'):
#         str1 += elem
    
# # b의 정수로 변환 가능한 부분을 다른 문자열로 옮깁니다.
# for elem in b:
#     if ord(elem) <= ord('9') and ord(elem) >= ord('0'):
#         str2 += elem
    
# # 합쳐진 문자열을 숫자로 바꿉니다.
# str1 = int(str1)
# str2 = int(str2)

# # 두 숫자의 합을 출력합니다.
# print(str1 + str2)
