class Solution:
    def Sum(self, candidates, target, n):
        res = []
        length = len(candidates)
        if n == 2:
            l = 0 
            r = length - 1
            while l < r: 
                if candidates[l] + candidates[r] < target:
                    l += 1 
                elif candidates[l] + candidates[r] > target:
                    r -= 1 
                else: 
                    res.append([candidates[l], candidates[r]])
                    last_l = candidates[l]
                    last_r = candidates[r]
                    while l < r and candidates[l] == last_l:
                        l += 1
                    while l < r and candidates[r] == last_r:
                        r -= 1
        elif n >= 3: 
            last = float('inf')
            for i,c in enumerate(candidates[:-n+1]):
                if c == last: continue
                Sum2 = self.Sum(candidates[i+1:], target-c, n-1)
                for sub in Sum2:
                    res.append([c]+sub)
                last = c
        # elif n == 4: 
        #     last = float('inf')
        #     for i,c in enumerate(candidates[:-3]):
        #         if c == last: continue
        #         Sum2 = self.Sum2(candidates[i+1:], target-c, 3)
        #         for sub in Sum2:
        #             res.append([c]+sub)
        #         last = c
        return res

    def fourSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()
        
        Sum2 = self.Sum(candidates, target,4)
        
        
        return Sum2