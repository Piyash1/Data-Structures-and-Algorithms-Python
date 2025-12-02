# Leetcode1976 - Number of Ways to Arrive at Destination

from typing import List
import sys
import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        for u, v, w in roads:
            adj_list[u].append([v, w])
            adj_list[v].append([u, w])
        
        MOD = 10 ** 9 +7
        distance = [sys.maxsize for _ in range(n)]
        ways = [sys.maxsize for _ in range(n)]
        distance[0] = 0
        ways[0] = 1
        
        priority_queue = [[0, 0]] # dist, node
        while priority_queue:
            dist, node = heapq.heappop(priority_queue)
            for adj_node, weight in adj_list[node]:
                new_distance = dist + weight
                if new_distance < distance[adj_node]:
                    distance[adj_node] = new_distance
                    heapq.heappush(priority_queue, [new_distance, adj_node])
                    ways[adj_node] = ways[node]
                elif new_distance == distance[adj_node]:
                    ways[adj_node] += ways[node]
        
        return ways[n-1] % MOD



sol = Solution()
n = 7
roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
print(sol.countPaths(n, roads))