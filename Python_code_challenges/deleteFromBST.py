
""" deleteFromBST -- 30 min.
A tree is considered a binary search tree (BST) if for each of its nodes 
the following is true:

The left subtree of a node contains only nodes with keys less than the 
node's key.
The right subtree of a node contains only nodes with keys greater than 
the node's key.
Both the left and the right subtrees must also be binary search trees.
Removing a value x from a BST t is done in the following way:

If there is no x in t, nothing happens;
Otherwise, let t' be a subtree of t such that t'.value = x.
If t' has a left subtree, remove the rightmost node from it and put it at 
the root of t';
Otherwise, remove the root of t' and its right subtree becomes the new 
t's root.
For example, removing 4 from the following tree has no effect because 
there is no such value in the tree:

    5
   / \
  2   6
 / \   \
1   3   8
       /
      7
Removing 5 causes 3 (the rightmost node in left subtree) to move to 
the root:

    3
   / \
  2   6
 /     \
1       8
       /
      7
And removing 6 after that creates the following tree:

    3
   / \
  2   8
 /   /
1   7
You're given a binary search tree t and an array of numbers queries. 
Your task is to remove queries[0], queries[1], etc., from t, step by step, 
following the algorithm above. Return the resulting BST.

Example

For

t = {
    "value": 5,
    "left": {
        "value": 2,
        "left": {
            "value": 1,
            "left": null,
            "right": null
        },
        "right": {
            "value": 3,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 6,
        "left": null,
        "right": {
            "value": 8,
            "left": {
                "value": 7,
                "left": null,
                "right": null
            },
            "right": null
        }
    }
}
and queries = [4, 5, 6], the output should be

deleteFromBST(t, queries) = {
    "value": 3,
    "left": {
        "value": 2,
        "left": {
            "value": 1,
            "left": null,
            "right": null
        },
        "right": null
    },
    "right": {
        "value": 8,
        "left": {
            "value": 7,
            "left": null,
            "right": null
        },
        "right": null
    }
}
Input/Output

[execution time limit] 4 seconds (py3)

[input] tree.integer t

A tree of integers.

Guaranteed constraints:
0 ≤ t size ≤ 1000,
-109 ≤ node value ≤ 109.

[input] array.integer queries

An array that contains the numbers to be deleted from t.

Guaranteed constraints:
1 ≤ queries.length ≤ 1000,
-109 ≤ queries[i] ≤ 109.

[output] tree.integer

The tree after removing all the numbers in queries, following the algorithm 
above.

"""

# Definition for binary tree:
class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def deleteFromBST(t, queries):
    for q in queries:
        t = calcTree(t, q)
    return t
    
def maxNode(t):
    if not t: return None
    while t.right:
        t = t.right
    return t.value

def delRight(t):
    if not t.right:
        return t.left
    else:
        t.right = delRight(t.right)
    return(t)

def calcTree(t, q):
    if not t: return None
    if q == t.value:
        if t.left:
            t.value = maxNode(t.left)
            t.left = delRight(t.left)
        else:
            t = t.right
    elif q < t.value:
        t.left = calcTree(t.left, q)
    elif q > t.value:
        t.right = calcTree(t.right, q)
    return(t)

### create tree for testing
tree1 = Tree(5)
tree1.left = Tree(2)
tree1.right = Tree(6)
tree1.left.left = Tree(1)
tree1.left.right = Tree(3)
tree1.right.right = Tree(8)
tree1.right.right.left = Tree(7)

#print tree response
printTree = deleteFromBST(tree1, [4, 5, 6])
print(printTree.value)
print(printTree.left.value)
print(printTree.right.value)
print(printTree.left.left.value)
print(printTree.right.left.value)
# 3 2 8 1 7
