n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
n_arr = len(arr)
res = 0
diff = 0
for i in range(n_arr):
    if n_arr == 1:
        res = 1
        break
    if i == 0 or arr[i] == arr[i-1]:
        diff += 1
    if res < diff:
        res = diff+1
        diff = 0

print(res)