inp = input()
n = len(inp)
# print(ord('a')) # 97
# print(ord('z')) # 122
# print(ord('A')) # 65
# print(ord('Z')) # 90
# print(ord('0')) # 48
# print(ord('1')) # 49
# print(ord('9')) # 57

# print(inp.lower())
for i in range(n):
    # 대문자
    if (ord(inp[i]) >= 65) and (ord(inp[i]) <= 90):
        print(inp[i].lower(), end='')
    elif (ord(inp[i]) >= 97) and (ord(inp[i]) <= 122):
        print(inp[i], end='')
    elif (ord(inp[i]) >= 48) and (ord(inp[i]) <= 57):
        print(inp[i], end='')
