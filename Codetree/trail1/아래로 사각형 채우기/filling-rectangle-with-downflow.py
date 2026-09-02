n = int(input())

for i in range(1, n+1):
    res = i
    for j in range(n):
        print(res, end=' ')
        res += n
    print()


# # others
# # n을 입력받습니다.
# n = int(input())
# num = 1

# # 2차원 배열을 구현합니다.
# arr = [
#     [0 for _ in range(n)]
#     for _ in range(n)
# ]
    
# # 배열의 숫자를 채웁니다.
# for i in range(n):
#     for j in range(n):
#         arr[j][i] = num
#         num += 1
        
# # 채워진 배열을 출력합니다.
# for row in arr:
#     for elem in row:
#         print(elem, end=" ")
#     print()
