n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
# N, E, S, W
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y = 0, 0

dict = {
    'N': 0,
    'E': 1,
    'S': 2,
    'W': 3
}

for i, d in enumerate(dir):
    x += dx[dict[d]] * dist[i]
    y += dy[dict[d]] * dist[i]

print(x, y)