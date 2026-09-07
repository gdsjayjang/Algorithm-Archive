inp = input()
n = len(inp)

for i in range(n):
    if (ord(inp[i]) >= 65) and (ord(inp[i]) <= 90):
        print(inp[i].lower(), end='')
    elif (ord(inp[i]) >= 97) and (ord(inp[i]) <= 122):
        print(inp[i], end='')
    elif (ord(inp[i]) >= 48) and (ord(inp[i]) <= 57):
        print(inp[i], end='')


# # others
# # 문자열을 입력받습니다.
# string = input()

# # 문자를 하나하나 확인하여 알파벳일 경우 모두 소문자로, 숫자일 경우 그대로 출력합니다.
# for elem in string:
#     if(elem >= 'A' and elem <= 'Z') or (elem >= 'a' and elem <= 'z'):
#         print(elem.lower(), end="")
    
#     if(elem >= '0' and elem <= '9'):
#         print(elem, end="")