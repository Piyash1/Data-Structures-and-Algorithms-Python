# Leetcode no.1631 - Path With Minimum Effort

from typing import List
import sys
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        effort_arr = [[sys.maxsize for _ in range(cols)] for _ in range(rows)]
        effort_arr[0][0] = 0
        pq = [[0, 0, 0]] # [d, i, j]
        
        while pq:
            effort, i, j = heapq.heappop(pq)
            if i == rows-1 and j == cols-1:
                return effort
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for x, y in directions:
                new_i, new_j = x + i, y + j
                if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                    continue
                new_effort = max(effort, abs(heights[new_i][new_j] - heights[i][j]))
                if new_effort < effort_arr[new_i][new_j]:
                    effort_arr[new_i][new_j] = new_effort
                    heapq.heappush(pq, [new_effort, new_i, new_j])
                    

sol = Solution()
heights = [[1,2,2],[3,8,2],[5,3,5]]
print(sol.minimumEffortPath(heights))