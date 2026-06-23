n, m = map(int, input().split())

arr = [
    [0] * n for _ in range(n)
]

for _ in range(m):
    inp = list(map(int, input().split()))

    for i in inp:
        arr[inp[0]-1][inp[1]-1] = 1

for i in arr:
    print(*i)