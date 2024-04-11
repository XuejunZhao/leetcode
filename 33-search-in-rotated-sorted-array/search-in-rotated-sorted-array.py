class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0 
        r = n - 1
        while l <= r: 
            mid = (r+l)//2
            if target == nums[mid]: 
                return mid 
            elif nums[l] <= nums[mid]: 
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else: 
                    l = mid + 1
            else: 
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else: 
                    r = mid - 1
        return -1
                