a, b = map(int, input().split())
arr = [2, 4, 6, 8]

for j in arr:
    for i in range(b, a-1, -1):
        if i != a:
            print(f'{i} * {j} = {i*j} /', end=' ')
        else:
            print(f'{i} * {j} = {i*j}')


# # others
# # 변수 선언, 입력
# inp = input()
# arr = inp.split()
# a, b = int(arr[0]), int(arr[1])

# # 조건대로 구구단을 출력합니다.
# for i in range (2, 9, 2):
#     for j in range(b, a - 1, -1):
#         print(f"{j} * {i} = {i * j}", end="")
#         if j != a:
#             print(" / ", end="")
#     print()