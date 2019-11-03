
""" houseRobber -- 20min
You are planning to rob houses on a specific street, and you know that 
every house on the street has a certain amount of money hidden. The only 
thing stopping you from robbing all of them in one night is that adjacent 
houses on the street have a connected security system. The system will 
automatically trigger an alarm if two adjacent houses are broken into on 
the same night.

Given a list of non-negative integers nums representing the amount of money 
hidden in each house, determine the maximum amount of money you can rob in 
one night without triggering an alarm.

Example

For nums = [1, 1, 1], the output should be
houseRobber(nums) = 2.

The optimal way to get the most money in one night is to rob the first 
and the third houses for a total of 2.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer nums

An array representing the amount of money that each house on the street 
has.

Guaranteed constraints:
0 ≤ nums.length ≤ 100,
0 ≤ nums[i] ≤ 500.

[output] integer
"""

def houseRobber(nums):
    notAdj1, notAdj2 = 0, 0
    for i in nums:
        newNotAdj2 = notAdj2 if notAdj2>notAdj1 else notAdj1
        notAdj1 = notAdj2 + i
        notAdj2 = newNotAdj2
    return notAdj2 if notAdj2>notAdj1 else notAdj1

print(houseRobber([1, 1, 1])) #2
print(houseRobber([2, 7, 9, 3, 1])) # 12
print(houseRobber([82, 217, 170, 215, 153, 55, 185, 55, 185, 232, 69, 
131, 130, 102])) #1082
