class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[1] * n for i in range(n)]
        
        top = 0
        bottom = len(matrix)
        left = 0
        right = len(matrix[0])
        
        squares = []

        for i in range(1,(n**2)+1):
            squares.append(i)

        k = 0

        while left < right and top < bottom:
            for i in range(left, right):
                matrix[top][i] = squares[k]
                k+=1
            top+=1
          
            for i in range(top, bottom):
                matrix[i][right-1] = squares[k]
                k+=1
            right-=1

            if not (left < right and top < bottom):
                break

            for i in range(right-1, left-1, -1):
                matrix[bottom-1][i] = squares[k]
                k+=1
            bottom-=1

            for i in range(bottom-1, top-1, -1):
                matrix[i][left] = squares[k]
                k+=1
            left+=1

        return matrix














        