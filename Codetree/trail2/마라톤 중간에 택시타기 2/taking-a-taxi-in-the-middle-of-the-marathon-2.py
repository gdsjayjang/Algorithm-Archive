n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
def get_distance(i, j):
    return abs(x[i] - x[j]) + abs(y[i] - y[j])

total_dist = 0
for i in range(n - 1):
    total_dist += get_distance(i, i + 1)

max_saved = 0

for i in range(1, n - 1):
    original_path = get_distance(i - 1, i) + get_distance(i, i + 1)
    skip_path = get_distance(i - 1, i + 1)

    saved = original_path - skip_path

    if saved > max_saved:
        max_saved = saved

print(total_dist - max_saved)