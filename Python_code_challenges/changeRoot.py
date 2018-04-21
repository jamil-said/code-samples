
"""  25min -- changeRoot
You are given an array parent of length n specifying a tree. The vertices 
of the tree are numbered from 0 to n - 1 and parent[i] is the parent of 
the ith node. The root of the tree is the vertex v, the parent of which 
is the same vertex (i.e. parent[v] = v if and only if v is a root).

What will the parent array look like if the edges remain the same but tree 
is rooted at the other vertex newRoot?

Example

For parent = [0, 0, 0, 1] and newRoot = 1, the output should be
changeRoot(parent, newRoot) = [1, 1, 0, 1].

Check out the image below for better understanding:

For parent = [0, 0, 0, 1, 1, 1, 2, 2, 7] and newRoot = 7, the output 
should be  changeRoot(parent, newRoot) = [2, 0, 7, 1, 1, 1, 2, 7, 7].

This is what the tree looks like in the beginning:

                      0
                  1       2
               3  4  5    6   7
                              8

And this is what it looks when we change the root to the vertex 7:
                       7
                   2       8     
                 0   6
                 1
              3  4  5

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer parent

The array of parents.

Guaranteed constraints:
4 ≤ parent.length ≤ 50,
0 ≤ parent[i] < parent.length.

[input] integer newRoot

The new root of the tree. It is guaranteed that it is different from 
initial root.

Guaranteed constraints:
0 ≤ newRoot < parent.length - 1.

[output] array.integer

The array of parents after changing the root.
"""

def changeRoot(parent, newR):
    oldPar = parent[:]
    parent[newR] = newR
    while True:
        newR2 = oldPar[newR]
        if newR2 == newR:
            return parent
        else: 
            tempR, parent[newR2] = parent[newR2], newR
            newR, newR2 = newR2, tempR

print(changeRoot([5, 3, 0, 5, 10, 5, 5, 0, 10, 10, 0, 13, 3, 3, 2], 8)) 
#[10, 3, 0, 5, 10, 0, 5, 0, 8, 10, 8, 13, 3, 3, 2]
print(changeRoot([0, 0, 0, 1], 1)) #[1, 1, 0, 1]
print(changeRoot([0, 0, 0, 1, 1, 1, 2, 2, 7], 7)) #[2, 0, 7, 1, 1, 1, 2, 7, 7]
print(changeRoot([0, 0, 0, 1, 1, 1, 2, 2, 7, 7], 2)) #[2, 0, 2, 1, 1, 1, 2, 2, 7, 7]
print(changeRoot([3, 3, 2, 2, 0], 0)) #[0, 3, 3, 0, 0]
print(changeRoot([8, 6, 8, 8, 7, 6, 8, 8, 8, 7], 7)) #[8, 6, 8, 8, 7, 6, 8, 7, 7, 7]



