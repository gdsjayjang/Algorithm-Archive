a, b = map(int, input().split())

# Please write your code here.
def game369(N):
    N_str = str(N)
    if ('3' in N_str) or ('6' in N_str) or ('9' in N_str):
        return 1

def func(N):
    if (N % 3 == 0) or (game369(N) == 1):
        return 1

cnt = 0
for i in range(a, b+1):
    if func(i) == 1:
        cnt += 1

print(cnt)