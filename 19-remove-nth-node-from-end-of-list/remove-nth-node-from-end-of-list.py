# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l = None 
        r = head 
        gap = n + 1
        while gap and r: 
            
            r = r.next 
            gap -= 1
        # if not r: return head
        if gap > 1 and not r: 
            return None 
        elif gap == 1 and not r: 
            return head.next
        else:
            l = head
            while r:
                l = l.next
                r = r.next 
        
            l_next = l.next
            l.next = l_next.next 
        return head



                


        