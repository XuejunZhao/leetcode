class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # place: 1; unplace: 0 
        chess = [[0 for j in range(n)] for i in range(n)]
        # queen rule 
        out = []
        def validatedQ(i,j):
            for k in range(i):
                if chess[k][j] == 1: 
                    return False 
            # diag: i+1, j-1 
           
            add_i_j = i + j
            for k_i in range(n):
                k_j = add_i_j - k_i
                if k_j in range(n) and chess[k_i][k_j]:
                    return False 
            ext_i_j = i - j
            for k_i in range(n):
                k_j = k_i - i + j
                if k_j in range(n) and chess[k_i][k_j]:
                    return False 
            return True
        def addQ(i,j):
            chess[i][j] = 1
        def removeQ(i,j):
            chess[i][j] = 0
        def printChess():
            res = []
            for i in range(n):
                curr = []
                for j in range(n):
                    if chess[i][j] == 1:
                        curr.append('Q')
                    else:
                        curr.append('.')
                res.append(''.join(curr))
            out.append(res)
        
        def backtrack(i):
            for j in range(n):
                if validatedQ(i,j): 
                    addQ(i,j)
                    if i == n -1: 
                        printChess()
                    else:
                        backtrack(i+1)
                    removeQ(i,j)
                        
                
        backtrack(0)
        return out