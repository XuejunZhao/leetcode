class Solution:
    def left_search(self, nums, target):
        n = len(nums)
        l = 0 
        r = n - 1
        while l <= r: 
            mid = (l+r)//2
            if nums[mid] > target: 
                r = mid - 1
            elif nums[mid] < target: 
                l = mid + 1 
            else: 
                r = mid - 1
        return l if 0<=l<= n -1 and nums[l] == target else -1
    def right_search(self,nums,target):
        n = len(nums)
        l = 0 
        r = n - 1
        while l <= r: 
            mid = (l+r)//2
            if nums[mid] > target: 
                r = mid - 1
            elif nums[mid] < target: 
                l = mid + 1 
            else: 
                l = mid + 1
        return r if  0<=r<= n -1 and nums[r] == target else -1


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = self.left_search(nums, target)
        r = self.right_search(nums, target)
        return (l, r)
        