
""" sudoku2 -- 30min
Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 
grid with numbers in such a way that each column, each row, and each of 
the nine 3 × 3 sub-grids that compose the grid all contain all of the 
numbers from 1 to 9 one time.

Implement an algorithm that will check whether the given grid of numbers 
represents a valid Sudoku puzzle according to the layout rules described 
above. Note that the puzzle represented by grid does not have to be solvable.

Example

For

grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
the output should be
sudoku2(grid) = true;

For

grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
the output should be
sudoku2(grid) = false.

The given grid is not correct because there are two 1s in the second 
column. Each column, each row, and each 3 × 3 subgrid can only contain 
the numbers 1 through 9 one time.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.char grid

A 9 × 9 array of characters, in which each character is either a digit 
from '1' to '9' or a period '.'.

[output] boolean

Return true if grid represents a valid Sudoku puzzle, otherwise return 
false.
"""

def sudoku2(grid):
    return checkRows(grid) and checkCols(grid) and checkLst3x3(grid)

def checkRows(grid):
    for row in grid:
        cleanRow = [x for x in row if x.isdigit()]
        if len(cleanRow) != len(set(cleanRow)):
            return False
    return True

def checkCols(grid):
    rotatedGrid = list(zip(*grid[::-1]))
    for row in rotatedGrid:
        cleanRow = [x for x in row if x.isdigit()]
        if len(cleanRow) != len(set(cleanRow)):
            return False
    return True

def checkLst3x3(grid):
    temp = []
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            new_3x3 = [item[i:i+3] for item in grid[j:j+3]]
            for row in new_3x3:
                cleanRow = [x for x in row if x.isdigit()]
                temp.extend(cleanRow)
            if len(temp) != len(set(temp)):
                return False
            temp = []
    return True

print(sudoku2(
       [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']])) # True

print(sudoku2([['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']])) # False

print(sudoku2([[".","4",".",".",".",".",".",".","."], 
         [".",".","4",".",".",".",".",".","."], 
         [".",".",".","1",".",".","7",".","."], 
         [".",".",".",".",".",".",".",".","."], 
         [".",".",".","3",".",".",".","6","."], 
         [".",".",".",".",".","6",".","9","."], 
         [".",".",".",".","1",".",".",".","."], 
         [".",".",".",".",".",".","2",".","."], 
         [".",".",".","8",".",".",".",".","."]])) # False

