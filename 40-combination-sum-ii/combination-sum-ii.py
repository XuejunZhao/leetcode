class Solution:
    def __init__(self):
        self.res = []
    def backtrack(self, last, candidates,target,tot):
        if sum(tot) == target: 
            self.res.append(tot[:])
        elif sum(tot) > target:
            return 
        for i,c in enumerate(candidates):
            if c == last: continue
            tot.append(c)
            self.backtrack(last, candidates[i+1:], target, tot)
            tot.pop(-1)
            last = c
        return 

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.backtrack(float('inf'), candidates,target,[])
        return self.res