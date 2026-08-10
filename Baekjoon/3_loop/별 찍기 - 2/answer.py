N = int(input())

for i in range(N):
    print(' ' * (N-1), '*' * (i+1))
    N -= 1


# # other
# N=i = int(input())
# while 0 < i:
#     i -= 1    
#     print(' ' * i + '*' * (N-i))