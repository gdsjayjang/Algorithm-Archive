n, m = map(int, input().split())
arr = list(map(int, input().split()))

def func(m):
    if m % 2 == 1: # 홀수
        m -= 1
    else: # 짝수
        m //= 2

    return m

cum = 0
while m >= 1:
    cum += arr[m-1]
    m = func(m)

print(cum)