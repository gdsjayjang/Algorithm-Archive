x, y = map(int, input().split())

if x > 0:
    print(1 if y > 0 else 4)
elif (x < 0):
    print(2 if y > 0 else 3)

# # short coding
# '3421'[int(input()) > 0::2][int(input()) > 0]