commands = input()

# Please write your code here.
# check
x, y = 0, 0
elapsed_time = 0
returned_to_origin = False

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

current_dir = 0

for cmd in commands:
    if cmd == 'L':
        current_dir = (current_dir - 1) % 4
        elapsed_time += 1
        
    elif cmd == 'R':
        current_dir = (current_dir + 1) % 4
        elapsed_time += 1
        
    elif cmd == 'F':
        x += dx[current_dir]
        y += dy[current_dir]
        elapsed_time += 1

        if x == 0 and y == 0:
            print(elapsed_time)
            returned_to_origin = True
            break

if not returned_to_origin:
    print(-1)