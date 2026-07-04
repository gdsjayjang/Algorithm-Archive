A = input()

# Please write your code here.
# check
open_cnt = 0
ans = 0

for i in range(len(A) - 1):
    if A[i] == '(' and A[i+1] == '(':
        open_cnt += 1

    elif A[i] == ')' and A[i+1] == ')':
        ans += open_cnt

print(ans)