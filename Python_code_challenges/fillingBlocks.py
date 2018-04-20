
""" fillingBlocks -- 30 min
You have a block with the dimensions 4 × n. Find the number of different 
ways you can fill this block with smaller blocks that have the dimensions 
1 × 2. You are allowed to rotate the smaller blocks.

Example

For n = 1, the output should be
fillingBlocks(n) = 1.

There is only one possible way to arrange the smaller 1 × 2 blocks inside 
the 4 × 1 block.

For n = 4, the output should be
fillingBlocks(n) = 36.

Here are the 36 possible configuration of smaller blocks inside the 
4 × 4 block:


Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Guaranteed constraints:
0 ≤ n ≤ 21.

[output] integer

An integer representing the number of possible configurations of smaller 
blocks within the larger block.
"""

def fillingBlocks(n):
    patt, i = [1,1,5,11,36], 5
    if n < 5: return patt[n]
    else:
        for i in range(5, n+1):
            rslt = patt[i-1] + 5 * patt[i-2] + patt[i-3] - patt[i-4]
            patt.append(rslt)
    return patt[n]

print(fillingBlocks(4)) # 36
