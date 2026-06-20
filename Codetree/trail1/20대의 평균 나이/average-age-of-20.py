cnt = 0
sum = 0
while True:
    a = int(input())
    sum += a
    cnt += 1
    if (a < 20) or( a >= 30):
        sum -= a
        cnt -= 1
        print(f'{sum / cnt:.2f}')
        break