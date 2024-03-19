class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat), len(mat[0])
        res = [[-1 for j in range(n)] for i in range(m)]
        q = []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j))
                    res[i][j] = 0
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        while q:
            x, y = q.pop(0)
            for d in dirs:
                dx, dy = d 
                if 0 <= x + dx < m and 0 <= y + dy < n and res[x+dx][y+dy] == -1:
                    res[x+dx][y+dy] = res[x][y] + 1
                    q.append((x+dx, y+dy))
        return res
                
