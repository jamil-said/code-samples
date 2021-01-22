""" minesweeper
In the popular Minesweeper game you have a board with some mines and those cells that don't 
contain a mine have a number in it that indicates the total number of mines in the neighboring 
cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

Example

For

matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]]

the output should be

minesweeper(matrix) = [[1, 2, 1],
                       [2, 1, 1],
                       [1, 1, 1]]

Check out the image below for better understanding:

Input/Output

    [execution time limit] 4 seconds (py3)

    [input] array.array.boolean matrix

    A non-empty rectangular matrix consisting of boolean values - true if the corresponding 
    cell contains a mine, false otherwise.

    Guaranteed constraints:
    2 ≤ matrix.length ≤ 100,
    2 ≤ matrix[0].length ≤ 100.

    [output] array.array.integer

    Rectangular matrix of the same size as matrix each cell of which contains an integer 
    equal to the number of mines in the neighboring cells. Two cells are called neighboring 
    if they share at least one corner.
"""


def minesweeper(m):
    r = [[0 for i in range(len(m[0]))] for j in range(len(m))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            if i-1 >= 0:
                r[i][j] += 1 if m[i-1][j] else 0
                r[i][j] += 1 if j-1>=0 and m[i-1][j-1] else 0
                r[i][j] += 1 if j+1<len(m[0]) and m[i-1][j+1] else 0
            if i+1 < len(m):
                r[i][j] += 1 if m[i+1][j] else 0
                r[i][j] += 1 if j-1>=0 and m[i+1][j-1] else 0
                r[i][j] += 1 if j+1<len(m[0]) and m[i+1][j+1] else 0
            r[i][j] += 1 if j-1>=0 and m[i][j-1] else 0
            r[i][j] += 1 if j+1<len(m[0]) and m[i][j+1] else 0
    return r


print(minesweeper([[True,False,False], 
                   [False,True,False], 
                   [False,False,False]])) # [[1,2,1], 
                                          #  [2,1,1], 
                                          #  [1,1,1]]
