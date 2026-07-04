n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
# check
max_sum = 0

for i in range(n):
    for j in range(i + 2, n):
        current_sum = numbers[i] + numbers[j]
        
        if current_sum > max_sum:
            max_sum = current_sum

print(max_sum)