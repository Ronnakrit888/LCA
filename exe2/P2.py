
def matdot(matrixA, matrixB):
    rows1, cols1 = len(matrixA), len(matrixA[0])
    rows2, cols2 = len(matrixB), len(matrixB[0])
   
    if cols1 != rows2:
        return "None"
    
    result = [[0 for _ in range(rows1)] for _ in range(cols2)]
    
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrixA[i][k] * matrixB[k][j]
            
    return result


A = [[ 1, 2, 3], 
     [-1, 0, 4]]

B = [[10, 20], 
     [5,  -2], 
     [7,   9]]

AB = matdot(A, B)
print("A dot B =", AB)
