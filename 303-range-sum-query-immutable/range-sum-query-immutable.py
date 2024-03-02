class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        self.diff_nums = []
        
        for i, num in enumerate(nums):
            if i == 0 :
                self.diff_nums.append(num)  
            else:
                self.diff_nums.append(num + self.diff_nums[-1])

            

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == 0:
            return self.diff_nums[right]
        else: 
            return self.diff_nums[right]-self.diff_nums[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)