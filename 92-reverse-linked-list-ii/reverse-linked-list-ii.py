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
        pre_l = None
        r = head
        tmp_left = left - 1
        while tmp_left: 
            if not pre_l: 
                pre_l = head 
            else: 
                pre_l = pre_l.next 
            tmp_left -= 1 
        
        if pre_l: 
            r_tail = pre_l.next
        else: 
            r_tail = head 
        
        r_head = None
        node = r_tail
        while gap: 
            tmp = node.next
            node.next = None
            r_head = self.reverse(r_head, node)
            gap -= 1 
            node = tmp
        
        # print (pre_l)
        # print (r_head)
        # print (r_tail)
        # print (node)
        if pre_l: 
            pre_l.next = r_head
        else: 
            head = r_head

        if r_tail: 
            r_tail.next = node
        return head
            
            
        