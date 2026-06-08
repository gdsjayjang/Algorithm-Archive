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

# sol1.
# # 가능한 모든 모양을 전부 적어줍니다.
# shapes = [
#     [[1, 1, 0],
#     [1, 0, 0],
#     [0, 0, 0]],

#     [[1, 1, 0],
#     [0, 1, 0],
#     [0, 0, 0]],

#     [[1, 0, 0],
#     [1, 1, 0],
#     [0, 0, 0]],

#     [[0, 1, 0],
#     [1, 1, 0],
#     [0, 0, 0]],

#     [[1, 1, 1],
#     [0, 0, 0],
#     [0, 0, 0]],

#     [[1, 0, 0],
#     [1, 0, 0],
#     [1, 0, 0]],
# ]

# # 주어진 위치에 대하여 가능한 모든 모양을 탐색하며 최대 합을 반환합니다.
# def get_max_sum(x, y):
#     max_sum = 0
#     for i in range(6):
#         is_possible = True
#         sum_of_nums = 0
#         for dx in range(0, 3):
#             for dy in range(0, 3):
#                 if shapes[i][dx][dy] == 0:
#                     continue
#                 if x + dx >= n or y + dy >= m:
#                     is_possible = False
#                 else:
#                     sum_of_nums += grid[x + dx][y + dy]
        
#         if is_possible:
#             max_sum = max(max_sum, sum_of_nums)

#     return max_sum


# ans = 0

# # 격자의 각 위치에 대하여 탐색하여줍니다.
# for i in range(n):
#     for j in range(m):
#         ans = max(ans, get_max_sum(i, j))

# print(ans)