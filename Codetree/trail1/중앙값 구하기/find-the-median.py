a, b, c = map(int, input().split())

if a > b:
    if b > c:           # c가 중앙
        print(b)
    elif a > c:
        print(c)
    else:
        print(a)
else:                   # a < b
    if b > c:
        print(c)
    else:               # a < b, b < c
        print(b)
