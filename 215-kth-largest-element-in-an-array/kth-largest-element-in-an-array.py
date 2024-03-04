class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pq = []
        for i, num in enumerate(nums):
            heapq.heappush(pq, num)
            if len(pq) > k: 
                
                head = heapq.heappop(pq)
                
        return pq[0]