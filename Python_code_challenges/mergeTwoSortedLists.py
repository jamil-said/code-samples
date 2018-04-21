
""" mergeTwoSortedLists
Merge two sorted linked lists and return it as a new list. The new list 
should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        myNode = temp = ListNode(None) 
        while l1 and l2:
            if l1.val < l2.val:
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
noder = (Solution.mergeTwoLists(Solution, ll1, ll2))
while noder:
    print(noder.val)
    noder = noder.next
#[1, 2, 3, 4, 5, 6]



