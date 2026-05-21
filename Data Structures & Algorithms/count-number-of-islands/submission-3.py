class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        res = 0
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c] = "0"

            while q:
                r,c = q.popleft()

                for dr,dc in directions:
                    nr = r +dr
                    nc = c + dc
                    if 0<=nr< row and 0 <= nc < col and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        q.append((nr,nc))


        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    res += 1
                    bfs(r,c)
        return res