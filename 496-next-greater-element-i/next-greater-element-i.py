class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nums2_dict = {}
        n = len(nums2)
        for i in range(n-1, -1, -1): 
            num = nums2[i]
            if stack and stack[-1] > num:
                 nums2_dict[num] =  stack[-1]
            else:
                while stack and stack[-1] <= num:
                    stack.pop(-1) 
                if stack: nums2_dict[num] =  stack[-1]
                else: nums2_dict[num] = -1 
            stack.append(num)

        res = []
        for num in nums1:
            if num in nums2_dict.keys():
                res.append(nums2_dict[num])
            else:
                res.append(-1)
        return res
            

            