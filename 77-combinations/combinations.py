class Solution(object):
    def combineset(self, s, k):
        """
        :type s: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        n = len(s)
        
        if k == 0: 
            return [[]]
        res = []
        for i in range(n):
            combines = self.combineset(s[i+1:], k-1)

            for c in combines: 
                res.append([s[i]] + c) 
        return res
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n == 1: 
            return [[n]*k]
        return self.combineset(range(1,n+1), k)

        