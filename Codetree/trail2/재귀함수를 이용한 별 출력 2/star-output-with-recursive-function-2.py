n = int(input())

# Please write your code here.
def func(n):
    if n <= 0:
        return
    print('* ' * n)
    func(n-1)
    print('* ' * n)

func(n)


# # others
# # 입력을 받습니다.
# n = int(input())


# def print_star(n):   # 1부터 2n번째 줄까지 주어진 모양대로 별을 출력하는 함수
#     if n == 0:       # n이 0이라면, 더 이상 진행하지 않고
#         return       # 퇴각합니다.
    
#     # 외각 별을 출력합니다.
#     for _ in range(n):
#         print("*", end=" ")
#     print()

#     print_star(n - 1) # 가운데 별을 출력하는 함수

#     # 외각 별을 출력합니다.
#     for _ in range(n):
#         print("*", end=" ")
#     print()

   
# print_star(n)