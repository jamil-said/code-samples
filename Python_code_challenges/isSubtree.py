
""" isSubtree -- 30min
Given two binary trees t1 and t2, determine whether the second tree is a 
subtree of the first tree. A subtree for vertex v in a binary tree t is a 
tree consisting of v and all its descendants in t. Determine whether or not 
there is a vertex v (possibly none) in tree t1 such that a subtree for 
vertex v (possibly empty) in t1 equals t2.

Example

For

t1 = {
    "value": 5,
    "left": {
        "value": 10,
        "left": {
            "value": 4,
            "left": {
                "value": 1,
                "left": null,
                "right": null
            },
            "right": {
                "value": 2,
                "left": null,
                "right": null
            }
        },
        "right": {
            "value": 6,
            "left": null,
            "right": {
                "value": -1,
                "left": null,
                "right": null
            }
        }
    },
    "right": {
        "value": 7,
        "left": null,
        "right": null
    }
}
and

t2 = {
    "value": 10,
    "left": {
        "value": 4,
        "left": {
            "value": 1,
            "left": null,
            "right": null
        },
        "right": {
            "value": 2,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 6,
        "left": null,
        "right": {
            "value": -1,
            "left": null,
            "right": null
        }
    }
}
the output should be isSubtree(t1, t2) = true.

This is what these trees look like:

      t1:             t2:
       5              10
      / \            /  \
    10   7          4    6
   /  \            / \    \
  4    6          1   2   -1
 / \    \
1   2   -1
As you can see, t2 is a subtree of t1 (the vertex in t1 with value 10).

For

t1 = {
    "value": 5,
    "left": {
        "value": 10,
        "left": {
            "value": 4,
            "left": {
                "value": 1,
                "left": null,
                "right": null
            },
            "right": {
                "value": 2,
                "left": null,
                "right": null
            }
        },
        "right": {
            "value": 6,
            "left": {
                "value": -1,
                "left": null,
                "right": null
            },
            "right": null
        }
    },
    "right": {
        "value": 7,
        "left": null,
        "right": null
    }
}
and

t2 = {
    "value": 10,
    "left": {
        "value": 4,
        "left": {
            "value": 1,
            "left": null,
            "right": null
        },
        "right": {
            "value": 2,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 6,
        "left": null,
        "right": {
            "value": -1,
            "left": null,
            "right": null
        }
    }
}
the output should be isSubtree(t1, t2) = false.

This is what these trees look like:

        t1:            t2:
         5             10
       /   \          /  \
     10     7        4    6
   /    \           / \    \
  4     6          1   2   -1
 / \   / 
1   2 -1
As you can see, there is no vertex v such that the subtree of t1 for 
vertex v equals t2.

For

t1 = {
    "value": 1,
    "left": {
        "value": 2,
        "left": null,
        "right": null
    },
    "right": {
        "value": 2,
        "left": null,
        "right": null
    }
}
and

t2 = {
    "value": 2,
    "left": {
        "value": 1,
        "left": null,
        "right": null
    },
    "right": null
}
the output should be isSubtree(t1, t2) = false.

Input/Output

[execution time limit] 4 seconds (py3)

[input] tree.integer t1

A binary tree of integers.

Guaranteed constraints:
0 ≤ tree size ≤ 6 · 104,
-1000 ≤ node value ≤ 1000.

[input] tree.integer t2

Another binary tree of integers.

Guaranteed constraints:
0 ≤ tree size ≤ 6 · 104,
-1000 ≤ node value ≤ 1000.

[output] boolean

Return true if t2 is a subtree of t1, otherwise return false.
"""

# Definition for binary tree:
class Tree(object):
    def __init__(self, x):
         self.value = x
         self.left = None
         self.right = None

def isSubtree(t1, t2):
    if not t2: return True
    if not t1: return False
    if checkTree(t1, t2): return True
    return isSubtree(t1.left, t2) or isSubtree(t1.right, t2)

def checkTree(t, s):
    if not t and not s: return True
    if not t or not s: return False
    return (t.value == s.value and checkTree(t.left , s.left) and
            checkTree(t.right, s.right)) 

### create tree for testing
tree1 = Tree(1)
tree1.left = Tree(2)
tree1.left.left = Tree(None)
tree1.left.right = Tree(None)
tree1.right = Tree(2)
tree2 = Tree(2)
tree2.left = Tree(1)
tree2.left.left = Tree(None)
tree2.left.right = Tree(None)
tree2.right = Tree(None)

print(isSubtree(tree1, tree2)) # False

