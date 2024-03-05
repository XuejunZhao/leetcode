class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        if n == 0: 
            return [[]]
        elif n == 1: 
            return [nums]
        res = []
        last = float('inf')
        for i, num in enumerate(nums):
            if num == last: continue
            permutations = self.permuteUnique(nums[:i]+nums[i+1:])
            for p in permutations:
                res.append([num]+p)
            last = num
        return res

        