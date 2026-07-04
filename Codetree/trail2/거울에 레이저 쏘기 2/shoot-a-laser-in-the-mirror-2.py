n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

# Please write your code here.
# check
# 1. k는 어딘가?
# 1~N : 0
# n+1 ~ 2n : 1
# 2n+1 ~ 3n : 2
# 3n+1 ~ 4n : 3
# (k-1) // 4로 ㅂ판단
# 2. 반사위치를 구해야
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

if k <= n:
    r, c = 0, k - 1
    d = 2
elif k <= 2 * n:
    r, c = k - n - 1, n - 1
    d = 3
elif k <= 3 * n:
    r, c = n - 1, 3 * n - k
    d = 0
else:
    r, c = 4 * n - k, 0
    d = 1

reflect_count = 0

while 0 <= r < n and 0 <= c < n:
    current_mirror = grid[r][c]
    
    if current_mirror == '/':
        d = d ^ 1
        reflect_count += 1
        
    elif current_mirror == '\\':
        d = 3 - d
        reflect_count += 1

    r += dr[d]
    c += dc[d]

print(reflect_count)