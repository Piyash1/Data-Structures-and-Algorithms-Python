# Leetcode no.1091 - Shortest Path in Binary Matrix

from typing import List
import sys
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        rows = len(grid)
        cols = len(grid[0])
        distance = [[sys.maxsize for _ in range(cols)] for _ in range(rows)]
        distance[0][0] = 1
        
        queue = deque()
        queue.append([1, 0, 0])
        while queue:
            dist, i, j = queue.popleft()
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, 1], [-1, -1], [1, -1], [1, 1]]
            for x , y in directions:
                new_i = x + i
                new_j = y + j
                if new_i < 0 or new_i >= rows or new_j <0 or new_j >= cols:
                    continue
                if grid[new_i][new_j] == 1:
                    continue
                dist_travel = dist + 1
                if dist_travel < distance[new_i][new_j]:
                    if new_i == rows-1 and new_j == cols-1:
                        return dist_travel
                    distance[new_i][new_j] = dist_travel
                    queue.append([dist_travel, new_i, new_j])
        
        if distance[rows-1][cols-1] == sys.maxsize:
            return -1
        return distance[rows-1][cols-1]
    
sol = Solution()
grid = [[0,1],[1,0]]
print(sol.shortestPathBinaryMatrix(grid))