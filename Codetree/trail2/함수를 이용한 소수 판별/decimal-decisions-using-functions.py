a, b = map(int, input().split())

# Please write your code here.
def prime(N):
    for i in range(2, N):
        if N % i == 0:
            return False
    return True

sum_of_prime = 0
for i in range(a, b+1):
    if prime(i) == True:
        sum_of_prime += i

print(sum_of_prime)