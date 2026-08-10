n = int(input())

res = 0
for i in range(n):
    res += int(input())

res = str(res)
new = res[1:] + res[0]
print(new)