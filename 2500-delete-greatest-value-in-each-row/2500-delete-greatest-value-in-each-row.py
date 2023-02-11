class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            grid[i].sort()

        currMax = 0
        res = 0

        for j in range(len(grid[0])-1,-1,-1):
            currMax = 0
            for i in range(len(grid)):
                currMax = max(currMax, grid[i][j])
            res += currMax
        return res

        
        
        
        
        