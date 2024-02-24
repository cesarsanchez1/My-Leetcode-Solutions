class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        rowSet = set()
        columnSet = set()
        columns = {}
        rows = {}

        for i in range(len(grid)):
            rows[tuple(grid[i])] = rows.get(tuple(grid[i]), 0) + 1
            rowSet.add(tuple(grid[i]))

        for j in range(len(grid[0])):
            temp = []
            for i in range(len(grid)):
                temp.append(grid[i][j])
            columns[tuple(temp)] = columns.get(tuple(temp), 0) + 1
            columnSet.add(tuple(temp))
        
        res = 0

        for item in rowSet:
            if item in columnSet:
                res += rows[item]*columns[item]
        
        return res
            




            


