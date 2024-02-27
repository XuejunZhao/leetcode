# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        prev = None 
        curr = head 
        while curr: 
            if curr.val == val:
                if prev: 
                    curr = curr.next 
                    prev.next = curr
                else:
                    head = head.next 
                    curr = head
            else: 
                prev = curr
                curr = curr.next 
        return head 
            