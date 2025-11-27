# Given a Directed Acyclic Graph (DAG) of V (0 to V-1) vertices and E edges represented as a 2D list of edges[][], where each entry edges[i] = [u, v] denotes a directed edge u -> v. Return the topological sort for the given graph.(Kahn's Algorithm - BFS Approach)

from collections import deque

class Solution:
    def topoSort(self, V, edges):
        adj_list = [[] for _ in range(V)]
        in_degree = [0 for _ in range(V)]
        for u, v in edges:
            adj_list[u].append(v)
            in_degree[v] += 1
        
        queue = deque()
        result = []
        for i in range(V):
            if in_degree[i] == 0:
                queue.append(i)
        
        while queue:
            current_node = queue.popleft()
            result.append(current_node)
            for adj_node in adj_list[current_node]:
                in_degree[adj_node] -= 1
                if in_degree[adj_node] == 0:
                    queue.append(adj_node)
        return result
        
# Example usage:
if __name__ == "__main__":
    V = 6
    edges = [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]
    solution = Solution()
    print(solution.topoSort(V, edges))  # Output could be [5, 4, 2, 3, 1, 0] or any valid topological order