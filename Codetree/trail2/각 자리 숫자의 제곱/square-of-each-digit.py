N = int(input())

# Please write your code here.
global res

def rec(n):
    if n < 1:
        return n
    temp = (n % 10)**2

    return rec(n // 10) + temp

print(rec(N))