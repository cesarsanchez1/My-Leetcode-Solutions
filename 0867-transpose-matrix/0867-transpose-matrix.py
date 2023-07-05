class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
    
        m = len(matrix[0])
        n = len(matrix)

        arrT = []

        for j in range(m):
            arr = []
            for i in range(n):
                arr.append(matrix[i][j])
            arrT.append(arr)

        return arrT
            



