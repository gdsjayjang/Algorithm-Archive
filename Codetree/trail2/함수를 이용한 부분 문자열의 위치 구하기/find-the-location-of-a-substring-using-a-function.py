a = list(input())
b = list(input())

n1 = len(a)
n2 = len(b)

def func(idx):
    for j in range(n2):
        if a[idx + j] != b[j]:
            return False
    return True

res = -1
for i in range(n1-n2+1): # n1-n2+1 = 7-2+1 = 6
    if func(i):
        res = i
        break

print(res)