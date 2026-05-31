import math

inp = input()
arr = inp.split()

A = int(arr[0])
B = int(arr[1])
C = int(arr[2])

sum = A + B + C
avg = math.floor(sum / len(arr))

print(sum)
print(avg)