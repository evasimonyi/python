from copy import deepcopy

# rotate matrix with 90 degrees to the left

# input:

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# output:

[
    [3, 6, 9],
    [2, 5, 8],
    [1, 4, 7]
]

# not square matrix

matrix2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [3, 3, 3]
]


def rotate_matrix(matrix):
    is_matrix_square = all(len(matrix) == len(elem) for elem in matrix)
    if (is_matrix_square):
        rotated_matrix = deepcopy(matrix)
        for listInMatrix in matrix:
            indexOfCurrentList = matrix.index(listInMatrix)  # i
            for numberInList in listInMatrix:
                indexOfCurrentNumber = listInMatrix.index(numberInList)  # j
                # rotated[j][i] = original[i][j] then reverse this list
                rotated_matrix[indexOfCurrentList][indexOfCurrentNumber] = matrix[indexOfCurrentNumber][indexOfCurrentList]
        return rotated_matrix[::-1]
    else:
        return 'matrix is not symmetric'


print(rotate_matrix(matrix1))
