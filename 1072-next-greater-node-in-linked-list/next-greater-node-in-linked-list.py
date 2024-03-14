# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        res = []
        if not head: 
            return res

        while head:
            r = head.next
            while r is not None and r.val <= head.val:
                r = r.next 
            if r is None: 
                res.append(0)
            else:
                res.append(r.val)
            head = head.next 
        
        return res


