# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # locate n+1 
        # slow, fast has the gap with n+1 
        fast = head 
        gap = n + 1
        while fast and gap: 
            fast = fast.next 
            gap -= 1
        if not fast and gap == 1: 
                return head.next 
        if not fast and gap > 1: 
                return None 
        else:
            slow = head 
            while fast: 
                slow = slow.next 
                fast = fast.next 
            
            slow.next = slow.next.next 
            return head 

        