arr = list(map(int, input().split()))
cnt = 0

for i in arr:
    if i == 0:
        break
    cnt += 1

print(f'{sum(arr[:cnt])} {sum(arr[:cnt])/cnt:.1f}')