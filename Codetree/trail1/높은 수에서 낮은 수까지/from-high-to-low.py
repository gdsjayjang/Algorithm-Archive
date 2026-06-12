inp = input()
arr = inp.split()

a = int(arr[0])
b = int(arr[1])

bigger = max(a, b)
smaller = min(a, b)
for i in range(bigger, smaller-1, -1):
    print(i, end=' ')