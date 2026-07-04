n = int(input())
S = input()

# Please write your code here.
# check
c_cnt = 0
co_cnt = 0
cow_cnt = 0

for char in S:
    if char == 'C':
        c_cnt += 1
        
    elif char == 'O':
        co_cnt += c_cnt
        
    elif char == 'W':
        cow_cnt += co_cnt

print(cow_cnt)