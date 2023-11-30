
def swoprow(matrix, i, j):
    row = len(matrix)
    if 0 <= i < row and 0 <= j < row:
        if i != j:
            matrix = [row[:] for row in matrix]
            matrix[i], matrix[j] = matrix[j], matrix[i] 
    
    return matrix

if __name__ == '__main__':  
    A = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [-1, -2, -3, -4]]  
    print(A)  
    print('After swop')  
    Ap = swoprow(A, 0, 3)  
    print('A=', A)  
    print("A'=", Ap)
