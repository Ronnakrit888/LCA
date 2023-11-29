
def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    
    return result

A = [[1,2,3,4],[5,6,7,8]]

At = transpose(A)

print(A)
print("is transposed to")
print(At)