n = int(input())

# Please write your code here.
def func(int):
    cnt = 1
    for _ in range(int):
        for _ in range(int):
            print(cnt, end=' ')
            cnt += 1

            if cnt > 9:
                cnt = 1
        print()
func(n)