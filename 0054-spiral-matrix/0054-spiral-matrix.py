class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix)
        left = 0
        right = len(matrix[0])
        arr = []
        
        while left < right and top < bottom:
            for i in range(left, right):
                arr.append(matrix[top][i])
            top+=1

            for i in range(top, bottom):
                arr.append(matrix[i][right-1])
            right-=1

            if not (left < right and top < bottom):
                break

            for i in range(right-1, left-1, -1):
                arr.append(matrix[bottom-1][i])
            bottom-=1

            for i in range(bottom-1, top-1,-1):
                arr.append(matrix[i][left])
            left+=1
        
        return arr
        
            
        
        
        
        
        
        
        
        
        
        