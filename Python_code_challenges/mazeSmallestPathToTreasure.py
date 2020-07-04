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

# I think this solution is right, but it was not tested with a large test case
def mazeFind(maze):
    if not maze or not maze[0]: 
        return -1
    result = []
    calc([], maze, set(), 0, 0, result)
    return result[0] if result else -1

def calc(path, maze, vis, i, j, result):
    if (i,j) in vis: 
        return
    elif (i >= len(maze) or i < 0) or (j >= len(maze[0]) or j < 0) or (maze[i][j] == 0):
        return 
    elif result and len(path) >= result[0]:
        return
    if maze[i][j] == 5: 
        if result:
            result[0] = min(len(path),result[0])
        else:
            result.append(len(path))
    else:
        visCopy = vis.copy()
        visCopy.update([(i,j)])
        calc(path+[1], maze, visCopy, i+1, j, result)
        calc(path+[1], maze, visCopy, i, j+1, result)
        calc(path+[1], maze, visCopy, i-1, j, result)
        calc(path+[1], maze, visCopy, i, j-1, result)
            

print(mazeFind([[1, 0, 0], [1, 0, 0], [1, 5, 1]])) #3
print(mazeFind([[1, 1, 1, 1], 
                [0, 1, 1, 1], 
                [0, 1, 0, 1], 
                [1, 1, 5, 1], 
                [0, 0, 1, 1]])) #5
print(mazeFind([[0, 0, 0], [1, 0, 0], [1, 5, 1]])) #-1
print(mazeFind([[5, 0, 0], [1, 0, 0], [1, 0, 1]])) # 0
print(mazeFind([[]])) # -1
print(mazeFind([])) # -1
print(mazeFind([[1,1,1,1,1,1],
                [1,0,0,0,1,1],
                [1,0,5,0,1,1],
                [1,1,1,0,1,1],
                [1,1,1,1,1,1],
                [1,1,1,1,1,1]])) #6
print(mazeFind([[1,1,1,1,1,1],
                [1,0,0,0,1,1],
                [1,0,5,0,1,1],
                [1,0,1,0,1,1],
                [1,1,1,0,1,1],
                [1,1,1,1,1,1]])) #8
