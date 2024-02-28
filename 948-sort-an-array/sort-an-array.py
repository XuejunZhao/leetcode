class Solution:
    def quicksort(self, nums: List[int], start: int, end: int) -> List[int]:
        
        if start >= end - 1: return nums 
        pivot = nums[start]
        pivot_left = start + 1
        for i in range(pivot_left, end):
            if nums[i] < pivot: 
                nums[i], nums[pivot_left] = nums[pivot_left], nums[i]
                pivot_left += 1
        nums[pivot_left-1], nums[start] = nums[start], nums[pivot_left-1]
        nums = self.quicksort(nums, start, pivot_left-1)
        nums = self.quicksort(nums, pivot_left, end)
        return nums

    def mergesort(self, nums: List[int])  -> List[int]:
        
        n = len(nums)
        if n <= 1: return nums
        start = 0 
        end = n 
        mid = start + (end-start)//2
        nums1 = self.mergesort(nums[start: mid])
        nums2 = self.mergesort(nums[mid: end])
        res = []
        while nums1 and nums2: 
            if nums1[0] < nums2[0]:
                res.append(nums1.pop(0))
            else:
                res.append(nums2.pop(0))

        if nums1: res += nums1
        if nums2: res += nums2
        return res


    def sortArray(self, nums: List[int]) -> List[int]:
        # random.shuffle(nums)
        # n = len(nums)
        # start = 0 
        # end = n 
        # nums = self.quicksort(nums, start, end)
        nums = self.mergesort(nums)
        return nums