# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addNode(self, head, tail, node):
        node.next = None
        if not head: 
            head = node 
            tail = node 
        else: 
            tail.next = node 
            tail = node 
        return head, tail

    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head: return head 
        l_head = None 
        l_tail = None 
        l = None 
        r = head 
        while r: 
            
            if r.val >= x: 
                l = r 
                r = r.next 
            else: 
                node = r 
                node_next = node.next
                if l:
                    l.next = node_next
                else: 
                    head = node_next 
                l_head, l_tail = self.addNode(l_head, l_tail, node)
                r = node_next
        # print (l_tail)
        # print (l_head)
        if l_head:
            l_tail.next = head 
            return l_head 
        else: 
            return head


            