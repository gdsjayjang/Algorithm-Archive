inp = input()
arr = inp.split()

A = int(arr[0])
B = int(arr[1])

if A < B:
    print(B-A)
else:
    print(A-B)