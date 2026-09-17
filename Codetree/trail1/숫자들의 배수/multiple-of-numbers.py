n = int(input())

temp = n
cnt = 0
while cnt <=1 :
    if temp % 5 == 0:
        cnt += 1

    print(temp, end=' ')
    temp += n