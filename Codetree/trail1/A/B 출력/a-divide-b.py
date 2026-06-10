import math
a, b = map(int, input().split())

div = a // b # 몫
res = a % b # 나머지

print(f'{div}.', end='')
for _ in range(20):
    res = res % b
    res = res * 10
    remainder = res // b
    print(remainder, end='')
    
