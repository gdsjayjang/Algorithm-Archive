n = int(input())

condition = False
for i in range(2, n):
    if n % i == 0:
        condition = True

if condition:
    print('C')
else:
    print('N')