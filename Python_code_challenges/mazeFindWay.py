
""" mazeFindWay
Given a maze (which is a 2d array with zeros and ones), find the way from 
the top-left corner to the bottom-right corner. You may traverse the array 
horizontally and vertically on "1" values, but cannot traverse on "0" values. 
Return an array with tuples of every value on the path from the top-left corner 
to the bottom-right corner. If the maze has no possible path to target, 
return an empty array. The Maze is guaranteed to have at least one value.

Example:
mazeFW([[1, 0, 0, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 1, 0],
        [1, 1, 1, 1, 1]])
Should return:
[(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (4, 3), (4, 4)]
"""

def mazeFW(arr):
    ok, tgt = set(), (len(arr)-1, len(arr[0])-1)
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 1: ok.add((i, j))
    result = calc([], ok, tgt, set(), 0, 0)
    return result if result else []

def calc(path, ok, tgt, tried, i, j):
    if (i, j) not in ok or (i, j) in tried: return
    elif (i, j) == tgt and (i, j) in ok: return path+[(i, j)]
    else: 
        tried.add((i, j))
        return calc(path+[(i, j)], ok, tgt, tried, i+1, j) or \
        calc(path+[(i, j)], ok, tgt, tried, i, j+1) or\
        calc(path+[(i, j)], ok, tgt, tried, i-1, j) or\
        calc(path+[(i, j)], ok, tgt, tried, i, j-1)
        
print(mazeFW([
        [1, 0, 0, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 1, 0],
        [1, 1, 1, 1, 1]])) 
# [(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (4, 3), (4, 4)]
print(mazeFW([
        [1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 0],
        [1, 1, 0, 0, 0, 0],
        [1, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 1],
        [1, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 0, 1]])) 
"""
 [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (2, 3), (2, 2) 
 , (2, 1), (3, 1), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (8, 1) 
 , (8, 2), (8, 3), (7, 3), (6, 3), (6, 2), (5, 2), (4, 2), (4, 3), (4, 4)
 , (4, 5), (5, 5), (6, 5), (7, 5), (8, 5)]
"""
print(mazeFW([[1, 1, 1]])) # [(0, 0), (0, 1), (0, 2)]
print(mazeFW([[1, 1, 1],
              [1, 1, 1],
              [1, 1, 1]])) # [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
print(mazeFW([[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]])) # []
print(mazeFW([[1]])) # [(0, 0)]
print(mazeFW([[0]])) # []
