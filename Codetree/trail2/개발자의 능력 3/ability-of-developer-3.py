abilities = list(map(int, input().split()))

# Please write your code here.
# check
import itertools

total_sum = sum(abilities)

min_diff = float('inf')

for team_a_indices in itertools.combinations(range(6), 3):
    team_a_sum = 0
    for idx in team_a_indices:
        team_a_sum += abilities[idx]

    team_b_sum = total_sum - team_a_sum
    
    diff = abs(team_a_sum - team_b_sum)
    
    if diff < min_diff:
        min_diff = diff

print(min_diff)