
""" nextPermutation
Implement next permutation, which rearranges numbers into the lexicographically 
next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest 
possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its 
corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

"""

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        idx, idx2 =  -1, 0
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]: idx = i
        if idx == -1:
            nums.reverse()
            return
        for i in range(idx+1, len(nums)):
            if nums[i] > nums[idx]: idx2 = i
        nums[idx], nums[idx2] = nums[idx2], nums[idx]
        nums[idx+1:] = nums[:idx:-1]


# this function is not to return anything, but may test it by returning nums
#print(Solution().nextPermutation([1,2,3])) #[1,3,2]
#print(Solution().nextPermutation([1,3,2])) #[2,1,3]
#print(Solution().nextPermutation([3,2,1])) #[1,2,3]
