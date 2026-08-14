a, b = map(int, input().split())

def func(a, b):
    big = max(a,b)
    small = min(a,b)

    big += 25
    small *= 2

    return small, big

small, big = func(a, b)
print(small, big)