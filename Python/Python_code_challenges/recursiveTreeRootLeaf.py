
""" 30min -- recursiveNotationTreeRootLeaf
You are given a recursive notation of a binary tree: each node of a tree 
is represented as a set of three elements:

value of the node;
left subtree;
right subtree.
So, a tree can be written as (value left_subtree right_subtree). If a 
node doesn't exist then it is represented as an empty set: (). For example, 
here is a representation of a tree in the given picture:

(2 (7 (2 () ()) (6 (5 () ()) (11 () ()))) (5 () (9 (4 () ()) ())))
               2
            7     5
          2   6      9
             3 11   4


Your task is to obtain a list of nodes, that are the most distant from the 
tree root, in the order from left to right.

In the notation of a node its value and subtrees are separated by exactly 
one space character.

Example

For

tree = "(2 (7 (2 () ()) (6 (5 () ()) (11 () ()))) (5 () (9 (4 () ()) ())))"
the output should be
treeBottom(tree) = [5, 11, 4].

Input/Output

[execution time limit] 4 seconds (py3)

[input] string tree

Guaranteed constraints:
5 ≤ tree.length ≤ 120.

[output] array.integer
"""

def treeBottom(tree):
    level, levelMax, dicLevel, tempR, result = 0, 0, {}, [], []
    for i, c in enumerate(tree):
        if c == '(': 
            level += 1
            if level not in dicLevel: dicLevel[level] = [i]
            else: dicLevel[level].append(i) 
            if level > levelMax: levelMax = level
        elif c == ')': 
            dicLevel[level].append(i)
            level -= 1
    while levelMax > 0:
        cLevel = dicLevel[levelMax]
        for i in range(0, len(cLevel), 2):
            if any(ch.isdigit() for ch in tree[cLevel[i]+1:cLevel[i+1]-1]):
                tempR.append(tree[cLevel[i]+1:cLevel[i+1]-1])
        if tempR:
            for r in tempR: 
                result.append(int(''.join(c for c in r if c.isdigit())))
            return result
        levelMax -= 1
    return []

print(treeBottom('(2 (7 (2 () ()) (6 (5 () ()) (11 () ()))) (5 () (9 (4 () ()) ())))'))
# [5,11,4]

