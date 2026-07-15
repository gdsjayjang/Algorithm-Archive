n = int(input())

for i in range(n,0,-1):
    for j in range(i):
        print('*', end='')
    
    print(' '*2*(n-i), end='')

    for k in range(i, 0, -1):
        print('*', end='')

    print()

# # others
# n = int(input())

# for i in range(n):
#     for _ in range(n - i):
#         print("*", end="")
#     for _ in range(2 * i):
#         print(" ", end="")
#     for _ in range(n - i):
#         print("*", end="")
#     print()