
""" composeRanges -- 15min
Given a sorted integer array that does not contain any duplicates, 
return a summary of the number ranges it contains.

Example

For nums = [-1, 0, 1, 2, 6, 7, 9], the output should be
composeRanges(nums) = ["-1->2", "6->7", "9"].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer nums

A sorted array of unique integers.

Guaranteed constraints:
0 ≤ nums.length ≤ 15,
-(231 - 1) ≤ nums[i] ≤ 231 - 1.

[output] array.string
"""

def composeRanges(nums):
    if not nums: return []
    results, start, end = [], nums[0], nums[0]
    for i in range(1, len(nums) + 1):
        if i < len(nums) and nums[i] == end + 1:
            end = nums[i]
        else:
            tempStr = str(start)
            if start != end:
                tempStr += '->' + str(end)
            results.append(tempStr)
            if i < len(nums):
                start, end = nums[i], nums[i]
    return results
            
print(composeRanges([-1, 0, 1, 2, 6, 7, 9])) #["-1->2", "6->7", "9"]            
print(composeRanges([0, 1])) #["0->1"]

