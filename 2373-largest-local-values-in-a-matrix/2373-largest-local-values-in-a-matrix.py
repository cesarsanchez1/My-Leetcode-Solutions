class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        rowScope = len(grid)-2
        columnScope = len(grid[0])-2
        fin = []

        for column in range(columnScope):
            res = []
            for row in range(rowScope):
                maxLocal = 0
                for k in range(3):
                    for j in range(3):
                        if maxLocal < grid[k+column][j+row]:
                            maxLocal = grid[k+column][j+row]
                res.append(maxLocal)
            fin.append(res)
            
        return fin    