arr = [0] * 10
for i in range(10):
    arr[i] = input()

idx = 0
chr = input()
for i in range(10):
    if arr[i][-1] == chr:
        print(arr[i])
        idx += 1

if idx == 0:
    print('None')