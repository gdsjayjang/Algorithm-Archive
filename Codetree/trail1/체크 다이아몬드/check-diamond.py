n = int(input())

for i in range(n):
    # 공백 i=0 -> 2, i=1 -> 1, i=2 -> 0
    for _ in range(n-1, i, -1):
        print(' ', end='')
    # 별 i=0 -> 1, i=1 -> 2, i=2 -> 3
    for _ in range(i+1):
        print('*', end=' ')

    print()

for j in range(n-1):
    # 공백 j=0 -> 1, j=1 -> 2
    for _ in range(j+1):
        print(' ', end='')
    # 별 j=0 -> 2, j=1 -> 1
    for _ in range(n-j, 1, -1):
        print('*', end=' ')

    print()


# # others
# # 변수 선언 및 입력
# n = int(input())

# # 모양에 맞게 위쪽 별을 출력합니다.
# for i in range(n):
#     for _ in range(n - i - 1):
#         print(" ", end="")
#     for _ in range(i + 1):
#         print("* ", end="")
#     print()

# # 모양에 맞게 아래쪽 별을 출력합니다.
# for i in range(n-2, -1, -1):
#     for _ in range(n - i - 1):
#         print(" ", end="")
#     for _ in range(i + 1):
#         print("* ", end="")
#     print()