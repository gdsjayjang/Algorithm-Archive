a, b = map(int, input().split())

arr = []
while a >= 1:
    mod = a % b
    a = a // b # 몫
    arr.append(mod)

dic = {}
for i in arr:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

res = 0
appear = list(dic.values())
for i in appear:
    res += i**2
    
print(res)