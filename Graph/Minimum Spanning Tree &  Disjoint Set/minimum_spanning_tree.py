import heapq

class Solution:
    def spanningTree(self, V, edges):
        adj_list = [[] for _ in range(V)]
        for u, v, w in edges:
            adj_list[u].append([v, w])
            adj_list[v].append([u, w])
            
        mst = []
        Sum = 0
        visited = [0 for _ in range(V)]
        
        priority_queue = []
        heapq.heappush(priority_queue, [0, 0, -1]) # wt, node, parent
        while priority_queue:
            wt, node, parent = heapq.heappop(priority_queue)
            if visited[node] == 0:
                visited[node] = 1
                if parent != -1:
                    Sum += wt
                    mst.append([parent, node])
                for adj_node, weight in adj_list[node]:
                    if visited[adj_node] == 0:
                        heapq.heappush(priority_queue, [weight, adj_node, node])
        return Sum

sol = Solution()
V = 3
Edges = [[0, 1, 5], [1, 2, 3], [0, 2, 1]]
print(sol.spanningTree(V, Edges))