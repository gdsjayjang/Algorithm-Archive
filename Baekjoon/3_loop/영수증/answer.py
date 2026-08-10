X = int(input())
N = int(input())
total = 0

for i in range(N):
    a, b = map(int, input().split())
    total = total + a*b

if X == total: 
    print('Yes')
else: 
    print('No')


# # short coding
# X, N, *A = open(0)
# print("YNeos"[int(X)!=sum(eval(i.replace(*' *'))for i in A)::2])