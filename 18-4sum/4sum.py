class Solution(object):
    def kSum(self, nums, target, k_size):
        n = len(nums)
        l = 0 
        r = n - 1
        res = []
        if k_size == 2:
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
        elif k_size >= 3: 
            for i, num in enumerate(nums):
                if i >= n - k_size+1 or (i > 0 and num == nums[i-1]): continue
                sub_res = self.kSum(nums[i+1:],target-num,k_size-1)
                if len(sub_res) ==0: continue
                for sub_sum in sub_res: 
                    res.append([nums[i]]+sub_sum)
            return res
        


    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = self.kSum(nums, target, 4)
            
        return res