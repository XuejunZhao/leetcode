# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next: 
            return head
        odd_head = head
        even_head = head.next 
        odd_tail = odd_head 
        even_tail = even_head
        curr = head.next.next
        idx = 1 
        while curr: 
            # curr_next = curr.next 
            # curr.next = None
            if idx%2 == 1:
                odd_tail.next = curr
                odd_tail = curr
            else: 
                even_tail.next = curr
                even_tail = curr
            curr = curr.next
            idx += 1 
        if even_tail: 
            even_tail.next = None
            odd_tail.next = even_head 

        return odd_head
            
