class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid) , len(grid[0])
        res = 0
        direction = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(r,c):
            if min(r,c) < 0 or r>= row or c>= col or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            size = 1
            for dr,dc in direction:
                size += dfs(r + dr, c + dc)
            return size
        

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    size = dfs(r,c)
                    res = max(size,res)
        return res