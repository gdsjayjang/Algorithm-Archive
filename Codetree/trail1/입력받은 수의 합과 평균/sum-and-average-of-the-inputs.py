n = int(input())

li = []
for _ in range(n):
    a = int(input())
    li.append(a)

print(sum(li), f'{sum(li)/len(li):.1f}')