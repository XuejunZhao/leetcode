class Solution(object):
    def __init(self):
        self.used_3sum = []
        
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        return self.nSumTarget(nums, 4, 0, target)
    def nSumTarget(self, nums, n, start, target): 
        l_nums = len(nums)
        res = []
        
        if n < 2 or l_nums < n:
            return res
        if n == 2: 
            lo = start 
            hi = l_nums - 1
            while lo < hi:
                tot = nums[lo] + nums[hi]
                left, right = nums[lo], nums[hi]
                if tot < target:
                    while lo < hi and nums[lo] == left:
                        lo += 1
                elif tot > target:
                    while lo < hi and nums[hi] == right:
                        hi -= 1
                else:
                    res.append([left, right])
                    
                    while lo < hi and nums[lo] == left:
                        lo += 1
                    while lo < hi and nums[hi] == right:
                        hi -= 1
                        
        else: 
            
            for i in range(start, l_nums):
                # print (i, n)
                if i > start and i < l_nums -1 and nums[i] == nums[i - 1]:
                    continue
                sub = self.nSumTarget(nums, n - 1, i + 1, target - nums[i])
                
                for arr in sub:
                    # print (sub)
                    arr.append(nums[i])
                    res.append(arr)
                   
                
                
                    
                
        return res