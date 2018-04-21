
""" isListPalindrome -- 30min
Note: Try to solve this task in O(n) time using O(1) additional space, 
where n is the number of elements in l, since this is what you'll be asked 
to do during an interview.

Given a singly linked list of integers, determine whether or not it's a 
palindrome.

Example

For l = [0, 1, 0], the output should be
isListPalindrome(l) = true;
For l = [1, 2, 2, 3], the output should be
isListPalindrome(l) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer l

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 5 · 105,
-109 ≤ element value ≤ 109.

[output] boolean

Return true if l is a palindrome, otherwise return false.
"""

# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None

def isListPalindrome(ll):
    listPalin = []
    while ll:
        listPalin.append(ll.value)
        ll = ll.next
    return listPalin == listPalin[::-1]


