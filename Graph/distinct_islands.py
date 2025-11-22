# Given a boolean 2D matrix grid of size n * m. You have to find the number of distinct islands where a group of connected 1s (horizontally or vertically) forms an island. Two islands are considered to be distinct if and only if one island is not equal to another (not rotated or reflected).

from typing import List

class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        distinct_islands = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and not visited[r][c]:
                    shape = []
                    self.dfs(r, c, r, c, grid, visited, shape,  rows, cols)
                    distinct_islands.add(tuple(shape))
        return len(distinct_islands)

    
    def dfs(self, base_i, base_j, i, j, grid, visited, shape, rows, cols):
        visited[i][j] = 1
        shape.append((i - base_i, j - base_j))
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        for dx, dy in directions:
            new_i, new_j = i + dx, j + dy
            if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                continue
            if grid[new_i][new_j] == 0:
                continue
            if visited[new_i][new_j] == 1:
                continue
            self.dfs(base_i, base_j, new_i, new_j, grid, visited, shape, rows, cols)
    
# Example usage:
if __name__ == "__main__":
    grid = [
        [1, 1, 0, 0, 0],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 0, 0]
    ]
    solution = Solution()
    result = solution.countDistinctIslands(grid)
    print(result)  # Output: 3