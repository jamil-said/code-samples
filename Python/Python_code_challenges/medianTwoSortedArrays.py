
""" medianTwoSortedArrays
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity 
should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1) % 2 != 0: return float(nums1[len(nums1)//2])
        return (nums1[len(nums1)//2 - 1] + nums1[len(nums1)//2])/2

print(Solution().findMedianSortedArrays([1, 3], [2])) #2.0
print(Solution().findMedianSortedArrays([1, 2], [3, 4])) #2.5


""" alternative, slower, longer
class Solution:
    def findMedianSortedArrays(self, n1, n2):
        len1, len2 = len(n1), len(n2)
        if (len1 + len2) % 2 == 1: 
            return self.calcM(n1, n2, (len1 + len2)//2 + 1)
        else:
            return (self.calcM(n1, n2, (len1 + len2)//2) + \
                    self.calcM(n1, n2, (len1 + len2)//2 + 1)) * 0.5

    def calcM(self, num1, num2, idx):
        l1, l2 = len(num1), len(num2)
        if l1 > l2: return self.calcM(num2, num1, idx)
        left, right = 0, l1    
        while left < right:
            mid = left + (right - left) // 2
            if 0 <= idx-1-mid < l2 and num1[mid] >= num2[idx-1-mid]: right = mid
            else: left = mid + 1
        num1Val = num1[left-1] if left-1 >= 0 else float("-inf")
        num2Val = num2[idx-1-left] if idx-1-left >= 0 else float("-inf")
        return float(max(num1Val, num2Val))
"""
