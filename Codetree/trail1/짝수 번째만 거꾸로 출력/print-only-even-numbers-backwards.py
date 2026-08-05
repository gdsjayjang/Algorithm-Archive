inp = list(input())
length = len(inp)

for i in range(length-1, -1, -2):
    if i <= 0:
        break
    if length % 2 == 0:
        print(inp[i], end='')
    else:
        print(inp[i-1], end='')