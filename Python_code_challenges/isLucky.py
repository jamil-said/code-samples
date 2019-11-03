
""" isLucky -- 10 min
Ticket numbers usually consist of an even number of digits. A ticket 
number is considered lucky if the sum of the first half of the digits is 
equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
isLucky(n) = true;
For n = 239017, the output should be
isLucky(n) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

A ticket number represented as a positive integer with an even number of 
digits.

Guaranteed constraints:
10 ≤ n < 106.

[output] boolean

true if n is a lucky ticket number, false otherwise.
"""

def isLucky(n):
    lstN, sum1, sum2 = list(str(n)), 0, 0
    if len(lstN) % 2 != 0: return False
    for n in range(len(lstN)//2): 
        sum1 += int(lstN[n])
        sum2 += int(lstN[len(lstN)-1-n])
    return sum1 == sum2

print(isLucky(1230)) # True
print(isLucky(239017)) # False

