n = int(input())
# A65 Z90

init = 65
for i in range(n): # i = 0 1 2
    # 공백: 0 1 2
    for _ in range(i):
        print(' ', end=' ')
    # 문자: 3 2 1
    for _ in range(n-i, 0, -1): # 3, 2, 1
        if init > 90:
            init = 65
        print(chr(init), end=' ')
        init += 1
    print()


# # other
# # 변수 선언 및 입력
# n = int(input())
# cnt = 'A'
    
# # 알파벳을 역삼각형 모양으로 출력합니다.
# for i in range(n):
#     for _ in range(i):
#         print("  ", end="")
#     for _ in range(n - i):
#         print(cnt, end=" ")
#         cnt = chr(ord(cnt) + 1)
#         if ord(cnt) > ord('Z'):
#             cnt = 'A'
#     print()