a, b = map(int, input().split())
n = input()

# Please write your code here.
# a -> 10
res1 = 0
idx = 0
for i in n[::-1]:
    res1 += int(i) * (a**(idx))
    idx += 1

# 10 -> b
res2 = []
while res1 > 0:
    res2.append(res1 % b)
    res1 = res1 // b
if n == '0':
    print(0)
else:
    print(*res2[::-1], sep='')