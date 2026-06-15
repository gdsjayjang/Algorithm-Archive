a, b = map(int, input().split())

li = []
for i in range(a, b+1):
    if (i%6==0) and (i%8!=0):
        li.append(i)

print(sum(li))