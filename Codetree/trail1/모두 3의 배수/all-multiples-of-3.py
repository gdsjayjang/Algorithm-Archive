condition = False
for i in range(5):
    a = int(input())
    if a % 3 == 0:
        condition = True
    else:
        condition = False
        break

if condition:
    print(1)
else:
    print(0)
