
""" reverseNodesInKGroups -- 45 min.
Note: Your solution should have O(n) time complexity, where n is the 
number of element in l, and O(1) additional space complexity, since this 
is what you would be asked to accomplish in an interview.

Given a linked list l, reverse its nodes k at a time and return the modified 
list. k is a positive integer that is less than or equal to the length of l. 
If the number of nodes in the linked list is not a multiple of k, then the 
nodes that are left out at the end should remain as-is.

You may not alter the values in the nodes - only the nodes themselves can 
be changed.

Example

For l = [1, 2, 3, 4, 5] and k = 2, the output should be
reverseNodesInKGroups(l, k) = [2, 1, 4, 3, 5];
For l = [1, 2, 3, 4, 5] and k = 1, the output should be
reverseNodesInKGroups(l, k) = [1, 2, 3, 4, 5];
For l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] and k = 3, the output should 
be reverseNodesInKGroups(l, k) = [3, 2, 1, 6, 5, 4, 9, 8, 7, 10, 11].
Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer l

A singly linked list of integers.

Guaranteed constraints:
1 ≤ list size ≤ 104,
-109 ≤ element value ≤ 109.

[input] integer k

The size of the groups of nodes that need to be reversed.

Guaranteed constraints:
1 ≤ k ≤ l size.

[output] linkedlist.integer

The initial list, with reversed groups of k elements.

"""

# Definition for singly-linked list:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

def reverseNodesInKGroups(ll, k):
    if not ll or k < 2: return ll
    revList = ll
    for i in range(k - 1):
        revList = revList.next
        if revList is None: return ll
    prev, current = None, ll
    for i in range(k):
        newNext = current.next
        current.next = prev
        prev, current = current, newNext
    ll.next = reverseNodesInKGroups(current, k)
    return revList


# create linked list for testing
ll = ListNode(1)
ll.next = ListNode(2)
ll.next.next = ListNode(3)
ll.next.next.next = ListNode(4)
ll.next.next.next.next = ListNode(5)

#test module:
noder = (reverseNodesInKGroups(ll, 2))
testTemp = []
while noder:
    testTemp.append(noder.value)
    noder = noder.next
print(testTemp)
#[2, 1, 4, 3, 5]




