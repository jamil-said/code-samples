
"""climbingStairs -- 15 min
You are climbing a staircase that has n steps. You can take the steps 
either 1 or 2 at a time. Calculate how many distinct ways you can climb 
to the top of the staircase.

Example

For n = 1, the output should be
climbingStairs(n) = 1;

For n = 2, the output should be
climbingStairs(n) = 2.

You can either climb 2 steps at once or climb 1 step two times.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Guaranteed constraints:
1 ≤ n ≤ 50.

[output] integer

It's guaranteed that the answer will fit in a 32-bit integer.
"""

def climbingStairs(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a

print(climbingStairs(38)) #63245986
