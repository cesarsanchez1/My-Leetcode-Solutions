class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        
        x = 0
        y = 0
        res = 0
        counter = 0
        
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 'R':
                    x = i
                    y = j
                    break
            
        for i in range(y+1, len(board)):
            if board[x][i] == 'B':
                break
            if board[x][i] == 'p':
                counter += 1
                break

        for i in range(y-1, -1, -1):
            if board[x][i] == 'B':
                break
            if board[x][i] == 'p':
                counter += 1
                break

        for i in range(x-1, -1, -1):
            if board[i][y] == 'B':
                break
            if board[i][y] == 'p':
                counter += 1
                break
        
        for i in range(x+1, len(board)):
            if board[i][y] == 'B':
                break
            if board[i][y] == 'p':
                counter += 1
                break
        
        return counter
                
                
            