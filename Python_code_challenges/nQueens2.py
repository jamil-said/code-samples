
"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard 
such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' 
placement, where 'Q' and '.' both indicate a queen and an empty space 
respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""

class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        partialR, tempLst, results = [], [], []
        def calcQueen(cols, forbMinus, forbPlus):
            lenC = len(cols)
            if lenC == n:
                partialR.append(cols)
                return None
            for q in range(1, n+1):
                if (q not in cols and lenC-q not in forbMinus and lenC+q not 
                in forbPlus):
                    calcQueen(cols+[q], forbMinus+[lenC-q], forbPlus+[lenC+q])  
        calcQueen([],[],[])
        for pr in partialR:
            for pru in pr:
                row = '.' * (pru-1) + 'Q' + '.' * (n-pru)
                tempLst.append(row)
            results.append(tempLst)
            tempLst = []
        return results

print(Solution.solveNQueens(Solution, 4))
"""
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""
