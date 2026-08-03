n = int(input())

for i in range(1, n+1):
    for j in range(1, i+1):
        print(n-i+j, end=' ')
    print()


# # others
# # 숫자로 이루어진 삼각형을 출력합니다.
# for i in range(n):
#     for j in range(i + 1):
#         print(n - i + j, end=" ")
#     print()