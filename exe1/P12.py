def read_matrix(file_name):
    matrix = []
    with open(file_name, 'r') as file:
        for line in file:
            row = list(map(int, line.strip().split()))
            matrix.append(row)
    return matrix

def write_matrix(matrix, file_name):
    with open(file_name, 'w') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')

def add_mat(file1, file2, result_file):
    matrix1 = read_matrix(file1)
    matrix2 = read_matrix(file2)

    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])

    if rows1 != rows2 or cols1 != cols2:
        with open(result_file, 'w'):
            pass
        return


    result_matrix = []
    for i in range(rows1):
        row = []
        for j in range(cols1):
            row.append(matrix1[i][j] + matrix2[i][j])
        result_matrix.append(row)


    write_matrix(result_matrix, result_file)

add_mat('mat1.txt', 'mat2.txt', 'outmat.txt')  
add_mat('mat1.txt', 'mat3.txt', 'outmat1.txt')

