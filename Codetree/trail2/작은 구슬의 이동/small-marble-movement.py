n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.

# 1. n x n 그리드
# 2. t초
# 3. 초기 값 r, c 그리드이므로 -1씩 필요
# 4. d: 초기 바라보는 방향 u , d, r, l
# 5. t초 후?

dir_str_to_sum = {
    'U': 0,
    'R': 1,
    'L': 2,
    'D': 3
}

d = dir_str_to_sum[d]

dxy = [
    (-1, 0), (0, 1), (0, -1), (1, 0)
]
def isin(r, c):
    return 1 <= r <= n and 1 <= c <= n

for _ in range(t):
    nr = r + dxy[d][0]
    nc = c + dxy[d][1]

    if not isin(nr, nc):
        d = 3 - d
    else:
        r, c = nr, nc

print(r, c)

# dict = {
#     'U': (-1, 0),
#     'D': (1, 0),
#     'R': (0, 1),
#     'L': (0, -1)
# }

# print(dict)

# # 방향
# def direct(dir):
#     return dict[dir]

# # 인덱스 범위
# def isin(nx, ny):
#     return 0<=nx<n and 0<=ny<n

# for i in range(t):
#     nx = r + direct(d)[0]
#     ny = c + direct(d)[1]

#     if not isin(nx, ny):
#         nx = r + direct(d)[0]
#         ny = c + direct(d)[1]
# print(nx, ny)

