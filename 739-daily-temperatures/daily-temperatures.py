class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        big_temperatures = [0]*n 
        stk = [[temperatures[-1],n-1]]
        for i in range(n-2,-1,-1):
            
            if temperatures[i] >= stk[-1][0]:
                while stk and temperatures[i] >= stk[-1][0]:
                    stk.pop(-1)
            if stk: big_temperatures[i]=stk[-1][1]-i
            stk.append([temperatures[i],i])
        return big_temperatures
        