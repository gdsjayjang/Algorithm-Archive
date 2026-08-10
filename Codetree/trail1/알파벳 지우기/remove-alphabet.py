a = list(input())
b = list(input())

arr_a = []
arr_b = []

for i in a:
    if i.isdigit():
        arr_a.append(i)

for j in b:
    if j.isdigit():
        arr_b.append(j)

print(''.join(arr_a) + ''.join(arr_b))