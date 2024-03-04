class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        pq = []
        for i, num in enumerate(arr):
            if len(pq) <k:
                heapq.heappush(pq, (-abs(num-x), num))
            else:
                diff, head = heapq.heappop(pq)
                if -abs(num-x) > diff: 
                    heapq.heappush(pq, (-abs(num-x), num))
                else:
                    heapq.heappush(pq, (diff, head))

        return sorted([num[1] for num in pq])


