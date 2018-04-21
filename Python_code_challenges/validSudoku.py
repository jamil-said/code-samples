
""" validSudoku
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled 
with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only 
the filled cells need to be validated. 
"""

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.checkRows(board) and self.checkCols(board) and \
        self.checkLst3x3(board)

    def checkRows(self, board):
        for row in board:
            cleanRow = [x for x in row if x.isdigit()]
            if len(cleanRow) != len(set(cleanRow)):
                return False
        return True

    def checkCols(self, board):
        rotatedGrid = list(zip(*board[::-1]))
        for row in rotatedGrid:
            cleanRow = [x for x in row if x.isdigit()]
            if len(cleanRow) != len(set(cleanRow)):
                return False
        return True

    def checkLst3x3(self, board):
        temp = []
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                new_3x3 = [item[i:i+3] for item in board[j:j+3]]
                for row in new_3x3:
                    cleanRow = [x for x in row if x.isdigit()]
                    temp.extend(cleanRow)
                if len(temp) != len(set(temp)):
                    return False
                temp = []
        return True
