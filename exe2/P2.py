
def matdot(matrixA, matrixB):
    rows1, cols1 = len(matrixA), len(matrixA[0])
    rows2, cols2 = len(matrixB), len(matrixB[0])
   
    if cols1 != rows2:
        return None
    
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    
    for i in range(rows1):
        for j in range(cols2):
            for k in range(rows2):
                result[i][j] += matrixA[i][k] * matrixB[k][j]
            
    return result


if __name__ == '__main__':  
    A = [[1, 2, 3], [-1, 0, 4]] 
    B = [[10, 20], [5, -2], [7, 9]]  
    M = [[8], [6]]  
    AB = matdot(A, B)  
    BA = matdot(B, A)  
    AM = matdot(A, M)  
    BM = matdot(B, M)  
    print('A=', A)  
    print('B=', B)  
    print('A dot B =', AB)  
    print('B dot A =', BA)  
    print('A dot M =', AM)  
    print('B dot M =', BM)
