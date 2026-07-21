class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS,COLS=len(grid),len(grid[0])
        count=0
        
        def bfs(r,c):
            queue=deque()
            queue.append((r,c))
            grid[r][c]="0"

            while queue:
                row,col=queue.popleft()
                dirc=[(row+1,col),(row-1,col),(row,col-1),(row,col+1)]
                for nr,nc in dirc:
                    if 0<= nr < ROWS and 0<= nc<COLS and grid[nr][nc]=='1':
                        grid[nr][nc]='0'
                        queue.append((nr,nc))
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=='1':
                    count+=1
                    bfs(r,c)

        return count
