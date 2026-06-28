n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
segments = []
current_pos = 0

for i in range(n):
    distance = x[i]
    direction = dir[i]
    
    if direction == 'R':
        next_pos = current_pos + distance
        segments.append((current_pos, next_pos))
    else:
        next_pos = current_pos - distance
        segments.append((next_pos, current_pos))
        
    current_pos = next_pos

events = []
for start, end in segments:
    events.append((start, 1))
    events.append((end, -1))

events.sort()

total_length = 0
current_lines = 0
prev_pos = 0

for position, event_type in events:
    if current_lines >= 2:
        total_length += (position - prev_pos)

    current_lines += event_type

    prev_pos = position

print(total_length)