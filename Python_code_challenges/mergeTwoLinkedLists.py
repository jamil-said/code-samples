
""" mergeTwoLinkedLists -- 30 min
Note: Your solution should have O(l1.length + l2.length) time complexity, 
since this is what you will be asked to accomplish in an interview.

Given two singly linked lists sorted in non-decreasing order, your task 
is to merge them. In other words, return a singly linked list, also sorted 
in non-decreasing order, that contains the elements from both original lists.

Example

For l1 = [1, 2, 3] and l2 = [4, 5, 6], the output should be
mergeTwoLinkedLists(l1, l2) = [1, 2, 3, 4, 5, 6];
For l1 = [1, 1, 2, 4] and l2 = [0, 3, 5], the output should be
mergeTwoLinkedLists(l1, l2) = [0, 1, 1, 2, 3, 4, 5].
Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer l1

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 104,
-109 ≤ element value ≤ 109.

[input] linkedlist.integer l2

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 104,
-109 ≤ element value ≤ 109.

[output] linkedlist.integer

A list that contains elements from both l1 and l2, sorted in non-decreasing 
order.
"""

# Definition for singly-linked list:
class ListNode(object):
   def __init__(self, x):
     self.value = x
     self.next = None

def mergeTwoLinkedLists(l1, l2):
    myNode = temp = ListNode(None) 
    while l1 and l2:
        if l1.value < l2.value:
            current = l1
            l1 = l1.next
        else:
            current = l2
            l2 = l2.next
        temp.next = current          
        temp = temp.next
    temp.next = l1 or l2
    return myNode.next


# create linked list for testing
ll1 = ListNode(1)
ll1.next = ListNode(2)
ll1.next.next = ListNode(3)

ll2 = ListNode(4)
ll2.next = ListNode(5)
ll2.next.next = ListNode(6)

#test module:
noder = (mergeTwoLinkedLists(ll1, ll2))
while noder:
    print(noder.value)
    noder = noder.next
#[1, 2, 3, 4, 5, 6]


