
""" climbingStaircase -- 30 min
You need to climb a staircase that has n steps, and you decide to get 
some extra exercise by jumping up the steps. You can cover at most k 
steps in a single jump. Return all the possible sequences of jumps that 
you could take to climb the staircase, sorted.

Example

For n = 4 and k = 2, the output should be

climbingStaircase(n, k) =
[[1, 1, 1, 1],
 [1, 1, 2],
 [1, 2, 1],
 [2, 1, 1],
 [2, 2]]
There are 4 steps in the staircase, and you can jump up 2 or fewer steps 
at a time. There are 5 potential sequences in which you jump up the stairs 
either 2 or 1 at a time.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Guaranteed constraints:
0 ≤ n ≤ 10.

[input] integer k

Guaranteed constraints:
0 ≤ k ≤ n.

[output] array.array.integer

An array containing all of the possible sequences in which you could climb 
n steps by taking them k or fewer at a time.
"""

def climbingStaircase(n, k):
    results = []
    calcSteps(results, [], k, n)
    return results
        
def calcSteps(results, steps, k, remain):
    if remain == 0:
        results.append(list(steps))
    else:
        for i in range(1, k+1):
            if i <= remain:
                steps.append(i)
                calcSteps(results, steps, k, remain-i)
                steps.pop()


print(climbingStaircase(4, 2))
"""
[[1, 1, 1, 1],
 [1, 1, 2],
 [1, 2, 1],
 [2, 1, 1],
 [2, 2]]
"""
#print(climbingStaircase(7, 3))
"""
[[1,1,1,1,1,1,1], 
 [1,1,1,1,1,2], 
 [1,1,1,1,2,1], 
 [1,1,1,1,3], 
 [1,1,1,2,1,1], 
 [1,1,1,2,2], 
 [1,1,1,3,1], 
 [1,1,2,1,1,1], 
 [1,1,2,1,2], 
 [1,1,2,2,1], 
 [1,1,2,3], 
 [1,1,3,1,1], 
 [1,1,3,2], 
 [1,2,1,1,1,1], 
 [1,2,1,1,2], 
 [1,2,1,2,1], 
 [1,2,1,3], 
 [1,2,2,1,1], 
 [1,2,2,2], 
 [1,2,3,1], 
 [1,3,1,1,1], 
 [1,3,1,2], 
 [1,3,2,1], 
 [1,3,3], 
 [2,1,1,1,1,1], 
 [2,1,1,1,2], 
 [2,1,1,2,1], 
 [2,1,1,3], 
 [2,1,2,1,1], 
 [2,1,2,2], 
 [2,1,3,1], 
 [2,2,1,1,1], 
 [2,2,1,2], 
 [2,2,2,1], 
 [2,2,3], 
 [2,3,1,1], 
 [2,3,2], 
 [3,1,1,1,1], 
 [3,1,1,2], 
 [3,1,2,1], 
 [3,1,3], 
 [3,2,1,1], 
 [3,2,2], 
 [3,3,1]]
"""

