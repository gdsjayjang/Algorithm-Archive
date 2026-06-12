str = input()
b = input()

leng = len(str)
cnt = 0
for i in range(leng):
    if b == str[i]:
        cnt += 1

print(cnt)