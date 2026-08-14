a, b = map(int, input().split())

def func(a, b):
    big = max(a, b)
    small = min(a, b)
    big += 25
    small *= 2

    return big, small

big, small = func(a, b)
print(big, small)