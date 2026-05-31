inp = input()
arr = inp.split()

A = int(arr[0])
B = int(arr[1])
C = int(arr[2])

sum = A + B + C
avg = sum / len(arr)

print(f'{sum:.0f}')
print(f'{avg:.0f}')
print(f'{sum - avg:.0f}')