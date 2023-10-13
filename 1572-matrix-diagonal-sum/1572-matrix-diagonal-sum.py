class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        
        first = 0
        second = 0
        midpoint = n//2
        
        for i in range(n):
            first += mat[i][i]
            second += mat[i][n-1-i]

        if len(mat)%2==0:
            return first+second
        return first+second-mat[midpoint][midpoint]
        
        
            
        