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