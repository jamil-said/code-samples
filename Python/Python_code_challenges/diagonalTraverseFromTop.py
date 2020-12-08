""" diagonalTraverseFromTop
Given an MxN matrix, write code which prints out the diagonals (from upper left
to lower right) of the matrix. In this example where M = 3, N = 4:

[[9 3 2]
 [8 6 1]
 [5 5 6]
 [1 2 8]]

Your code should print out:
9
3 8
2 6 5
1 5 1
6 2
8
"""


def printMtx(arr):
    for idX in range(len(arr[0])):
        printDia(arr, idX, 0, '')
    for idY in range(1, len(arr)):
        printDia(arr, len(arr[0])-1, idY, '')
    
def printDia(arr, idX, idY, res):
    while idY < len(arr) and idX >= 0:
        res += (str(arr[idY][idX]) + ' ')
        idY += 1
        idX -= 1
    print(res[:-1])        


printMtx([[9,3,2], [8,6,1], [5,5,6], [1,2,8]])
"""
9
3 8
2 6 5
1 5 1
6 2
8
"""
