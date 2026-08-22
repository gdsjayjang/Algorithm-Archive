N = int(input())

# Please write your code here.
global res

def rec(n):
    if n < 10:
        return n**2
    temp = (n % 10)**2

    return rec(n // 10) + temp

print(rec(N))