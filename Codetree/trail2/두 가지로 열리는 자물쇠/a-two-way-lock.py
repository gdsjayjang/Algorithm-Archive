N = int(input())
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

# Please write your code here.
# check
def get_distance(x, y, n):
    abs_dist = abs(x - y)
    return min(abs_dist, n - abs_dist)

def is_valid(a, b, c, target_a, target_b, target_c, n):
    return (get_distance(a, target_a, n) <= 2 and
            get_distance(b, target_b, n) <= 2 and
            get_distance(c, target_c, n) <= 2)

success_count = 0

for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if (is_valid(i, j, k, a1, b1, c1, N) or 
                is_valid(i, j, k, a2, b2, c2, N)):
                success_count += 1

print(success_count)