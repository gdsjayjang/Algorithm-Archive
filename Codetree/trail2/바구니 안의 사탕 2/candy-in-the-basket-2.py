N, K = map(int, input().split())
candy = []
pos = []

# for _ in range(N):
#     c, p = map(int, input().split())
#     candy.append(c)
#     pos.append(p)

# Please write your code here.
# check
buckets = []
for _ in range(N):
    c, p = map(int, input().split())
    buckets.append((p, c))

buckets.sort()

max_candies = 0
current_sum = 0
left = 0

for right in range(N):
    current_sum += buckets[right][1]

    while buckets[right][0] - buckets[left][0] > 2 * K:
        current_sum -= buckets[left][1]
        left += 1

    if current_sum > max_candies:
        max_candies = current_sum

print(max_candies)