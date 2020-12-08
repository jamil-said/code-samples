
""" sumInRange -- 20 min
You have an array of integers nums and an array queries, where queries[i]
is a pair of indices (0-based). Find the sum of the elements in nums from 
the indices at queries[i][0] to queries[i][1] (inclusive) for each query, 
then add all of the sums for all the queries together. Return that number 
modulo 109 + 7.

Example

For nums = [3, 0, -2, 6, -3, 2] and queries = [[0, 2], [2, 5], [0, 5]], 
the output should be sumInRange(nums, queries) = 10.

The array of results for queries is [1, 3, 6], so the answer is 1 + 3 + 
6 = 10.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer nums

An array of integers.

Guaranteed constraints:
1 ≤ nums.length ≤ 105,
-1000 ≤ nums[i] ≤ 1000.

[input] array.array.integer queries

An array containing sets of integers that represent the indices to query
in the nums array.

Guaranteed constraints:
1 ≤ queries.length ≤ 3 · 105,
queries[i].length = 2,
0 ≤ queries[i][j] ≤ nums.length - 1,
queries[i][0] ≤ queries[i][1].

[output] integer

An integer that is the sum of all of the sums gotten from querying nums, 
taken modulo 10^9 + 7.
"""

def sumInRange(nums, queries):
    runSum, memo, results = [0], 0, 0
    for i in range(len(nums)):
        memo += nums[i]
        runSum.append(memo)
    for q in queries:
        results += runSum[q[1] + 1] - runSum[q[0]]
    return results % 1000000007
        
print(sumInRange([3, 0, -2, 6, -3, 2], [[0, 2], [2, 5], [0, 5]])) #10
print(sumInRange([-20, -17, -32, -43, -8, -33, -15, -16, -42, -46, -23, -41, -11, -20, -46, -34, -38, -23, -30, -19], 
[[0,3], [1,2], [0,6], [0,1], [6,8], [4,9], [6,8], [1,6], [3,3], [0,2]])) #999999075
