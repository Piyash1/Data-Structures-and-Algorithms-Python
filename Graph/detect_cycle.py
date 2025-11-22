# Given an undirected graph with V vertices and E edges, represented as a 2D vector edges[][], where each entry edges[i] = [u, v] denotes an edge between vertices u and v, determine whether the graph contains a cycle or not.

from collections import deque

class Solution:
    def isCycle(self, V, edges):
        # Build adjacency list
        adj_list = [[] for _ in range(V)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = [0] * V
        
        # Check all components
        for i in range(V):
            if visited[i] == 1:
                continue

            queue = deque()
            queue.append((i, -1))  # (node, parent)
            visited[i] = 1

            while queue:
                node, parent = queue.popleft()

                for neighbor in adj_list[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = 1
                        queue.append((neighbor, node))
                    elif neighbor != parent:
                        # Found a cycle
                        return True

        return False


# Example usage:
if __name__ == "__main__":
    V = 5
    edges = [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4]]
    solution = Solution()
    if solution.isCycle(V, edges):
        print("Graph contains a cycle")
    else:
        print("Graph does not contain a cycle")
    
# # DFS approach
# class Solution:
#     def isCycle(self, V, edges):
#         adj_list = [[] for _ in range(V)]
#         for u, v in edges:
#             adj_list[u].append(v)
#             adj_list[v].append(u)
        
#         visited = [0] * V
#         for i in range(V):
#             if visited[i] == 1:
#                 continue
#             if self.dfs(i, -1, visited, adj_list):
#                 return True
#         return False
    
#     def dfs(self, node, parent, visited, adj_list):
#         visited[node] = 1
        
#         for neighbor in adj_list[node]:
#             if not visited[neighbor]:
#                 if self.dfs(neighbor, node, visited, adj_list):
#                     return True
#             elif neighbor != parent:
#                 return True
#         return False