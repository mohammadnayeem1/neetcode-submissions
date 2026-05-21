class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0 
        row, col = len(grid), len(grid[0])
        direction = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(r,c):
            if min(r,c) < 0 or r >= row or c >= col or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for dr,dc in direction:
                dfs(r+dr,dc+c)


        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    dfs(r,c)
                    res += 1
        return res