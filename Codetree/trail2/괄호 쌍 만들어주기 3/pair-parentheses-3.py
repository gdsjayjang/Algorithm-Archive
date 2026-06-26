A = input()

# Please write your code here.
A = list(A)

# '('가 오면 순회하면서 ')'를 찾아야함
# 그리고 그 개수를 카운트.
cnt = 0
length = len(A)
for i in range(length):
    if A[i] == '(':
        for j in A[i+1:]:
            if j == ')':
                cnt += 1
    else:
        continue
print(cnt)