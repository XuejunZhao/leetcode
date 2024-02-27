# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        addition = 0 
        head = None 
        tail = None
        def digit_rule(num, head, tail):
            # if num == 0: 
            #     return 0, head, tail
            
            addition = num/10
            node = ListNode(num%10)
            if not head: 
                head = node 
                tail = node
            else: 
                tail.next = node 
                tail = node 
            print (head, tail)
            return addition, head, tail 
            
        while l1 or l2 or addition:
            num = 0  
            if l1:
                num = l1.val
                l1 = l1.next
            if l2:
                num += l2.val
                l2 = l2.next 
            num += addition 
            addition, head, tail = digit_rule(num, head, tail)
        print (head, tail )
        return head
        