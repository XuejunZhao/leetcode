
            
class Solution(object):
    class MonotonicQueue:
        def __init__(self):
            self.q = []
        def push(self, num, idx):
            while self.q and num > self.q[-1][0]:
                self.q.pop(-1)
            self.q.append([num, idx])
            # print (self.q)
        def max(self):
            return self.q[0][0]
        def pop(self, idx):
            if self.q[0][1] == idx:
                self.q.pop(0)
    
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        if k >= n: return [max(nums)]
        res = []
        window = self.MonotonicQueue()
        for r in range(n):
            window.push(nums[r],r)
            if r >= k-1: 
                res.append(window.max())
                window.pop(r-k+1)
            
        return res