
def swoprow(matrix, row1, row2):
    matrix[row1] = matrix[row2]
    matrix[row2] = matrix[row1] 
    
    return matrix

A = [[0, 23, 6, 8, 1], [1, 3, 5, 7, 16], [2, 4, 6, 8, 9], [25, 66, 2, 5, 19], [-1, -2, -3, -5, 8]]

print(swoprow(A, 2, 0))