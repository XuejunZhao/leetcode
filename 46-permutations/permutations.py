class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n <= 1: 
            return [nums]
        res = []
        for i,num in enumerate(nums):
            permutations = self.permute(nums[:i]+nums[i+1:])
            for p in permutations:
                res.append(p+[num])
        return res
        