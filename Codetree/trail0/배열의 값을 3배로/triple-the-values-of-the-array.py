matrix = [list(map(int, input().split())) for _ in range(3)]
new_matrix = [[3* element for element in row] for row in matrix]

for row in new_matrix:
    for element in row:
        print(element, end=' ')
    print()