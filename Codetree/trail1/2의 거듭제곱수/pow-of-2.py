n = int(input())

a = 1
while True:
    if n == 2**a:
        print(a)
        break
    else:
        a += 1