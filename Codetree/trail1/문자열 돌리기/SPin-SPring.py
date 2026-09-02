inp = input()
n = len(inp)

for i in range(n+1):
    print(inp)
    inp = inp[-1] + inp[:-1]