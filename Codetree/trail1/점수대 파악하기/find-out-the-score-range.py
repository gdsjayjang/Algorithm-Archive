arr = list(map(int, input().split()))
new_arr = [0] * 11

for i in range(len(arr)):
    digit = arr[i] // 10
    if arr[i] == 0:
        break
    new_arr[digit] = new_arr[digit] + 1

for i in range(len(new_arr)-1, 0, -1):
    print(f'{i*1}0 - {new_arr[i]}')