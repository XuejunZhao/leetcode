class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l = 1
        r = 1000000000 + 1

        def f(max_size):
            n = len(piles)
            l = 0 
            time = 0 
            for l in range(n):
                time += piles[l] // max_size
                if piles[l] % max_size > 0:
                    time += 1
            return time 

        while l <= r:
            mid = l + (r-l)/2
            if f(mid) <= h: 
                r = mid - 1
            elif f(mid) > h:
                l = mid + 1 
        return l 

