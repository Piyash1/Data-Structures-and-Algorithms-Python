# 3619. Count Islands With Total Value Divisible by K
#
from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m:
                return 0
            
            if grid[i][j] == 0:
                return 0

            total = grid[i][j]
            grid[i][j] = 0

            total += dfs(i-1, j)
            total += dfs(i+1, j)
            total += dfs(i, j-1)
            total += dfs(i, j+1)

            return total

        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    island_sum = dfs(i, j)

                    if island_sum % k == 0:
                        count += 1
        
        return count


# Example usage
if __name__ == "__main__":
    solution = Solution()
    grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]]
    k = 5
    print(solution.countIslands(grid, k))
