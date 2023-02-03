class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for col in range(len(matrix)):
            for row in range(col,len(matrix)):
                temp = matrix[col][row]
                matrix[col][row] = matrix[row][col]
                matrix[row][col] = temp
        
        for i in range(len(matrix)):
            matrix[i].reverse()
                

        