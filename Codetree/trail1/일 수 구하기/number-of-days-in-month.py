month = int(input())

day_31 = [1, 3, 5, 7, 8, 10, 12]
day_30 = [4, 6, 9, 11]
day_28 = [28]

if month in day_31:
    print(31)
elif month in day_30:
    print(30)
else:
    print(28)