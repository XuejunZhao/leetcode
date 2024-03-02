class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        if n < 1: 
            return n
        l = 0 
        for r in range(n):
            if nums[r] != val: 
                nums[l] = nums[r]
                l += 1
        return l
        