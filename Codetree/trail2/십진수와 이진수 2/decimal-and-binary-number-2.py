N = input()

# Please write your code here.
n = len(N)
arr = []
for i in N:
    arr.append(i)
arr = arr[::-1]

# 십진수 변환
res = 0
k = 0
for i in arr:
    res += int(i) * (2**k)
    k+= 1

res = res * 17

# 이진수 변환
arr2 = []
while res > 0:
    arr2.append(res % 2)
    res = res // 2

print(*arr2[::-1], sep='')


# # others
# # 변수를 선언하고 이진수로 표현된 수를 입력받습니다.
# binary = list(map(int, list(input())))
# length = len(binary)

# # 십진수로 변환합니다.
# num = 0
# for i in range(length):
#     num = num * 2 + binary[i]

# # 십진수에 17을 곱합니다.
# num *= 17

# digits = []

# # 이진수로 변환합니다.
# while True:
#     if num < 2:
#         digits.append(num)
#         break

#     digits.append(num % 2)
#     num //= 2

# # 이진수를 출력합니다.
# # 뒤집은 다음에 출력해야 함에 유의합니다.
# for digit in digits[::-1]:
#     print(digit, end="")
# print()