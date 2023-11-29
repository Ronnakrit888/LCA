
def swoprow(matrix, row1, row2):
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]
    
    return matrix

A = [[ 1,   2,   3,   4 ], # row 0
     [ 5,   6,   7,   8 ], # row 1
     [ 9,  10,  11,  12 ], # row 2
     [-1,  -2,  -3,  -4 ]] # row 3

print(swoprow(A, 0, 3))
