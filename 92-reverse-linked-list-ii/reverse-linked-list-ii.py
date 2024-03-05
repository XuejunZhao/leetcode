# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self, head, node):
        if not head: 
           head = node 
        else: 
            node.next = head 
            head = node 
        return head

    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        # locate the node before left 
        # locate the right 
        gap = right - left + 1
        pre_l = left - 1
        l = None 
        r = head

        while pre_l: 
            l = r
            r = r.next 
            pre_l -= 1

        r_head = None 
        r_tail = r 
        while r and gap: 
            r_next = r.next
            r.next = None
            r_head = self.reverse(r_head, r)
            r = r_next
            gap -= 1
        
        if l: 
            l.next = r_head 
        else:
            head = r_head 
        if r_tail: 
            r_tail.next = r 
        return head

