class Solution(object):
    def twosum(self, nums, target):
        n = len(nums)
        l = 0 
        r = n - 1
        res = []
        while l < r: 
            if nums[l] + nums[r] == target: 
                res.append([nums[l],nums[r]])
                pre_l, post_r = l, r
                l += 1
                r -= 1
                while l < r and nums[l] == nums[pre_l]: 
                    l += 1
                while l < r and nums[r] == nums[post_r]: 
                    r -= 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else: 
                l += 1
        return res 

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if i >= len(nums) - 2 or (i > 0 and num == nums[i-1]): continue
            twosum_res = self.twosum(nums[i+1:],-num)
            if len(twosum_res) ==0: continue
            for twosum in twosum_res: 
                 res.append([nums[i]]+twosum)
            
        return res
        