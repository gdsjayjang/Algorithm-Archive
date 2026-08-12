n = int(input())
# A65 Z90

init = 65
for i in range(n): # i = 0 1 2
    # 공백: 0 1 2
    for _ in range(i):
        print(' ', end=' ')
    # 문자: 3 2 1
    for _ in range(n-i, 0, -1): # 3, 2, 1
        if init > 90:
            init = 65
        print(chr(init), end=' ')
        init += 1
    print()