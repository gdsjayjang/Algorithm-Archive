a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

if a1 > b1:         # 수학
    print('A')
elif a1 == b1:      # 수학이 같을 때
    if a2 > b2:     # 영어
        print('A')
    else:
        print('B')
else:
    print('B')
    