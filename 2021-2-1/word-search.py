class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i,j,w):
            if not w:
                return True
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return False
            if board[i][j] != w[0]:
                return False 
            board[i][j] = '#'
            for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                if dfs(i+di,j+dj,w[1:]):
                    return True
            board[i][j] = w[0]
            return False       
 
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,word):
                    return True
        return False
        