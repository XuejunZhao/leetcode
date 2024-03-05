class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n == 0: 
            return [[]]
        elif n == 1: 
            return [nums]
        res = []
        for i, num in enumerate(nums):
            permutations = self.permute(nums[:i]+nums[i+1:])
            for p in permutations:
                res.append([num]+p)
        return res

        