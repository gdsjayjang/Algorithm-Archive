inp = input()
arr = inp.split()

a = int(arr[0])
b = int(arr[1])

bigger = a if a > b else b
print(bigger)