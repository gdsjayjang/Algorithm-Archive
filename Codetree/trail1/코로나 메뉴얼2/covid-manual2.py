ppl = [0] * 3
cold = [0] * 3
res = [0] * 4

cnt = 0
for i in range(3):
    inp = input().split()
    ppl[i], cold[i] = inp[0], int(inp[1])

for i in range(3):
    if (ppl[i] == 'Y') and (cold[i] >= 37):
        res[0] += 1
    elif (ppl[i] == 'N') and (cold[i] >= 37):
        res[1] += 1
    elif (ppl[i] == 'Y') and (cold[i] < 37):
        res[2] += 1
    else:
        res[3] += 1

print(*res, sep=' ', end=' ')
if res[0] >= 2:
    print('E')