# Given a Directed Acyclic Graph (DAG) of V (0 to V-1) vertices and E edges represented as a 2D list of edges[][], where each entry edges[i] = [u, v] denotes a directed edge u -> v. Return the topological sort for the given graph.

class Solution:
    def topoSort(self, V, edges):
        adj_list = [[] for _ in range(V)]
        for u, v in edges:
            adj_list[u].append(v)
        
        stack = []
        visited = [0 for _ in range(V)]
        for i in range(V):
            if visited[i] == 0:
                self.dfs(i, visited, stack, adj_list)
        return stack[::-1]
        
    def dfs(self, current_node, visited, stack, adj_list):
        visited[current_node] = 1
        for adj_node in adj_list[current_node]:
            if visited[adj_node] == 0:
                self.dfs(adj_node, visited, stack, adj_list)
        
        stack.append(current_node)

# Example usage:
if __name__ == "__main__":
    V = 6
    edges = [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]
    solution = Solution()
    print(solution.topoSort(V, edges))  # Output could be [5, 4, 2, 3, 1, 0] or any valid topological order