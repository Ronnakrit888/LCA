def gauss_jordan(matrix1, matrix2):
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])

    # Augmenting the matrix1 with matrix2
    augmented_matrix = [row1 + row2 for row1, row2 in zip(matrix1, matrix2)]

    for i in range(rows1):
        # Partial pivoting
        max_row = i
        for j in range(i + 1, rows1):
            if abs(augmented_matrix[j][i]) > abs(augmented_matrix[max_row][i]):
                max_row = j
        augmented_matrix[i], augmented_matrix[max_row] = augmented_matrix[max_row], augmented_matrix[i]

        # Make the diagonal elements to be 1
        divisor = augmented_matrix[i][i]
        for j in range(cols1 + cols2):
            augmented_matrix[i][j] /= divisor

        # Perform row operations to make other elements in the column zero
        for j in range(rows1):
            if j != i:
                factor = augmented_matrix[j][i]
                for k in range(cols1 + cols2):
                    augmented_matrix[j][k] -= factor * augmented_matrix[i][k]

    # Extract the result matrix after Gauss-Jordan elimination
    result_matrix = [row[cols1:] for row in augmented_matrix]
    return result_matrix

