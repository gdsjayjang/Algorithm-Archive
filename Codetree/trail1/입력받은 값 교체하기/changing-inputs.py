inp = input()
arr = inp.split()

a = int(arr[0])
b = int(arr[1])

temp = a
a = b
b = temp

print(a, b)