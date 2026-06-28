n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
events = []
for start, end in segments:
    events.append((start, 0))
    events.append((end, 1))

events.sort()

max_overlaps = 0
current_overlaps = 0

for position, event_type in events:
    if event_type == 0:
        current_overlaps += 1
    else:
        current_overlaps -= 1
    
    if current_overlaps > max_overlaps:
        max_overlaps = current_overlaps

print(max_overlaps)