""" addTwoHugeNumbers -- 30min
You're given 2 huge integers represented by linked lists. Each linked 
list element is a number from 0 to 9999 that represents a number with 
exactly 4 digits. The represented number might have leading zeros. Your 
task is to add up these huge integers and return the result in the same 
format.

Example

For a = [9876, 5432, 1999] and b = [1, 8001], the output should be
addTwoHugeNumbers(a, b) = [9876, 5434, 0].

Explanation: 987654321999 + 18001 = 987654340000.

For a = [123, 4, 5] and b = [100, 100, 100], the output should be
addTwoHugeNumbers(a, b) = [223, 104, 105].

Explanation: 12300040005 + 10001000100 = 22301040105.

Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer a

The first number, without its leading zeros.

Guaranteed constraints:
0 ≤ a size ≤ 104,
0 ≤ element value ≤ 9999.

[input] linkedlist.integer b

The second number, without its leading zeros.

Guaranteed constraints:
0 ≤ b size ≤ 104,
0 ≤ element value ≤ 9999.

[output] linkedlist.integer

The result of adding a and b together, returned without leading zeros in 
the same format.
"""

# Definition for singly-linked list:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

def addTwoHugeNumbers(a, b):
    n1, n2 = a.value, b.value
    a, b = a.next, b.next
    c = ListNode(0)
    while a:
        n1 *= 10000
        n1 += a.value
        a = a.next
    while b:
        n2 *= 10000
        n2 += b.value
        b = b.next
    n3 = n1 + n2
    while True:
        c.value = n3 % 10000
        n3 //= 10000
        if n3 == 0:
            break
        d = ListNode(0)
        d.next = c
        c = d
    return c


""" alternative, probably slower, more complicated

def addTwoHugeNumbers(a, b):
    numA, numB = a.value, b.value
    currentA, currentB = a.next, b.next
    llResult = ListNode(0)
    currNodeResul = llResult
    while currentA:
        numA = numA * 10000 + currentA.value
        currentA = currentA.next
    while currentB:
        numB = numB * 10000 + currentB.value
        currentB = currentB.next
    sumABStr = str(numA + numB)
    modLen = 4 - (len(sumABStr) % 4)
    if modLen != 4:
        sumABStr = '0' * modLen + sumABStr
    for i in range (0, len(sumABStr), 4):
        currValue = int(sumABStr[i:i+4])
        currNodeResul.value = currValue
        if i + 4 < len(sumABStr):
            currNodeResul.next = ListNode(0)
            currNodeResul = currNodeResul.next                     
    return llResult

"""
