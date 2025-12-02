# Shortest path in Undirected Graph

from collections import deque
class Solution:
    def shortestPath(self, V, edges, src):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        n = len(adj)
        distance = [-1 for _ in range(n)]
        queue = deque()
        queue.append([src, 0])
        distance[src] = 0
        
        while queue:
            node, dis_travel = queue.popleft()
            for adj_node in adj[node]:
                if distance[adj_node] == -1:
                    distance[adj_node] = dis_travel+1
                    queue.append([adj_node, dis_travel+1])
        return distance

sol = Solution()
V = 9
edges = [[0, 1], [0, 3], [1, 2], [3, 4], [4, 5], [2, 6], [5, 6], [6, 7], [6, 8], [7, 8]]
src = 0
print(sol.shortestPath(V, edges, src))