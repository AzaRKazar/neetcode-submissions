from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return
        rows=len(grid)
        cols=len(grid[0])
        queue=deque()
        INF=2^31 - 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    queue.append((r,c))
        
        while queue:
            r,c=queue.popleft()
            for i,j in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                if i<0 or j<0 or i>=rows or j>= cols or grid[i][j]==INF:
                    grid[i][j]=grid[r][c]+1
                    queue.append((i,j))
