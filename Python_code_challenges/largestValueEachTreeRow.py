
""" largestValueEachTreeRow
You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largestValues(self, t):
        """
        :type t: TreeNode
        :rtype: List[int]
        """
        results, tree = [], [t]
        while any(tree): 
            results.append(max(node.val for node in tree))
            tempHolder = []
            for node in tree:
                for child in (node.left, node.right):
                    if child: tempHolder.append(child)
            tree = tempHolder
        return results

# create tree for testing
t = TreeNode(1)
t.left = TreeNode(3)
t.right = TreeNode(2)
t.left.left = TreeNode(5)
t.left.right = TreeNode(3)
t.right.right = TreeNode(9)

print(Solution().largestValues(t)) # [1, 3, 9]

