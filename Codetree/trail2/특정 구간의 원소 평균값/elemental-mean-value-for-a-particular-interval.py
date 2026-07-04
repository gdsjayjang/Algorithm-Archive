n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
# check
count = 0

for i in range(n):
    current_sum = 0

    for j in range(i, n):
        current_sum += arr[j]
        length = j - i + 1
        
        avg = current_sum / length
        
        if avg in arr[i:j+1]:
            count += 1

print(count)