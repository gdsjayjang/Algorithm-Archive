n, m = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(m):
    start, end = map(int, input().split())

    print(sum(arr[start-1:end]))