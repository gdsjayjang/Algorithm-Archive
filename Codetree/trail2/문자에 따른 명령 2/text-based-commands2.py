dirs = input()

# Please write your code here.
dirs_list = list(dirs)

# 동 남 서 북
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

dir_num = 3
x, y = 0, 0
for i in dirs_list:
    if i == 'R':
        dir_num = (dir_num + 1) % 4
    elif i == 'L':
        dir_num = (dir_num -1 + 4) % 4
    else:
        x += dx[dir_num]
        y += dy[dir_num] 

print(x, y)