class Solution:
    def __init__(self):
        self.res =[]
        self.track = []
        self.target = float('inf')

    def backtrack(self, candidates, last):
        if sum(self.track) == self.target:
            self.res.append(self.track[:])
        elif sum(self.track) > self.target:
            return
        else:
            for i,c in enumerate(candidates):
                if c == last:
                    continue
                self.track.append(c)
                self.backtrack(candidates[i+1:], last)
                self.track.pop(-1)
                last = c

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.target  = target

        self.backtrack(candidates, float('inf'))
        return self.res