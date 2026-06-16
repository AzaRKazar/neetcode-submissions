class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
    # Import deque from collections because it provides an efficient queue
# BFS requires a queue structure where we remove elements from the front
    
        
        # Edge Case 1:
        # If the grid itself is empty, then there are no fruits
        # So the answer will be 0 minutes
        if not grid or not grid[0]:
            return 0
        
        # Get number of rows in the grid
        rows = len(grid)
        
        # Get number of columns in the grid
        cols = len(grid[0])
        
        # Create a queue for BFS traversal
        # This queue will store positions of rotten fruits
        queue = deque()
        
        # Variable to count number of fresh fruits
        fresh_count = 0
        
        # STEP 1: Scan the entire grid
        # We iterate through all cells to find
        # 1) Initial rotten fruits
        # 2) Total fresh fruits
        for r in range(rows):               # r represents row index
            for c in range(cols):           # c represents column index
                
                # If the cell contains a rotten fruit
                if grid[r][c] == 2:
                    # Add its position into the BFS queue
                    # This acts as a starting point for rotting
                    queue.append((r, c))
                
                # If the cell contains a fresh fruit
                elif grid[r][c] == 1:
                    # Increase the fresh fruit count
                    fresh_count += 1
        
        # If there are no fresh fruits initially
        # No time is needed
        if fresh_count == 0:
            return 0
        
        # Directions for neighbor traversal
        # We will check four directions
        # Up, Down, Left, Right
        directions = [
            (-1, 0),   # move up
            (1, 0),    # move down
            (0, -1),   # move left
            (0, 1)     # move right
        ]
        
        # Variable to track minutes passed
        minutes = 0
        
        # STEP 2: BFS Traversal
        # Continue until queue becomes empty
        while queue:
            
            # The size of queue represents
            # how many rotten fruits exist in this minute
            level_size = len(queue)
            
            # Flag to check if any fruit rotted in this minute
            rotted_this_round = False
            
            # Process all rotten fruits of this minute
            for _ in range(level_size):
                
                # Remove one rotten fruit position from queue
                row, col = queue.popleft()
                
                # Check all 4 neighbors
                for dr, dc in directions:
                    
                    # Compute neighbor cell position
                    new_row = row + dr
                    new_col = col + dc
                    
                    # Check if the neighbor is inside grid boundaries
                    if (0 <= new_row < rows and 0 <= new_col < cols):
                        
                        # If neighbor is a fresh fruit
                        if grid[new_row][new_col] == 1:
                            
                            # Convert fresh fruit into rotten fruit
                            grid[new_row][new_col] = 2
                            
                            # Reduce fresh fruit count
                            fresh_count -= 1
                            
                            # Add this new rotten fruit into queue
                            # It will rot others in the next minute
                            queue.append((new_row, new_col))
                            
                            # Mark that rotting happened this minute
                            rotted_this_round = True
            
            # If at least one fruit rotted this round
            # then one minute has passed
            if rotted_this_round:
                minutes += 1
        
        # After BFS completes
        # If fresh fruits still remain
        # it means some fruits were unreachable
        if fresh_count > 0:
            return -1
        
        # Otherwise return total minutes needed
        return minutes