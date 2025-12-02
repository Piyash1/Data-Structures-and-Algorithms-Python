class Solution:
    def bellmanFord(self, V, edges, src):
        dist = [10**8 for _ in range(V)]
        dist[src] = 0
        
        for _ in range(V - 1): # (n-1)
            for u, v, w in edges:
                if dist[u] != 10**8:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
        
        for u, v, w in edges:
            if dist[u] != 10**8:
                if dist[u] + w < dist[v]:
                    return [-1]
        
        return dist


sol = Solution()
V = 5
edges = [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]]
src = 0
print(sol.bellmanFord(V, edges, src))