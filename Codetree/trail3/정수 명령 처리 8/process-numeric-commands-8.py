N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] in ["push_front", "push_back"]:
        A.append(int(line[1]))
    else:
        A.append(0)

# Please write your code here.
arr = []
for i in range(N):
    if command[i] == 'push_front':
        arr =[A[i]] + arr
    elif command[i] == 'push_back':
        arr.append(A[i])
    elif command[i] == 'pop_front':
        print(arr[0])
        arr = arr[1:]
    elif command[i] == 'pop_back':
        print(arr[-1])
        arr = arr[:-1]
    elif command[i] == 'size':
        print(len(arr))
    elif command[i] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif command[i] == 'front':
        print(arr[0])
    elif command[i] == 'back':
        print(arr[-1]) 