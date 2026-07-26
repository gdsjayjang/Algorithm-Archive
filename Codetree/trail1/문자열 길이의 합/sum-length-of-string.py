n = int(input())

sum = 0
cnt = 0
for _ in range(n):
    temp = input()
    sum += len(temp)
    if temp[0] == 'a':
        cnt += 1

print(sum, cnt)