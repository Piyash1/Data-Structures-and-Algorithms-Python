# Leetcode no.1334 - Find the City With the Smallest Number of Neighbors at a Threshold Distance

from typing import List
import sys

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj_matrix = [[sys.maxsize for _ in range(n)] for _ in range(n)]
        for u, v, w in edges:
            adj_matrix[u][v] = w
            adj_matrix[v][u] = w
        
        for i in range(n):
            adj_matrix[i][i] = 0
        
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if adj_matrix[i][via] != sys.maxsize and adj_matrix[via][j] != sys.maxsize:
                        adj_matrix[i][j] = min(adj_matrix[i][j], adj_matrix[i][via] + adj_matrix[via][j])
        
        min_neighbours = n
        city = -1
        for i in range(n): # city
            count = 0
            for j in range(n):
                if adj_matrix[i][j] <= distanceThreshold:
                    count += 1
            if count <= min_neighbours:
                min_neighbours = count
                city = i
        return city


sol = Solution()
n = 4
edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
distanceThreshold = 4
print(sol.findTheCity(n, edges, distanceThreshold))