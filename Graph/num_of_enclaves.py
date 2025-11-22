# Leetcode no.1020 - Number of Enclaves

from collections import deque

class Solution(object):
    def numEnclaves(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        queue = deque()
        
        # 1. Add ONLY boundary LAND cells to the queue
        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    # Only add to queue if it is actually land (1)
                    if grid[r][c] == 1:
                        queue.append((r, c))
                        visited[r][c] = 1
        
        # 2. BFS to find all land connected to the boundary
        while queue:
            i, j = queue.popleft() # Fixed: added () to call the method
            
            directions = [(1,0), (0,1), (-1,0), (0,-1)]
            for x, y in directions:
                new_i = x + i
                new_j = y + j
                
                # Check bounds
                if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                    continue
                # Check if water
                if grid[new_i][new_j] == 0:
                    continue
                
                # Check if land and not visited yet
                if grid[new_i][new_j] == 1 and visited[new_i][new_j] == 0:
                    queue.append((new_i, new_j))
                    visited[new_i][new_j] = 1
        
        # 3. Count the enclaves (Land cells that were NOT visited)
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and visited[r][c] == 0:
                    count += 1
                    
        return count

# Example usage:
if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
    ]
    solution = Solution()
    result = solution.numEnclaves(grid)
    print("Number of enclaves:", result)
    

# Optimized BFS(in-place modification)
from collections import deque

class Solution(object):
    def numEnclaves(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        
        # --- Optimization B: Boundary Loops only ---
        # Add boundary land cells to queue and mark as 0 (visited) immediately
        for r in range(rows):
            for c in range(cols):
                # We only care about the edges
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    if grid[r][c] == 1:
                        grid[r][c] = 0  # Optimization A: Change '1' to '0' in-place
                        queue.append((r, c))
        
        # --- BFS ---
        while queue:
            i, j = queue.popleft()
            directions = [(1,0), (0,1), (-1,0), (0,-1)]
            for x, y in directions:
                new_i = x + i
                new_j = y + j
                if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                        continue
                if grid[new_i][new_j] == 0:
                    continue
                if grid[new_i][new_j] == 1:
                    grid[new_i][new_j] = 0
                    queue.append((new_i, new_j))
        
        # --- Final Count ---
        # Since we turned all boundary-connected land to 0, 
        # any remaining 1s are true enclaves.
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    count += 1
                    
        return count