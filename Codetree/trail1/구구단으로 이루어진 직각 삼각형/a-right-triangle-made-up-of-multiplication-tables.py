n = int(input())

for i in range(1, n+1):
    for j in range(1, n-i+2):
        if j != n-i+1:
            print(f'{i} * {j} = {i*j} / ', end='')
        else:
            print(f'{i} * {j} = {i*j}', end='')
    print()


# # others
# # 변수 선언 및 입력
# n = int(input())

# # 구구단으로 이루어진 직각 삼각형을 출력합니다.
# for i in range(1, n + 1):
#     for j in range(1, n - i + 2):
#         print(f"{i} * {j} = {i * j}", end="")
        
#         if j != (n - i + 1):
#             print(" / ", end="")
#     print()