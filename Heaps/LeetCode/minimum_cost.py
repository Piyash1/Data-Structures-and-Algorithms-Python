# Leetcode-3650. Minimum Cost Path with Edge Reversals

import heapq
from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, 2 * w))
        
        dist = [float('inf')] * n
        dist[0] = 0
        
        heap = [(0, 0)]  # (cost, node)
        
        while heap:
            current_cost, node = heapq.heappop(heap)
            if current_cost > dist[node]:
                continue
            
            for neighbour, cost in graph[node]:
                new_cost = current_cost + cost
                if new_cost < dist[neighbour]:
                    dist[neighbour] = new_cost
                    heapq.heappush(heap, (new_cost, neighbour))
        
        return dist[n - 1] if dist[n - 1] != float('inf') else -1

# Example usage:
solution = Solution()
n = 4
edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]
print(solution.minCost(n, edges)) 