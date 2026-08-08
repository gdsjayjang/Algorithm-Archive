arr = list(input())

for i in arr:
    if ord(i) >= 97:
        print(i.upper(), end='')
    else:
        print(i.lower(), end='')