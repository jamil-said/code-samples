
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

def printMtx(mtx):
    if not mtx or not mtx[0]: 
        print('')
        return
    startD = []
    for i in range(len(mtx[0])):
        startD.append([0, i])
    for i in range(1, len(mtx)):
        startD.append([i, len(mtx[0])-1])
    printDia(mtx, startD)
        
def printDia(mtx, startD):
    tmpStr = ''
    for a in startD:
        row, col = a[0], a[1]
        tmpStr += str(mtx[row][col]) + ' '
        while row < len(mtx)-1 and col > 0:
            row += 1
            col -= 1
            tmpStr += str(mtx[row][col]) + ' '
        print(tmpStr)
        tmpStr = ''
    
print(printMtx([[9,3,2], [8,6,1], [5,5,6], [1,2,8]]))
"""
9
3 8
2 6 5
1 5 1
6 2
8
"""
