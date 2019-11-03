
""" mazeSmallestPathToTreasure
Given a maze (a 2d array), and considering that you can traverse the maze 
where the value is 1 and cannot traverse it when the value is 0, find the 
smallest path from the upper left corner of the maze to the treasure, 
which is hidden somewhere in the maze (the treasure has value 5, and there's 
only one treasure in the maze). If there's no viable path to the treasure, 
return -1. There are only 1, 0, and 5 values in the maze. Return an integer 
that represents the minimum path value which has to be traversed to arrive 
at the treasure.

For example:

maze = [[1, 0, 0], 
        [1, 0, 0], 
        [1, 5, 1]]
        
would return 3, as one would have to traverse the maze elements (0,0),
(1,0),(2,0) to arrive at the treasure located at (2,1)
"""

def mazeFind(maze):
    if not maze or not maze[0]: return -1
    if maze[0][0] == 5: return 0
    ok, result = set(), []
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1: ok.add((i,j))
            elif maze[i][j] == 5: tgt = (i,j)
    calc([], ok, tgt, set(), 0, 0, result)
    return sorted(result)[0]-1 if result else -1

def calc(path, ok, tgt, vis, i, j, result):
    if (i,j) == tgt: result.append(len(path+[1]))
    elif (i,j) not in ok or (i,j) in vis: return
    else:
        vis.add((i,j))
        calc(path+[1], ok, tgt, vis, i+1, j, result)
        calc(path+[1], ok, tgt, vis, i, j+1, result)
        calc(path+[1], ok, tgt, vis, i-1, j, result)
        calc(path+[1], ok, tgt, vis, i, j-1, result)
            

print(mazeFind([[1, 0, 0], [1, 0, 0], [1, 5, 1]])) #3
print(mazeFind([[1, 1, 1, 1], [0, 1, 1, 1], [0, 1, 0, 1], [1, 1, 5, 1], 
[0, 0, 1, 1]])) #5
print(mazeFind([[0, 0, 0], [1, 0, 0], [1, 5, 1]])) #-1
print(mazeFind([[5, 0, 0], [1, 0, 0], [1, 5, 1]])) # 0
print(mazeFind([[]])) # -1
print(mazeFind([])) # -1


