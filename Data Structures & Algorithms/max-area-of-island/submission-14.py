class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # iterative
        # if not grid:
        #     return 0
        # rows,cols=len(grid),len(grid[0])
        # max_area=0
        
        
        # def bfs(r, c):
        #     queue = deque()
        #     queue.append((r, c))
        #     grid[r][c] = '0'
        #     area = 1  # <-- starting cell counts as 1

        #     while queue:
        #         row, col = queue.popleft()
        #         directions = [(row-1,col), (row+1,col), (row,col-1), (row,col+1)]
        #         for nr, nc in directions:
        #             if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
        #                 grid[nr][nc] = 0
        #                 queue.append((nr, nc))
        #                 area += 1  # <-- increment for every new cell found

        #     return area  # <-- return the total island size
        # # iteratvve bfs
        # for i in range(rows):
        #     for j in range(cols):
        #         if grid[i][j]==1:
        #             areaofgrid=bfs(i,j)
        #             max_area=max(max_area,areaofgrid)

        # return max_area








        #recursion
        rows,cols=len(grid),len(grid[0])
        max_area=0
 
        def dfs(r,c):
            rowb=0<=r<rows
            colb=0<=c<cols
            if not rowb or not colb :
                return 0
            if grid[r][c]==0:
                return 0
            grid[r][c]=0

            return 1 + dfs(r-1,c) + dfs(r+1,c) + dfs(r,c-1) + dfs(r,c+1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    max_area=max(dfs(i,j),max_area)

        return max_area
