class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        directions = [[1,0],[-1,0],[0,-1],[0,1]]

        def dfs(r,c,index):
            if index == len(word):
                return True
            if min(r,c)<0 or r == row or c == col or word[index] != board[r][c]:
                return False
            board[r][c] = "#"
            res = (dfs(r+1,c,index+1) or dfs(r-1,c,index+1) or dfs(r,c-1,index+1) or dfs(r,c+1,index+1))
            board[r][c] = word[index]
            return res



        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True
        return False