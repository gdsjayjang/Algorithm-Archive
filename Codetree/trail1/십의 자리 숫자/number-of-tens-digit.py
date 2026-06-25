arr = list(map(int, input().split()))

new_arr = [0] * 10
for i in range(len(arr)):
    digit = arr[i] // 10
    if arr[i] == 0:
        break
    new_arr[digit] = new_arr[digit] + 1

for i in range(1, len(new_arr)):
    print(f'{i} - {new_arr[i]}')