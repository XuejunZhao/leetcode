class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        h, w = len(matrix), len(matrix[0])
        self.cu_matrix = [[0 for j in range(w+1)] for i in range(h+1)]
        for i in range(1,h+1):
            for j in range(1,w+1):
                # if i == 0 and j == 0: 
                #     self.cu_matrix[0][0] = matrix[0][0]
                # elif j != 0 and i == 0 :
                #     self.cu_matrix[0][j] = self.cu_matrix[0][j-1] + matrix[0][j]
                # elif j == 0 and i != 0 :
                #     self.cu_matrix[i][0] = self.cu_matrix[i-1][0] + matrix[i][0]
                # else: 
                self.cu_matrix[i][j] += self.cu_matrix[i-1][j] + self.cu_matrix[i][j-1] - self.cu_matrix[i-1][j-1] + matrix[i-1][j-1]
            
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # print (self.cu_matrix)
        # if row1 ==0 and col1 == 0: 
        #     return self.cu_matrix[row2][col2]
        # elif row1 == 0 and col1 != 0: 
        #     return self.cu_matrix[row2][col2] - self.cu_matrix[0][col1]
        # elif row1 != 0 and col1 == 0: 
        #     return self.cu_matrix[row2][col2] - self.cu_matrix[row1][0]
        # else:
        return self.cu_matrix[row2+1][col2+1] - self.cu_matrix[row2+1][col1] - self.cu_matrix[row1][col2+1] + self.cu_matrix[row1][col1]

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)