class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])
        pac, atl = set(),set()

        def dfs(r,c,seen,prev):
            if min(r,c)< 0 or r == row or c == col or heights[r][c] < prev or (r,c) in seen:
                return
            seen.add((r,c))
            dfs(r+1,c,seen,heights[r][c])
            dfs(r-1,c,seen,heights[r][c])
            dfs(r,c+1,seen,heights[r][c])
            dfs(r,c-1,seen,heights[r][c])

        
        res = []
        for r in range(row):
            for c in range(col):
                if r == 0:
                    dfs(0,c,pac,heights[r][c])
                if c == 0:
                    dfs(r,0,pac,heights[r][c])
                if r == row -1:
                    dfs(r,c,atl,heights[r][c])
                if c == col - 1:
                    dfs(r,c,atl,heights[r][c])
        for r in range(row):
            for c in range(col):
                if (r,c) in pac and (r,c) in atl:
                    res.append((r,c))
        return res