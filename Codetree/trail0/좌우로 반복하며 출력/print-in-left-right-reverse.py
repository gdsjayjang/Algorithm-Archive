N = int(input())

for i in range(1, N+1):

    if i % 2 == 1: # 홀수: 정방향
        for j in range(1, N+1):
            print(j, end='')
        print()
    elif i % 2 == 0: # 짝수: 역방향
        for j in range(N, 0, -1):
            print(j, end='')
        print()
