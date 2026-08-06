inp = list(input())
com = list(input())

for i in range(len(com)):
    if com[i] == 'L':
        temp = inp[0]
        for j in range(len(inp)-1):
            inp[j] = inp[j+1]
        inp[-1] = temp

    elif com[i] == 'R':
        temp = inp[-1]
        for j in range(len(inp)-1, 0, -1):
            inp[j] = inp[j-1]
        inp[0] = temp

print(*inp, sep='')