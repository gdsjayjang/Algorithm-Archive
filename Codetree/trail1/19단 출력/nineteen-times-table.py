flag = 0
for i in range(1, 20):
    for j in range(1, 20):
        if j == 19:
            print(f'{i} * {j} = {i*j}')
        elif flag < 1 :
            print(f'{i} * {j} = {i*j} /', end=' ')
            flag += 1
        else:
            print(f'{i} * {j} = {i*j}')
            flag = 0
        