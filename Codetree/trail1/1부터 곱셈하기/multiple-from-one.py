n = int(input())

prod = 1
for i in range(1, 11):
    prod *= i
    if prod >= n:
        temp = i
        break

print(temp)