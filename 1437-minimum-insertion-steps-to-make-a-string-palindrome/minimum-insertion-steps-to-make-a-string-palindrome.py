class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[-1 for i in range(n)] for i in range(n)]
        def dfs(l,r):
            if l >= r:
                return 0 
            if dp[l][r] != -1:
                return dp[l][r]
            if s[l] == s[r]:
                dp[l][r] = dfs(l+1, r-1)
            else:
                dp[l][r] = min(dfs(l,r-1),dfs(l+1,r))+1
            return dp[l][r]
        return dfs(0,n-1)
    