
""" removeNthNodeEndList
Given a linked list, remove the nth node from the end of list and return 
its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 
   1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        start = end = dummy
        for i in range(n): 
            end = end.next
        while end.next:
            end = end.next
            start = start.next
        start.next = start.next.next
        return dummy.next 

""" alternative, more complex & slower
from collections import deque
class Solution:
    def removeNthFromEnd(self, head, n):
        count, curr, hold = 0, head, deque([])
        while curr:
            hold.append(curr)
            if len(hold) > n+1: hold.popleft()
            nextN = curr.next
            curr = nextN
            count += 1
        if count == 1: return None
        elif n == count:
                hold[0].next = None
                head = hold[1]
        elif count == 2: hold[0].next = None
        elif count >= 3 and n == 1: hold[0].next = None
        elif count >= 3: hold[0].next = hold[2]
        return head
"""



