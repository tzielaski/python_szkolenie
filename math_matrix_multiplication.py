def matrix_multiplication(A, B):
    """
    >>> A = [[1, 0], [0, 1]]
    >>> B = [[4, 1], [2, 2]]
    >>> matrix_multiplication(A, B)
    [[4, 1], [2, 2]]

    >>> A = [[1,0,1,0], [0,1,1,0], [3,2,1,0], [4,1,2,0]]
    >>> B = [[4,1], [2,2], [5,1], [2,3]]
    >>> matrix_multiplication(A, B)
    [[9, 2], [7, 3], [21, 8], [28, 8]]
    """
    partial_sum = 0
    result_matrix = []
    for i in range(0, len(A)):
        result_matrix.append([])
        for j in range(0, len(B[i])):
            result_matrix[i].append(0)
            for k in range(0, len(B)):
                partial_sum += A[i][k] * B[k][j]
            result_matrix[i][j] = partial_sum
            partial_sum = 0
    return result_matrix
