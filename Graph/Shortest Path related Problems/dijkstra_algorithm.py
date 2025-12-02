import heapq
import sys

class Solution:
    def dijkstra(self, V, edges, src):
        adj_list = [[] for _ in range(V)]
        
        # UNDIRECTED graph
        for u, v, d in edges:
            adj_list[u].append((v, d))
            adj_list[v].append((u, d))  # add reverse edge
        
        distance = [float('inf')] * V
        distance[src] = 0
        
        pq = [(0, src)]
        
        while pq:
            curr_dist, node = heapq.heappop(pq)
            
            if curr_dist > distance[node]:
                continue
            
            for adj_node, weight in adj_list[node]:
                new_dist = curr_dist + weight
                if new_dist < distance[adj_node]:
                    distance[adj_node] = new_dist
                    heapq.heappush(pq, (new_dist, adj_node))
        
        return distance
    
    def dijkstra_set(self, V, edges, src):
        adj_list = [[] for _ in range(V)]
        
        # UNDIRECTED graph
        for u, v, d in edges:
            adj_list[u].append((v, d))
            adj_list[v].append((u, d))
        
        distance = [sys.maxsize] * V
        distance[src] = 0
        my_set = set()
        my_set.add((0, src))
        
        while len(my_set) != 0:
            dist, node = min(my_set)
            my_set.discard((dist, node))
            for adj_node, weight in adj_list[node]:
                dist_travel = dist + weight
                if dist_travel < distance[adj_node]:
                    if distance[adj_node] != sys.maxsize:
                        my_set.discard((distance[adj_node], adj_node))
                    distance[adj_node] = dist_travel
                    my_set.add((dist_travel, adj_node))
        return distance
        

sol = Solution()
V = 3
edges = [[0,1,1], [1,2,3], [0,2,6]]
src = 2
print(sol.dijkstra(V, edges, src))