n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def func(n1, n2, a, b):
    check_list = []

    for i in range(n1):
        for j in range(n2):
            if a[i] == b[j]:
                new_idx = i
                new_raw = []

                if new_idx + n2 <= n1:
                    for k in range(new_idx, new_idx + n2):
                        new_raw.append(a[k])
                    check_list.append(new_raw)
    
    for target in check_list:
        if target == b:
            return 'Yes'
    
    return 'No'


result = func(n1, n2, a, b)
print(result)


# Sol.1
# def func(n1, n2, a, b):
#     for i in range(n1 - n2 + 1):
#         if a[i:i+n2] == b:
#             return 'Yes'
    
#     return 'No'

# result = func(n1, n2, a, b)
# print(result)



# Sol.2
# # n번째 인덱스부터 시작하는 n2길이의 a수열과
# # b수열이 완전히 일치하는지 확인합니다..
# def is_same(n):
#     for i in range(n2):
#         if a[i + n] != b[i]:
#             return False

#     return True

# # b가 a의 연속부분수열인지 확인합니다.
# def is_subsequence():
#     for i in range(n1 - n2 + 1):
#         if is_same(i):
#             return True
    
#     return False


# if is_subsequence():
#     print("Yes")
# else:
#     print("No")