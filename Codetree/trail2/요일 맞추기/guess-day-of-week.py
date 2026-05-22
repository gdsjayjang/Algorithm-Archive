m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

days_m1 = sum(months[:m1-1]) + d1
days_m2 = sum(months[:m2-1]) + d2
days_diff = days_m2 - days_m1

if days_diff < 0:
    days = days_diff % 7
elif days_diff >= 0:
    days = abs(days_diff) % 7
    
print(days_list[days])