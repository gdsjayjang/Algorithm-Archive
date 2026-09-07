inp = input()

res = 0
for i in inp:
    if (i >= '0') and (i <= '9'):
        res += int(i)

print(res)