inp = list(input())

sec = inp[1]

for i in range(len(inp)):
    if inp[i] == sec:
        inp[i] = inp[0]

out = ''.join(inp)
print(out)