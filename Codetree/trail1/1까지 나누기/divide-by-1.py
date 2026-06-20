n = int(input())

i = 1
cnt = 0
while True:
    n = n // i
    cnt += 1
    if n <= 1:
        break
    i += 1

print(cnt)