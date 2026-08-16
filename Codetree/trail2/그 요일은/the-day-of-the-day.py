m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

start_days = sum(month[:m1]) + d1
end_days = sum(month[:m2]) + d2

diff = end_days - start_days
div = diff  // 7
mod = diff - div * 7


if (days.index(A)) > mod:
    print((end_days - start_days) // 7)
else:   
    print((end_days - start_days) // 7 + 1) 