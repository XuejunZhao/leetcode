class Solution:
    def __init__(self):
        self.nums = []
        self.pairs = 0

    """
    [-3, -2], [-2, -1]
              [-4, -2]
              [2, 0]

    [0, 4, 10, 11, 12], [0, 1, 8, 9, 10, 11, 12]
    """

    def mergesort(self, nums):
        n = len(nums)
        if n <= 1: 
            return nums
        mid = n//2 
        
        l_nums = self.mergesort(nums[:mid])
        r_nums = self.mergesort(nums[mid:])
        # if adding element from l_nums, then the reverse_pairs with the element at left should be total numbers of pairs. However, there might be error (since the left element at the current left)
        # if adding element from r_nums, then the reverse_pairs with the element at right should be the number of right list. 
        new_nums = []
        temp_r_nums = [num*2 for num in r_nums]
        temp_l_nums = l_nums[:]
        while temp_l_nums and temp_r_nums: 
            if temp_l_nums[0] > temp_r_nums[0]:
                temp_r_nums.pop(0)
                self.pairs += len(temp_l_nums)
            else: 
                temp_l_nums.pop(0)

            
        while l_nums and r_nums: 
            if l_nums[0] > r_nums[0]:
                new_nums.append(r_nums.pop(0)) 
            else: 
                new_nums.append(l_nums.pop(0)) 
            
        if l_nums: 
            new_nums+=l_nums
            
        if r_nums:
            new_nums+=r_nums
        return new_nums

    def reversePairs(self, nums: List[int]) -> int:
        self.nums= nums[:]
        self.mergesort(nums)
        return self.pairs


        
        