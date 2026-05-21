inp = input()
arr = inp.split()
N = int(arr[0])
M = int(arr[1])

matrix1 = [
    list(map(int, input().split())) for _ in range(N)
]
matrix2 = [
    list(map(int, input().split())) for _ in range(N)
]
matrix3 = []

for i in range(N):
    row = []
    for j in range(M):
        elem1 = matrix1[i][j]
        elem2 = matrix2[i][j]
        
        if elem1 == elem2:
            row.append(0)
        else:
            row.append(1)
    matrix3.append(row)

for i in range(N):
    for j in range(M):
        elem = matrix3[i][j]
        print(elem, end=' ')
    print()
