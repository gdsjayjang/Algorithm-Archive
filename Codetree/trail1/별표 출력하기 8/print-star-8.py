n = int(input())

for i in range(1, n+1):
    if i % 2 == 1:
        print('*')
    else:
        print('* ' * i, end=' ')
        print()


# # others
# # 변수 선언 및 입력
# n = int(input())

# #i가 짝수인 경우 별을 1개, 홀수인 경우 i+1개를 출력합니다
# for i in range(n):
#     if i % 2 == 0:
#         print("*", end="")
#     else:
#         for _ in range(i + 1):
#             print("*", end=" ")
#     print()