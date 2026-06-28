N, B = map(int, input().split())

# Please write your code here.
arr = []
while N > 0:
    M = N % B # 나머지
    N = N // B # 몫
    arr.append(M)

print(*arr[::-1], sep='')