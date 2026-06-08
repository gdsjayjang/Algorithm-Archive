cnt = 0
str = []

while True:
    inp = input()
    cnt += 1
    if inp != '0':
        str.append(inp)
    else:
        cnt -= 1
        break

print(cnt)
for i in range(0, len(str), 2):
    print(str[i])