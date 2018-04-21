
""" constructSubmatrix -- 15 minutes
Given a matrix (i.e. an array of arrays), find its submatrix obtained by 
deleting the specified rows and columns.

Example

For

matrix = [[1, 0, 0, 2], 
          [0, 5, 0, 1], 
          [0, 0, 3, 5]]
rowsToDelete = [1] and columnsToDelete = [0, 2], the output should be

constructSubmatrix(matrix, rowsToDelete, columnsToDelete) = [[0, 2],
                                                             [0, 5]]
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.integer matrix

2-dimensional array of integers.

Guaranteed constraints:
1 ≤ matrix.length ≤ 5,
1 ≤ matrix[0].length ≤ 5,
0 ≤ matrix[i][j] ≤ 15.

[input] array.integer rowsToDelete

Array of indices (0-based) of rows to be deleted.

Guaranteed constraints:
0 ≤ rowsToDelete.length ≤ 2,
0 ≤ rowsToDelete[i] < matrix.length.

[input] array.integer columnsToDelete

Array of indices (0-based) of columns to be deleted.

Guaranteed constraints:
0 ≤ columnsToDelete.length ≤ 2,
0 ≤ columnsToDelete[i] < matrix[0].length.

[output] array.array.integer

"""
#may need to sort the colDel before using it (if input not sorted)
def constructSubmatrix(matrix, rowDel, colDel):
    count = 0
    for i in rowDel:
        del matrix[i]
    for i in colDel:
        for row in matrix:
            del row[i-count]
        count += 1
    return matrix

print(constructSubmatrix([[1, 0, 0, 2], 
                          [0, 5, 0, 1], 
                          [0, 0, 3, 5]], [1], [0, 2])) # [[0, 2], [0, 5]]


