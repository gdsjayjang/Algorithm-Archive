a, b, c = map(int, input().split())

# Please write your code here.
day = a - 11
hour = b - 11
minute = c - 11

if (day == 0) and (hour < 0):
    print(-1)
elif (day == 0) and (hour == 0) and (minute < 0):
    print(-1)
else:
    day_min = day * 24 * 60
    hour_min = hour * 60

    results = day_min + hour_min + minute

    print(results)

# another
# diff = (a * 24 * 60 + b * 60 + c) - (11 * 24 * 60 + 11 * 60 + 11)

# if diff < 0:
#     print(-1)
# else:
#     print(diff)