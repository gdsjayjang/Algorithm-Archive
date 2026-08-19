N = input()

# Please write your code here.
n = len(N)
arr = []
for i in N:
    arr.append(i)
arr = arr[::-1]

# 십진수 변환
res = 0
k = 0
for i in arr:
    res += int(i) * (2**k)
    k+= 1

res = res * 17
arr2 = []
while res > 0:
    arr2.append(res % 2)
    res = res // 2

print(*arr2[::-1], sep='')