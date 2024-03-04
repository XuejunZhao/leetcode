# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        if not list2: 
            return list1
        res = None
        head = None
       
        while list1 and list2: 
            if list1.val < list2.val: 
                node = list1 
                list1 = list1.next 
            else: 
                node = list2
                list2 = list2.next 
            if not res: 
                res = node 
                head = res
            else: 
                res.next = node 
                res = node 
        if list1: 
            res.next = list1 
        if list2: 
            res.next = list2
        return head
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        n = len(lists)
        if n == 0:
            return None
        elif n == 1: 
            return lists[0]

        # merged_lists = []
        # for i in range(n/2):
        #     if len(lists) >= 2: 
        #         l = lists.pop(0)
        #         r = lists.pop(0)
        #         merged_lists.append(self.mergeTwoLists(l, r))

        # if len(lists) > 0: 
        #     merged_lists.append(lists.pop(0))
        # return self.mergeKLists(merged_lists)

        dummy = ListNode(-1)
        p = dummy 
        pq = []
        for head in lists: 
            if head: 
                heapq.heappush(pq, (head.val, id(head), head))
        while pq: 
            node = heapq.heappop(pq)[2]
            p.next = node 
            if node.next: 
                heapq.heappush(pq, (node.next.val, id(node.next), node.next))
            p = p.next 
        return dummy.next


        
