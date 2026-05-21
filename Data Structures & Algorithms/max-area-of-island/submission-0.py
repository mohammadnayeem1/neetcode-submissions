class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        maxC = 0
        def dfs(r,c):
            if (min(r,c)< 0 or r == row or c == col or grid[r][c] == 0):
                return 0
            
            grid[r][c] = 0
            count = 1
            count += dfs(r+1,c)
            count += dfs(r-1,c)
            count += dfs(r,c+1)
            count += dfs(r,c-1)
            return count



        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    count = dfs(r,c)
                    maxC = max(maxC,count)
        return maxC