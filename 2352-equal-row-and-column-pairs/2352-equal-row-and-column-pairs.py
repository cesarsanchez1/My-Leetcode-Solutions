class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        arrT = []

        for j in range(m):
            temp = []
            for i in range(n):
                temp.append(grid[i][j])
            arrT.append(temp)
        
        freq = {}
        res = 0
        gridSet = set()

        for item in grid:
            gridSet.add(tuple(item))
            freq[tuple(item)] = freq.get(tuple(item), 0) + 1

        for item in arrT:
            if tuple(item) in gridSet:
                res += freq[tuple(item)]
        
        return res




        
        