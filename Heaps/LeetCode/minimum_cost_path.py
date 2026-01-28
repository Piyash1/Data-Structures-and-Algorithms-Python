# Leetcode - 3651. Minimum Cost Path with Teleportations

from typing import List
import heapq

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        
        # visited [row][col][teleportations_used]
        visited = [[[False] * (k+1) for _ in range(n)] for _ in range(m)]
        
        # pre - store all cells sorted by their values
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((grid[i][j], i, j))
        cells.sort()
        
        heap = [(0, 0, 0, 0)]  # (cost, row, col, teleportations_used)
        
        teleport_ptr = [0] * (k + 1)
        
        while heap:
            cost, r, c, t = heapq.heappop(heap)
            if r == m - 1 and c == n - 1:
                return cost

            if visited[r][c][t]:
                continue
            visited[r][c][t] = True
            
            # moves right
            if c + 1 < n:
                new_cost = cost + grid[r][c+1]
                heapq.heappush(heap, (new_cost, r, c + 1, t))
            
            # moves down
            if r + 1 < m:
                new_cost = cost + grid[r+1][c]
                heapq.heappush(heap, (new_cost, r + 1, c, t))
            
            # teleportation
            if t < k:
                ptr = teleport_ptr[t]
                while ptr < len(cells) and cells[ptr][0] <= grid[r][c]:
                    _, i, j = cells[ptr]
                    heapq.heappush(heap, (cost, i, j, t + 1))
                    ptr += 1
                teleport_ptr[t] = ptr

        
        return -1

# Example usage:
solution = Solution()
grid = [[1,3,3],[2,5,4],[4,3,5]]
k = 2
print(solution.minCost(grid, k))