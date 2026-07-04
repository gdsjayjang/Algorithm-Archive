N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
# check
x, y = 0, 0
elapsed_time = 0
returned_to_origin = False

dx = {'N': 0, 'S': 0, 'E': 1, 'W': -1}
dy = {'N': 1, 'S': -1, 'E': 0, 'W': 0}

for i in range(N):
    current_dir = dir[i]
    current_dist = dist[i]
    
    for _ in range(current_dist):
        x += dx[current_dir]
        y += dy[current_dir]
        elapsed_time += 1   # 1초 경과
        
        if x == 0 and y == 0:
            print(elapsed_time)
            returned_to_origin = True
            break
            
    if returned_to_origin:
        break

if not returned_to_origin:
    print(-1)