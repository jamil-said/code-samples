
""" mergeKSortedLists
Merge k sorted linked lists and return it as one sorted list. Analyze and 
describe its complexity.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from operator import attrgetter
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        holder = []
        for l in lists:
            while l:
                holder.append(l)
                l = l.next
        holder = sorted(holder, key = attrgetter('val'))
        dummy = curr = ListNode(0)
        for node in holder:
            curr.next = curr = node
        return dummy.next

""" alternative, much slower
class Solution:
    def mergeKLists(self, lists):
        dic = {}
        lists = [i for i in lists if i]
        if not lists: return []
        for idx, node in enumerate(lists):
            if node not in dic: dic[node.val] = idx
        sml = min([i for i in dic.keys()])
        curr = head = lists[dic[sml]]
        if lists[dic[sml]].next: 
            lists[dic[sml]] = lists[dic[sml]].next
            dic.pop(sml)
        else:
            lists.pop(dic[sml])
            dic.pop(sml)
        self.calcL(lists, curr, dic)
        return head

    def calcL(self, lists, curr, dic):
        while lists:
            for idx, node in enumerate(lists):
                if node not in dic: dic[node.val] = idx
            sml2 = min([i for i in dic.keys()])
            curr.next = lists[dic[sml2]]
            curr = lists[dic[sml2]]
            if lists[dic[sml2]].next: 
                lists[dic[sml2]] = lists[dic[sml2]].next
                dic.pop(sml2)
            else:
                lists.pop(dic[sml2])
                dic.pop(sml2)
        return
"""        


