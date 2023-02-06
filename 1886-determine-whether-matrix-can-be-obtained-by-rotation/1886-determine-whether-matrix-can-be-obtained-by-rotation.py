class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for i in range(4):
            for col in range(len(mat)):
                for row in range(col, len(mat[0])):
                    temp = mat[col][row]
                    mat[col][row] = mat[row][col]
                    mat[row][col] = temp
                
            for col in range(len(mat)):
                mat[col].reverse()
                
            if mat == target:
                return True
        return False
                
            
                
        