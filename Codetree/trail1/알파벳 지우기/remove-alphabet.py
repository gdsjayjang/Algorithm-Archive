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

print(int(''.join(arr_a)) + int(''.join(arr_b)))