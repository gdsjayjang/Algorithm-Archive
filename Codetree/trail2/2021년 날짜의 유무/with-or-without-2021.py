M, D = map(int, input().split())

# Please write your code here.
month_31 = [1, 3, 5, 7, 8, 10, 12]
month_30 = [4, 6, 9, 11]
month_28 = [2]

def func(M, D):
    if (M in month_31) and (1 <= D <= 31):
        return 'Yes'
    elif M in month_30 and (1 <= D <= 30):
        return 'Yes'
    elif M in month_28 and (1 <= D <= 28):
        return 'Yes'
    
    
    return 'No'

res = func(M, D)
print(res)