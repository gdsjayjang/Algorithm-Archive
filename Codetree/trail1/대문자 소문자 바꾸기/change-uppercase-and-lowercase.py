arr = input()

for i in arr:
    if ord(i) < 65:
        print(i.upper(), end='')
    else:
        print(i.lower(), end='')