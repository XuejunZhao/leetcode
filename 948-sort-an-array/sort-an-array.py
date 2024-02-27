class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import random
        # # nums
        if nums == sorted(nums): 
            return nums
        nums = sorted(nums, key=lambda x: random.random())
        n = len(nums)
        if n <= 1: 
            return nums 
        # pivot = nums[0]
        # l = 0
        # for i in range(1,n):
        #     if nums[i] < pivot: 
        #         l += 1
        #         nums[i], nums[l] = nums[l], nums[i]
         
        # nums[0], nums[l] = nums[l], nums[0]
        # nums[0:l] = self.sortArray(nums[0:l])
        # nums[l+1:] = self.sortArray(nums[l+1:])
        # return nums

        mid = n / 2
        l = self.sortArray(nums[:mid])
        r = self.sortArray(nums[mid:])
        res = []
        while l and r: 
            if l[0] <= r[0]:
                res.append(l[0])
                l.pop(0)
            else:
                res.append(r[0])
                r.pop(0)
        if l: res+=l
        if r: res+=r
        return res


                
        
        