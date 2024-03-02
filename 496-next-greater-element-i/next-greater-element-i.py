class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        out = []
        n2 = len(nums2)
        big_nums2 = [-1]*n2
        stk = [nums2[-1]]
        for j in range(n2-2, -1, -1):
            # print (stk)
            
            if nums2[j] >= stk[-1]:
                while stk and nums2[j] >= stk[-1]:
                    stk.pop(-1)
            if stk: big_nums2[j] = stk[-1]
            stk.append(nums2[j])

        for num1 in nums1:
            num1_idx = nums2.index(num1)
            out.append(big_nums2[num1_idx])
        return out
                

        