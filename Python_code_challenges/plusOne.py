
""" plusOne
Given a non-negative integer represented as a non-empty array of digits, 
plus one to the integer.

You may assume the integer do not contain any leading zero, except the 
number 0 itself.

The digits are stored such that the most significant digit is at the 
head of the list.
"""

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9: 
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits[0] = 1
        digits.append(0)
        return digits

print(Solution().plusOne([1, 0])) #[1, 1]

