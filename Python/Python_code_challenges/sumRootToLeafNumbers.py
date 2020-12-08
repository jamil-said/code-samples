
""" sumRootToLeafNumbers
Given a binary tree containing digits from 0-9 only, each root-to-leaf 
path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 
123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3


The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return Solution.calcSum(Solution, root, 0)

    def calcSum(self, root, result):
        if root is None: return 0
        result = (result*10 + root.val)
        if root.left is None and root.right is None:
            return result
        return Solution.calcSum(Solution, root.left, result) + Solution.calcSum(
        Solution, root.right, result)

# defining a tree for test
root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
print(Solution.sumNumbers(Solution, root)) # 218
