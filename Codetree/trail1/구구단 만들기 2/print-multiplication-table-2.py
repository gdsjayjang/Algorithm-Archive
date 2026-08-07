a, b = map(int, input().split())
arr = [2, 4, 6, 8]

for j in arr:
    for i in range(b, a-1, -1):
        if i != a:
            print(f'{i} * {j} = {i*j} /', end=' ')
        else:
            print(f'{i} * {j} = {i*j}')