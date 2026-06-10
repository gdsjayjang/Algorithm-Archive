import math
a, b = map(int, input().split())

q = a // b # 몫
r = a % b # 나머지

print(f'{q}.', end='')
for _ in range(20):
    r = r % b
    r = r * 10
    remainder = r // b
    print(remainder, end='')
    
