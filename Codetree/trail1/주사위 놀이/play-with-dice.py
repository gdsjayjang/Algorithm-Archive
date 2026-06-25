arr = list(map(int, input().split()))
temp_arr = [0] * 6

cnt = 0
for i in arr:
    temp_arr[i-1] += 1

for i in range(len(temp_arr)):
    print(f'{i+1} - {temp_arr[i]}')