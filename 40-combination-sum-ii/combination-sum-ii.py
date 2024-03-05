class Solution(object):
    def __init__(self):
        self.res = []
        self.track = []
    def backtrack(self, candidates, target, tot, last):
        if tot == target: 
            self.res.append([c[0] for c in self.track])
        elif tot > target: 
            return
        else: 
            for i,c in enumerate(candidates):
                if c == last: continue
                tot += c 
                self.track.append([c,i])
                self.backtrack(candidates[i+1:], target, tot, last)
                tot -= c 
                self.track.pop()
                last = c
              


    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        last = float('inf')
        self.backtrack(candidates, target, 0, last)
        return self.res

        