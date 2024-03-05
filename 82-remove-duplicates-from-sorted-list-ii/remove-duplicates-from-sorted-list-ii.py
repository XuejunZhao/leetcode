# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def linknode(self, head, tail, node):
        if not head: 
            head = node 
            tail = node
        else: 
            tail.next = node 
            tail = node 
        return head, tail 
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head 
        if not head.next: return head 
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = head  
  
        while cur: 
            while cur.next and cur.val == cur.next.val:
                    cur = cur.next 
            if  pre.next == cur : 
                pre = pre.next
                cur = cur.next

            else:
                pre.next = cur.next
                cur = pre.next 
                
            
            
        return dummy.next




            

            
                

            
        