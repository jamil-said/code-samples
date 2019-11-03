
""" combinationSum -- 40 min
Given an array of integers a and an integer sum, find all of the unique 
combinations in a that add up to sum.
The same number from a can be used an unlimited number of times in a 
combination.
Elements in a combination (a1 a2 … ak) must be sorted in non-descending 
order, while the combinations themselves must be sorted in ascending order.
If there are no possible combinations that add up to sum, the output 
should be the string "Empty".

Example

For a = [2, 3, 5, 9] and sum = 9, the output should be
combinationSum(a, sum) = "(2 2 2 3)(2 2 5)(3 3 3)(9)".

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer a

An array of positive integers.

Guaranteed constraints:
1 ≤ a.length ≤ 12,
1 ≤ a[i] ≤ 9.

[input] integer sum

Guaranteed constraints:
1 ≤ sum ≤ 30.

[output] string

All possible combinations that add up to a given sum, or "Empty" if 
there are no possible combinations.
"""

def combinationSum(arr, sumNum):
    results, strRslt = [], ''
    arr = list(set(arr))
    arr.sort()
    calcComb(arr, sumNum, 0, [], results)
    if len(results) == 0: return 'Empty'
    for i in results:
        strRslt += str(tuple(i)).replace(',','')
    return strRslt
    
def calcComb(nums, sumNum, idx, path, results):
    if sumNum < 0: return
    if sumNum == 0:
        results.append(path)
        return 
    for i in range(idx, len(nums)):
        calcComb(nums, sumNum-nums[i], i, path+[nums[i]], results)

print(combinationSum([2, 3, 5, 9], 9)) #(2 2 2 3)(2 2 5)(3 3 3)(9)
