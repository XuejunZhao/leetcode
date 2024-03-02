class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1: return nums
        l = 0
        for r in range(n):
            if nums[r] != 0:
                nums[l] = nums[r]
                l += 1
        for i in range(l,n): 
            nums[i] = 0
        return nums
        