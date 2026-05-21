class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row = len(grid)
        col = len(grid[0])
        q = deque()
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    q.append([r,c,0])
        while q:
            r,c,distance = q.popleft()
            for dr,dc in directions:
                nr = dr + r
                nc = dc + c
                if 0<=nr<row and 0<=nc<col and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = distance +1
                    q.append([nr,nc,distance+1])
        
        