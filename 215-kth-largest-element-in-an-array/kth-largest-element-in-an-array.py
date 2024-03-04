class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pq = []
        for i, num in enumerate(nums):
            if len(pq) < k: 
                heapq.heappush(pq, num)
            else: 
                head = heapq.heappop(pq)
                if num >= head:
                    heapq.heappush(pq, num)
                else:
                    heapq.heappush(pq, head)
        return pq[0]