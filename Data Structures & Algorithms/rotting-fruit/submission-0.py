class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows,cols= len(grid),len(grid[0])
        que=deque()
        fresh=0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    que.append((i,j))

        minutes=0            
        while que and fresh>0:
            
            for i in range(len(que)):
                r,c=que.popleft()

            for i,j in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                if 0<=i<rows and 0<=j<cols and grid[i][j]==1:
                    grid[i][j]=2
                    fresh-=1
                    que.append((i,j))



            minutes+=1
        if fresh ==0:
            return minutes
        else :
            return -1