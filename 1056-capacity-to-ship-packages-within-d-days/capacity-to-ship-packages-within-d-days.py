class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        l = max(weights)
        r = sum(weights)
        def f(cargo):
            n = len(weights)
            t_days = 0
            l = 0 
            while l < n: 
                remain = cargo - weights[l] 
                l += 1
                while remain and l < n: 
                    remain -= weights[l] 
                    if remain >= 0:
                        l += 1
                    else: 
                        break
                t_days += 1
            return t_days

        while l <= r:
            cargo = l + (r-l)/2
            if days >= f(cargo): 
                r = cargo - 1
            elif days < f(cargo): 
                l = cargo + 1
                
           
                
        return l 
            
            