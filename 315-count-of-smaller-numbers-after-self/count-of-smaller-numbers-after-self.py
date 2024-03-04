class Solution(object):
    def __init__(self):
        self.count = defaultdict(int)
    def mergeSort(self, nums):
        n = len(nums)
        if n <=1: return nums
        l = 0 
        r = n - 1
        mid = l + (r-l)//2
        merged_l = self.mergeSort(nums[l:mid+1])
        merged_r = self.mergeSort(nums[mid+1:r+1])
        merged_r_small_size = 0 
        res = []
        while merged_l and merged_r: 
            if merged_l[0] <= merged_r[0]: 
                curr = merged_l.pop(0)
                res.append(curr)
                self.count[curr[1]] += merged_r_small_size
            else: 
                res.append(merged_r.pop(0))
                merged_r_small_size += 1
                
        if merged_l: 
            # print (merged_l)
            # print (merged_r)
            res += merged_l 
            for curr_l in merged_l: 
                self.count[curr_l[1]] += merged_r_small_size
            
        if merged_r: 
            res += merged_r
        return res
            

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # merge sort
        # then calculate the smaller when the right is bigger 
        nums_idxs = [ [num,i] for i,num in enumerate(nums)]
        self.mergeSort(nums_idxs)
        out = [0]*len(nums)
        for idx, val in self.count.items():
            out[idx] = val
        return out