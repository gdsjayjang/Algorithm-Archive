a, b = map(int, input().split())

condition = False
for i in range(a, b+1, 1):
    if (1920 % i == 0) and (2880 % i == 0):
        condition = True

if condition:
    print(1)
else:
    print(0)