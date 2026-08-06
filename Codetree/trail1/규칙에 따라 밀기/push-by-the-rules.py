inp = list(input())
com = list(input())

for i in range(len(com)):
    if com[i] == 'L':
        temp = inp[0]
        for j in range(len(inp)-1):
            inp[j] = inp[j+1]
        inp[-1] = temp

    elif com[i] == 'R':
        temp = inp[-1]
        for j in range(len(inp)-1, 0, -1):
            inp[j] = inp[j-1]
        inp[0] = temp

print(*inp, sep='')


# # others
# # 문자열을 입력받습니다.
# string = input()
# string2 = input()
    
# # 문자열의 길이를 구합니다.
# leng = len(string)
    
# # 명령 문자열에서 제시하는 대로 행동합니다.
# for elem in string2:
#     if elem == 'L':
#         # 명령 문자열이 L일 때에는 문자열을 왼쪽으로 한 칸 쉬프트합니다.
#         string = string[1:] + string[0]
#     else:
#         # 명령 문자열이 R일 때에는 문자열을 오른쪽으로 한 칸 쉬프트합니다.
#         string = string[leng - 1] + string[:leng - 1]

# # 명령대로 쉬프트된 문자열을 출력합니다.
# print(string)
