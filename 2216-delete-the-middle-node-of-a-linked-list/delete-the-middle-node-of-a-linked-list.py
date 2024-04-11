# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self,head):
        n = 0
        while head: 
            n += 1
            head = head.next 
        return n

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = self.length(head)
        if n == 1: return None
        elif n == 2: 
            head.next = None
            return head 
        k = n//2
        l, r = None, head 
        idx = k + 1
        
        while idx: 
            idx -= 1
            r = r.next
        while r:
            r = r.next 
            if l == None: 
                l = head
            else:
                l = l.next 
        if n%2 == 1:
            l.next = l.next.next 
        else: 
            l = l.next 
            l.next = l.next.next 
        return head