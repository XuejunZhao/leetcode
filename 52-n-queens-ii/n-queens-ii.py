class Solution:
    def __init__(self):
        self.queens = set()
        self.res = 0
    def placeQueens(self, n, dp, curr_i, curr_j):
        
        for i in range(n):
            if curr_i != i and dp[i][curr_j] == 1: 
                return False 

        for j in range(n):
            if curr_j != j and dp[curr_i][j] == 1: 
                return False 
        pos = curr_i + curr_j
        neg = curr_i - curr_j
        for i in range(n):
            j = pos-i
            if j >= 0 and j < n and dp[i][j] == 1: 
                return False 
        for i in range(n):
            j = i-neg
            if j >= 0 and j < n and dp[i][j] == 1: 
                return False  
        return True       
    def backtrack(self, n, dp, i):
        for j in range(n):
            if self.placeQueens(n, dp, i, j):
                dp[i][j] = 1
                if i == n - 1: 
                    # self.queens.add(dp[:])
                    # print (dp)
                    self.res += 1
                else:
                    self.backtrack(n,dp,i+1)
                dp[i][j] = 0 

    def totalNQueens(self, n: int) -> int:
        dp=[[0 for i in range(n)] for j in range(n)]
        self.backtrack(n, dp, 0)
        return self.res
