arr = [0] * 10
cnt1 = 0
cnt2 = 0

for i in range(10):
    arr[i] = int(input())

for j in arr:
    if j%3 == 0:
        cnt1 += 1
    if j%5 == 0:
        cnt2 += 1

print(cnt1, cnt2)
