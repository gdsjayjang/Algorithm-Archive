n, a = input().split()
n = int(n)

cnt = 0
for i in range(n):
    str = input()
    if a == str:
        cnt +=1

print(cnt)