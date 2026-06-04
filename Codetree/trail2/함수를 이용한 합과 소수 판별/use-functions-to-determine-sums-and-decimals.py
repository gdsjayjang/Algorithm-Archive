a, b = map(int, input().split())

# Please write your code here.
def prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def func(n):
    is_prime = prime(n)

    sum = 0
    while n > 0:
        one = n % 10 # 끝자리수
        n = n // 10
        sum += one
    if (is_prime == True) and ((sum) % 2 == 0):
        return 1
    else:
        return 0

cnt = 0
for i in range(a, b+1):
    cnt += func(i)

print(cnt)