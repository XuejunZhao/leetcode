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
        pre_n = None 
        curr_n = head 
        step = n + 1
        while step and curr_n: 
            curr_n = curr_n.next
            step -= 1
        
        if step > 1 and not curr_n: 
            return None 
        elif step == 1 and not curr_n: 
            return head.next
        
        else:
            pre_n = head 
            while curr_n: 
                pre_n = pre_n.next 
                curr_n = curr_n.next 
            tmp = pre_n.next  
            pre_n.next = tmp.next 
            # else: pre_n.next = None
        return head


                


        