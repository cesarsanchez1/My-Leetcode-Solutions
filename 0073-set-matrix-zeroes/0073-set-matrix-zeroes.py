class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rowsDel = set()
        columnsDel = set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rowsDel.add(i)
                    columnsDel.add(j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rowsDel:
                    matrix[i][j] = 0
                if j in columnsDel:
                    matrix[i][j] = 0
        
                
        
            
                





























        