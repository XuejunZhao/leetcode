class Solution(object):
    def l_bound(self, nums, target):
        n = len(nums)
        l = 0 
        r = n -1
        while l <= r: 
            mid = l + (r-l)/2
            if nums[mid] >= target: 
                r = mid - 1
            else: 
                l = mid + 1
        if l not in range(n): return -1
        return l if nums[l] == target else -1

    def r_bound(self, nums, target):
        n = len(nums)
        l = 0 
        r = n -1
        while l <= r: 
            mid = l + (r-l)/2
            if nums[mid] <= target: 
                l = mid + 1
            else: 
                r = mid - 1
        if r not in range(n): return -1
        return r if nums[r] == target else -1


    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums: return [-1, -1]
        return [self.l_bound(nums, target), self.r_bound(nums, target)]
        