n = int(input())

arr = [0] *  n
for i in range(n):
    arr[i] = input()

check = input()

cnt = 0
length = 0
for j in arr:
    if j[0] == check:
        cnt += 1
        length += len(j)

print(cnt, f'{length/cnt:.2f}')