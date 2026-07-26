str = input()
str = list(str)
str.pop(1)
str.pop(-2)

print(*str, sep='')


# # others
# # 문자열을 입력받습니다.
# string = input()

# # 문자열의 길이를 구합니다.
# leng = len(string)

# # pop 함수를 사용하기 위해 문자열을 list로 전환합니다.
# arr = list(string)
    
# # 앞에서 2번째 원소를 제거합니다. (이때 문자열의 길이가 1 감소하는것을 반드시 기억합니다)
# arr.pop(1)
# leng -= 1
    
# # 뒤에서 2번째 원소를 제거합니다.
# arr.pop(leng - 2)
# leng -= 1

# # list를 문자열로 변환합니다.
# string = ''.join(arr)
    
# # 앞에서 2번째, 뒤에서 2번째 원소가 제거된 문자열을 출력합니다.
# print(string)