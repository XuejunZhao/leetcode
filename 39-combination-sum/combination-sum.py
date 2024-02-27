class Solution(object):
    def __init__(self):
        self.res = []
        self.track = []

    def backtrack(self, start, candidates, target, tot): 
        if tot == target: 
            self.res.append(self.track[:])
        if tot > target: 
            return 
        
        for i in range(start,len(candidates)):
            tot += candidates[i]
            self.track.append(candidates[i])
            self.backtrack(i, candidates, target, tot)
            tot -= candidates[i]
            self.track.pop()

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates: return []
        start = 0 
        tot = 0 
        self.backtrack(start, candidates, target, tot)
        return self.res
        