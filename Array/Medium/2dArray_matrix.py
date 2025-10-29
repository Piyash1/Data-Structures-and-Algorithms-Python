matrix = [[5,10,8],[7,6,3],[2,1,9]]

rows = len(matrix)
cols = len(matrix[0])
#print the matrix
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")
    print()

# Print Transpose of the Matrix
print("Transpose of the Matrix:")
result = [[0] * rows for _ in range(cols)]
for i in range(rows):
    for j in range(cols):
        result[j][i] = matrix[i][j]
print(result)

# Print Upper Triangular Matrix
print("Upper Triangular Matrix:")
for i in range(rows):
    for j in range(cols):
        if j >= i:
            print(matrix[i][j], end=" ")
        else:
            print("*", end=" ")
    print()

# Print Lower Triangular Matrix
print("Lower Triangular Matrix:")
for i in range(rows):
    for j in range(cols):
        if j <= i:
            print(matrix[i][j], end=" ")
        else:
            print("*", end=" ")
    print()

# Print Diagonal Matrix
print("Diagonal Matrix:")
for i in range(rows):
    for j in range(cols):
        if i == j:
            print(matrix[i][j], end=" ")
        else:
            print("*", end=" ")
    print()

