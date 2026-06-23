n = int(input())
arr = list(map(int, input().split()))

res = [0] * 9

for i in arr:
    res[i-1] += 1

for i in res:
    print(i)

####
# for i in arr:
#     for j in range(1, 10):
#         if i == j:
#             res[j-1] += 1

# for i in res:
#     print(i)