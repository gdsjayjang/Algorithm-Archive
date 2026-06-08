inp = input()
arr = inp.split()

a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
elif b > a:
    if b > c:
        print(b)
    else:
        print(c)
elif a > c:
    if a > b:
        print(a)
    else:
        print(b)
elif c > a:
    if c > b:
        print(c)
    else:
        print(b)
elif b > c:
    if b > a:
        print(b)
    else:
        print(a)
elif c > b:
    if c > a:
        print(c)
    else:
        print(a)
