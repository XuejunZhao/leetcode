class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        k = 2 
        n = len(prices)
        balance_if_buy = -float('inf')
        dp = [[0 for i in range(n)] for j in range(k+1)]
        for j in range(1,k+1):
            for i in range(n):
                # if i == 0: 
                #     dp[j][i] = 0 
                # else:
                dp[j][i] = max(dp[j-1][i], dp[j][i-1])
                if i > 0: dp[j][i] = max(dp[j][i], prices[i]+balance_if_buy)

                balance_if_buy = max(dp[j-1][i-1] - prices[i], balance_if_buy) if i>0 else -prices[i]
        return dp[k][n-1]



