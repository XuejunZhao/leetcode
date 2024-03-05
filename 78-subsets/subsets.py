class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        n = len(nums)
        if n == 0: 
            return [[]]
        
        res = [[]]
        for i, num in enumerate(nums):
            subset = self.subsets(nums[i+1:])
            for s in subset:
                res.append([num] + s)
            if not subset: 
                res.append([num])
        return res
