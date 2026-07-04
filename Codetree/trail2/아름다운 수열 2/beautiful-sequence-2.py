N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
# check
sorted_B = sorted(B)

beautiful_count = 0

for i in range(N - M + 1):
    sub_sequence = A[i:i+M]
    
    if sorted(sub_sequence) == sorted_B:
        beautiful_count += 1

print(beautiful_count)