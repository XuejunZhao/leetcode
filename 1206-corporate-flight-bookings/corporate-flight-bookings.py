class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        diff = [0 for i in range(n+1)]
        out = [0 for i in range(n+1)]
        for booking in bookings:
            l, r, val = booking
            diff[l-1] += val 
            diff[r] -= val
        
        l = 1
        for i in range(n):
            out[i] += diff[i] + out[i-1]
            
        return out[:-1]


        

        