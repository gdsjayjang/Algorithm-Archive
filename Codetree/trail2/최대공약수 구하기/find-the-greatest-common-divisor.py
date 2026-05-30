n, m = map(int, input().split())

# Please write your code here.
if n < m:
    n, m = m, n

# (n >= m)
def gcd(n, m):
    while m != 0:
        temp = m
        m = n % m   # remainder
        n = temp

    return n

result = gcd(n, m)
print(result)