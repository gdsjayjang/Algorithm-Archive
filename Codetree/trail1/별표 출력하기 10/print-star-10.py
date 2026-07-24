n = int(input())

for i in range(2*n):
    if i % 2 ==0:
        # i=0; 1
        # i=2; 2
        # i=4; 3
        # i=6; 4
        # i=8; 5
        idx = int((i+2)/2)
        for j in range(idx):
            print('*', end=' ')
    else:
        # i=1; 5
        # i=3; 4
        # i=5; 3
        # i=7; 2
        # i=9; 1
        idx = int((2*n-i)/2)
        for k in range(idx,-1, -1):
            print('*', end=' ')
    print()


# # others
# # 변수 선언 및 입력
# n = int(input())

# # i가 짝수인 경우 별을 1개, 홀수인 경우 i + 1개 출력합니다
# for i in range(2 * n):
#     if i % 2 == 0:
#         for _ in range(1 + i // 2):
#             print("*", end=" ")
#     else:
#         for _ in range(n - (i - 1) // 2):
#             print("*", end=" ")
#     print()