a, b, c = map(int, input().split())

condition = True
for i in range(a, b+1):
    if i % c == 0:
        condition = False

if condition == True:
    print('YES')
else:
    print('NO')