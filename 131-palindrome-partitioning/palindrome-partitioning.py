class Solution:
    def __init__(self):
        self.res = []
        self.track = []
    def palindrome(self, s, i, j):
        n = len(s)
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1 
            j -= 1
        return True 
    def backtrack(self, s, start):
        n = len(s)
        if start == n: 
            self.res.append(self.track[:])
        else: 
            for i in range(start,n):
                if not self.palindrome(s, start, i):
                    continue
                self.track.append(s[start:i+1])
                self.backtrack(s,i+1)
                self.track.pop(-1)
    def partition(self, s: str) -> List[List[str]]:
        
        self.backtrack(s,0)
        return self.res
