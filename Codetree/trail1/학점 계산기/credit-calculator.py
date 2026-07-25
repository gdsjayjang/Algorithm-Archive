n = int(input())

arr = list(map(float, input().split()))

arr_mean = round(sum(arr) / len(arr), 1)

print(arr_mean)
if arr_mean >= 4:
    print('Perfect')
elif arr_mean >= 3 :
    print('Good')
else:
    print('Poor')