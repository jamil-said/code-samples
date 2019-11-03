
""" sortedArrayToBinarySearchTree
Given an array where elements are sorted in ascending order, convert it 
to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary 
tree in which the depth of the two subtrees of every node never differ 
by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following 
height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: return
        rootI = (len(nums))//2
        root = TreeNode(nums[rootI])
        root.left = self.sortedArrayToBST(nums[:rootI])
        root.right = self.sortedArrayToBST(nums[rootI+1:])
        return root
        

result = Solution().sortedArrayToBST([-10,-3,0,5,9])
print(result.val) # 0
print(result.left.val) # -3
print(result.right.val) # 9
print(result.left.left.val) # -10
print(result.right.left.val) # 5






