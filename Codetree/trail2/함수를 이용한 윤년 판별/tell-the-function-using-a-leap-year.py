y = int(input())

# Please write your code here.
def check(N):
    if N % 4 == 0:
        if (N % 100 == 0) and (N % 400 != 0):
            return 'false'
        return 'true'

    else:
        return 'false'

print(check(y))