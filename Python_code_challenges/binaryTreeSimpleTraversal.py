
""" binaryTreeSimpleTraversal
Given a binary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, all stored in order in an array).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:

[3, 9, 20, 15, 7]
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        holder, result = deque([root]), []
        while holder:
            cur = holder.popleft()
            result.append(cur.val)
            if cur.left: holder.append(cur.left)
            if cur.right: holder.append(cur.right)
        return result

# Creating tree for test
node = TreeNode(3)
node.left = TreeNode(9)
node.right = TreeNode(20)
node.right.left = TreeNode(15)
node.right.right = TreeNode(7)

print(Solution().levelOrder(node)) #[3, 9, 20, 15, 7]
