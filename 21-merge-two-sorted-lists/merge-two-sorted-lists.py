# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        if not list2: 
            return list1
        res = None
        head = None
        while list1 and list2: 
            if list1.val < list2.val: 
                node = list1 
                list1 = list1.next 
            else: 
                node = list2
                list2 = list2.next 
            if not res: 
                res = node 
                head = res
            else: 
                res.next = node 
                res = node 
        if list1: 
            res.next = list1 
        if list2: 
            res.next = list2
        return head
        