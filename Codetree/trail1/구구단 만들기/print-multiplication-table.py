a, b = map(int, input().split())

arr = []
for i in range(b, a-1, -1):
    if i % 2 == 0:
        arr.append(i)

# 구구단 출력
for i in range(1, 10):
    for j in arr:
        print(f'{j} * {i} = {j*i}', end='')
        if j != arr[-1]:
            print(' / ', end='')
    print()