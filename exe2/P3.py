def minor(matrix, row, col):
    sub_matrix = [row[:col] + row[col+1:] for row_index, row in enumerate(matrix) if row_index != row]
    return sub_matrix

def determinant(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    if rows == 1 and cols == 1:
        return matrix[0][0] 
    
    elif rows == 2 and cols == 2:
        det = (matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1])
        return det
    
    det = 0
    for i in range(cols):
        m = minor(matrix[1:], 0, i)
        det += ((-1) ** i) * matrix[0][i] * determinant(m)

    return det
    
A = [[3,  4, 5],
     [1, -1, 0],
     [8,  2, 7]]

print(determinant(A))