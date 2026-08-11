a, b = map(int, input().split())

arr = []
while a > 1:
    mod = a % b
    a = a // b # 몫
    arr.append(mod)

dic = {}
for i in arr:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

res = 0
appear = list(dic.values())
for i in appear:
    res += i**2

print(res)


# # others
# # 변수 입력받기
# a, b = tuple(map(int, input().split()))
# count_arr = [0] * 10
# ans = 0
    
# # a가 1 이하가 될 때 까지 나누면서 나머지를 count배열에 저장하기
# while a > 1:
#     count_arr[a % b] += 1
#     a //= b
    
# # 나머지가 나온 횟수를 구해 정답 구하기
# for elem in count_arr:
#     ans += elem ** 2

# # 출력
# print(ans)
