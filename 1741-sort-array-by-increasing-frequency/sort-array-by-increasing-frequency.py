class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        freq_val = defaultdict(list)
        # print (freq_val)
        curr = []
        for i in range(n-1, -1, -1):
            print (freq_val)
            
            if i < n - 1 and nums[i] not in curr:
                freq_val[len(curr)].append(curr[-1])
                curr = []
                curr.append(nums[i])
            else:
                curr.append(nums[i])
        if curr:
            freq_val[len(curr)].append(curr[-1])
        res = []
        sorted_freq = sorted(freq_val)
        # print (freq_val)
        for freq in sorted_freq:
            vlist = freq_val[freq]
            
            for val in vlist:
                print ([val]*freq)
                res += [val]*freq
        return res


        