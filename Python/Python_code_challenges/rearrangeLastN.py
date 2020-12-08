
""" rearrangeLastN -- 40 min
Note: Try to solve this task in O(list size) time using O(1) additional 
space, since this is what you'll be asked during an interview.

Given a singly linked list of integers l and a non-negative integer n, 
move the last n list nodes to the beginning of the linked list.

Example

For l = [1, 2, 3, 4, 5] and n = 3, the output should be
rearrangeLastN(l, n) = [3, 4, 5, 1, 2];
For l = [1, 2, 3, 4, 5, 6, 7] and n = 1, the output should be
rearrangeLastN(l, n) = [7, 1, 2, 3, 4, 5, 6].
Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer l

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 105,
-1000 ≤ element value ≤ 1000.

[input] integer n

A non-negative integer.

Guaranteed constraints:
0 ≤ n ≤ list size.

[output] linkedlist.integer

Return l with the n last elements moved to the beginning.

"""

# Definition for singly-linked list:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

def rearrangeLastN(head, n):
    lstNodes, current = [], head
    while current:
        lstNodes.append(current)
        current = current.next
    if not lstNodes or not n or len(lstNodes) == n: return head
    if len(lstNodes) > n: lstNodes = lstNodes[-n-1:]
    newEnd = lstNodes.pop(0)
    newEnd.next = None
    newHead = lstNodes[0]
    if len(lstNodes) == 1:
        newHead.next = head
        return newHead
    lstNodes = lstNodes[::-1]
    while len(lstNodes) >= 2:
        currNodeChg = lstNodes.pop()
        currNodeChg2 = lstNodes.pop()
        currNodeChg.next = currNodeChg2
    if lstNodes:
        currNodeChg2.next = lstNodes.pop()
        currNodeChg2.next.next = head
    else: currNodeChg2.next = head
    return newHead

# create linked list for testing
ll1 = ListNode(1)
ll1.next = ListNode(2)
ll1.next.next = ListNode(3)
ll1.next.next.next = ListNode(4)
ll1.next.next.next.next = ListNode(5)

#test module:
noder = (rearrangeLastN(ll1, 3))
while noder:
    print(noder.value)
    noder = noder.next
"""
3
4
5
1
2
"""
