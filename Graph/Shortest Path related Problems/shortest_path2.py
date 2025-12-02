from typing import List

class Solution:
    # ---------- DFS for topological sort ----------
    def dfs(self, node, stack, visited, adj_list):
        visited[node] = 1
        for adjNode, _ in adj_list[node]:         # ignore weight during DFS
            if visited[adjNode] == 0:
                self.dfs(adjNode, stack, visited, adj_list)
        stack.append(node)                        # post-order push

    # ---------- main function ----------
    def shortestPath(self, V: int, E: int, edges: List[List[int]]) -> List[int]:
        # 1. Build adjacency list
        adj_list = [[] for _ in range(V)]
        for u, v, w in edges:                     # directed edge u -> v (weight w)
            adj_list[u].append([v, w])

        # 2. Topological sort by DFS
        stack   = []
        visited = [0] * V
        for i in range(V):
            if visited[i] == 0:
                self.dfs(i, stack, visited, adj_list)

        # 3. Initialise distance array
        distance = [float("inf")] * V
        distance[0] = 0                           # source vertex

        # 4. Relax edges following topological order
        while stack:                              # pop = left-to-right order
            node = stack.pop()
            if distance[node] == float("inf"):    # unreachable so far
                continue
            for adjNode, w in adj_list[node]:
                new_d = distance[node] + w
                if new_d < distance[adjNode]:
                    distance[adjNode] = new_d

        # 5. Replace infinity by -1 as problem demands
        for i in range(V):
            if distance[i] == float("inf"):
                distance[i] = -1
        return distance
    

sol = Solution()
V = 6
E = 7
edges = [
    [0, 1, 2],  # 0 -> 1 (weight 2)
    [0, 4, 1],  # 0 -> 4 (weight 1)
    [1, 2, 3],  # 1 -> 2 (weight 3)
    [4, 2, 2],  # 4 -> 2 (weight 2)
    [4, 5, 4],  # 4 -> 5 (weight 4)
    [2, 3, 6],  # 2 -> 3 (weight 6)
    [5, 3, 1]   # 5 -> 3 (weight 1)
]
result = sol.shortestPath(V, E, edges)
print(f"Vertices: {V}, Edges: {E}")
print(f"Shortest distances from vertex 0: {result}")
print()