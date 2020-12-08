"""   addTwoNumbers
You are given two non-empty linked lists representing two non-negative 
integers. The digits are stored in reverse order and each of their nodes 
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except 
the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        l3 = res = ListNode(0)
        carry = 0
        while True:
            v3 = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = 0 if (v3 < 10) else 1
            l3.val = v3 % 10
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
            if l1 or l2 or carry:
                l3.next = ListNode(0)
                l3 = l3.next
            else:
                break
        return res


""" Alternative, equal in speed and memory usage, but more complicated

class Solution:
    def addTwoNumbers(self, l1, l2):
        n1, n2, i = 0, 0, 1
        while l1:
            n1 += (l1.val * i)
            i *= 10
            l1 = l1.next
        i = 1
        while l2:
            n2 += (l2.val * i)
            i *= 10
            l2 = l2.next
        n3 = n1 + n2
        l3 = res = ListNode(0)
        while True:
            tmp = n3 % 10
            l3.val = tmp
            n3 = n3 // 10
            if n3 == 0:
                break
            l3.next = ListNode(0)
            l3 = l3.next
        return res

"""

""" alternative, slower

class Solution:
    def addTwoNumbers(self, l1, l2):
        l1Num, l2Num = self.calcNums(l1), self.calcNums(l2)
        return self.buildLL(str(l1Num + l2Num))
        
    def calcNums(self, ll):
        numStr = ''
        while ll:
            numStr += str(ll.val)
            ll = ll.next
        return int(numStr[::-1])
            
    def buildLL(self, sNum):
        curr = newHead = ListNode(0)
        for i in range(len(sNum)-1, -1, -1):
            curr.val = int(sNum[i])
            curr.next = ListNode(0)
            prev, curr = curr, curr.next
        prev.next = None
        return newHead

"""
     
