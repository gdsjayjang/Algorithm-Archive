n = int(input())

for i in range(2*n):
    if i % 2 == 0:
        # idx should be 5, 4, 3, 2, 1
        idx = (2*n-i)// 2 #
        for _ in range(idx):
            print('*', end=' ')

    else:
        # idx should be 1, 2, 3, 4, 5
        idx = i // 2 + 1
        for _ in range(idx):
            print('*', end=' ')
    print()


# # others
# # 변수 선언 및 입력
# n = int(input())

# # i가 홀수인 경우 별을 1 + (i // 2)개, 짝수인 경우 n - (i // 2)개 출력합니다
# for i in range(2 * n):
#     if i % 2 == 1:
#         for _ in range(1 + i // 2):
#             print("* ", end="")
#     else:
#         for _ in range(n - i // 2):
#             print("* ", end="")
#     print()