n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
arr = [0] * 200

for i in segments:
    for j in range(i[0], i[1]):
        arr[j-1] += 1

print(max(arr))