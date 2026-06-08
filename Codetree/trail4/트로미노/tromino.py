n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# max_m 부터
# ㅡ 모양
max_m_m = 0
for i in range(n):
    for j in range(m-2):
        temp_m_m = grid[i][j] + grid[i][j+1] + grid[i][j+2]
        if max_m_m < temp_m_m:
            max_m_m = temp_m_m
# max_m 부터
# ㅣ 모양
max_m_l = 0
for j in range(m):
    for i in range(n-2):
        temp_m_l = grid[i][j] + grid[i+1][j] + grid[i+2][j]
        if max_m_l < temp_m_l:
            max_m_l = temp_m_l
max_r_s = 0
# ㄴ 모양
for i in range(n-1):
    for j in range(m-1):
        temp_r_s = grid[i][j] + grid[i+1][j] + grid[i+1][j+1]
        if max_r_s < temp_r_s:
            max_r_s = temp_r_s
max_r_r = 0
# ㄱ 모양
for i in range(n-1):
    for j in range(m-1):
        temp_r_r = grid[i][j] + grid[i][j+1] + grid[i+1][j+1]
        if max_r_r < temp_r_r:
            max_r_r = temp_r_r
max_r_rs = 0
# ㄴ 뒤집은 모양
for i in range(n-1):
    for j in range(m-1):
        temp_r_rs = grid[i][j+1] + grid[i+1][j+1] + grid[i+1][j]
        if max_r_rs < temp_r_rs:
            max_r_rs = temp_r_rs    
max_r_rr = 0
# ㄱ 뒤집은 모양
for i in range(n-1):
    for j in range(m-1):
        temp_r_rr = grid[i][j] + grid[i][j+1] + grid[i+1][j]
        if max_r_rr < temp_r_rr:
            max_r_rr = temp_r_rr

print(max(max_m_m, max_m_l, max_r_r, max_r_s, max_r_rr, max_r_rs))