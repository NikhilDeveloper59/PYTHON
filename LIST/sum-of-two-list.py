matrix = [[1, 2, 3],[4, 5, 6]]

print(matrix)

sum = 0
for row in matrix:
    for value in row:
        sum += value

print("sumation of all element:",sum)   