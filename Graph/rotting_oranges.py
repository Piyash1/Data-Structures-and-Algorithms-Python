# Leetcode no.994 - Rotting Oranges

from copy import deepcopy
from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        grid_copy = deepcopy(grid)
        
        fresh_count = 0
        queue = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid_copy[r][c] == 2:
                    queue.append((r, c))
                elif grid_copy[r][c] == 1:
                    fresh_count += 1
        
        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while len(queue) != 0 and fresh_count > 0:
            minutes += 1
            total_rotten = len(queue)
            for _ in range(total_rotten):
                i, j = queue.popleft()
                for dx, dy in directions:
                    new_i, new_j = i + dx, j + dy
                    if new_i < 0 or new_i == rows or new_j < 0 or new_j == cols:
                        continue
                    if grid_copy[new_i][new_j] == 1:
                        grid_copy[new_i][new_j] = 2
                        fresh_count -= 1
                        queue.append((new_i, new_j))
        if fresh_count > 0:
            return -1
        return minutes

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    grid = [
        [2,1,1],
        [1,1,0],
        [0,1,1]
    ]
    result = solution.orangesRotting(grid)
    print("Minutes until all oranges rot:", result)