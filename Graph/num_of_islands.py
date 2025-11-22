# Leetcode no.200 - Number of Islands

from collections import deque
class Solution(object):
    def numIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        count = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and not visited[r][c]:
                    count += 1
                    self.bfs(r, c, grid, visited)
        return count

    def bfs(self, i, j, grid, visited):
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        queue.append((i, j))
        visited[i][j] = 1
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                new_i, new_j = x + dx, y + dy
                if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                    continue
                if grid[new_i][new_j] == '0':
                    continue
                if visited[new_i][new_j] == 1:
                    continue
                visited[new_i][new_j] = 1
                queue.append((new_i, new_j))
                
# Example usage:
if __name__ == "__main__":
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    solution = Solution()
    result = solution.numIslands(grid)
    print(result) 
        

# # DFS Approach
# class Solution(object):
#     def numIslands(self, grid):
#         rows = len(grid)
#         cols = len(grid[0])
#         visited = [[0 for _ in range(cols)] for _ in range(rows)]
#         count = 0

#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == "1" and not visited[r][c]:
#                     count += 1
#                     self.dfs(r, c, grid, visited)
#         return count

#     def dfs(self, i, j, grid, visited):
#         rows = len(grid)
#         cols = len(grid[0])

#         if i < 0 or i >= rows or j < 0 or j >= cols:
#             return
#         if grid[i][j] == "0":
#             return
#         if visited[i][j] == 1:
#             return

#         visited[i][j] = 1
        
#         self.dfs(i + 1, j, grid, visited)
#         self.dfs(i - 1, j, grid, visited)
#         self.dfs(i, j - 1, grid, visited)
#         self.dfs(i, j + 1, grid, visited)
