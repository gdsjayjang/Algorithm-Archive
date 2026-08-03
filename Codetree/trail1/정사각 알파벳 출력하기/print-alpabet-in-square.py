n = int(input())

out = 'A'
for _ in range(n):
    for _ in range(n):
        print(out, end='')
        out = ord(out) + 1
        out = chr(out)
    print()