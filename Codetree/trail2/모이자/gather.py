n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
def get_dist_sum(k):
    temp = 0
    # 모든 집 i에 대해서
    for i in range(n):
        temp += abs(k-i) * A[i]
    return temp

res = get_dist_sum(0)

for i in range(1, n):
    res = min(res, get_dist_sum(i))

print(res)