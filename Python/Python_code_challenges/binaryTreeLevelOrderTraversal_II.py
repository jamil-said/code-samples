
""" binaryTreeLevelOrderTraversal II
Given a binary tree, return the bottom-up level order traversal of its 
nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        holder, result = [root], []
        return self.traverse(holder, result)
    
    def traverse(self, holder, result):
        if not holder: return result[::-1]
        tmp, tmp2 = [], []
        while holder:
            cur = holder.pop()
            if cur:
                tmp2.append(cur.val)
                tmp.append(cur)
        if tmp2: result.append(tmp2[::-1])
        holder = []
        while tmp:
            cur = tmp.pop()
            if cur.left: holder.append(cur.left)
            if cur.right: holder.append(cur.right)
        return self.traverse(holder, result)


#print(Solution().())
