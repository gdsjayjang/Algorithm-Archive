N = int(input())

for i in range(1, N+1):
    for j in range(1, N+1):
        if i % 2 == 1: # 홀수: 정방향
            print(j, end='')
        elif i % 2 == 0: # 짝수: 역방향
            print(N-j+1, end='')
    print()
