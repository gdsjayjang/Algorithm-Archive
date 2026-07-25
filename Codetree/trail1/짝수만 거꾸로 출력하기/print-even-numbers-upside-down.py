n = int(input())

arr = list(map(int, input().split()))
arr_reverse = arr[::-1]

for i in arr_reverse:
    if i % 2 == 0:
        print(i, end=' ')