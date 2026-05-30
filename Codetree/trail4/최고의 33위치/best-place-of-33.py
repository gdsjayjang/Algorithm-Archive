n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_coins = 0

for i in range(n - 2):
    for j in range(n - 2):
        
        # 동전 카운트
        current_coins = 0
        for row in range(i, i + 3):
            for col in range(j, j + 3):
                current_coins += grid[row][col]
                
        # 비교
        if current_coins > max_coins:
            max_coins = current_coins

print(max_coins)