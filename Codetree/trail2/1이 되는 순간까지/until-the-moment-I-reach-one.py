N = int(input())

# Please write your code here.
cnt = 0

def func(n):
    global cnt
    if n == 1:
        return

    if n % 2 == 0:    
        cnt += 1
        func(n / 2)
    else:
        cnt += 1
        func(n // 3)
    
func(N)
print(cnt)
