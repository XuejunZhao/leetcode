# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def scanlength(self,head):
        length = 0 
        while head: 
            length += 1
            head = head.next 
        return length
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if not head: return head
        length = self.scanlength(head)
        if length <= k: 
            k = k%length
        if k == 0: return head 
        gap = k - 1
        l = None
        r = head 
        while gap and r: 
            gap -= 1
            r = r.next 
        
        r_dummy = ListNode(-1) 
        p = r_dummy
        while r: 
            if not l: 
                l = head 
            else: 
                p.next = l 
                p = p.next
                l = l.next 
            r = r.next 
        
        p.next = None
        new_start = l 
        curr = new_start
        while curr.next:
            curr = curr.next
        curr.next = r_dummy.next 
        return new_start

        
