N = int(input())

for _ in range(N):
    inp = input()
    arr = inp.split()

    A = int(arr[0])
    B = int(arr[1])

    sum = 0
    for i in range(A, B+1):
        if i % 2 == 0:
            sum += i
    print(sum)
