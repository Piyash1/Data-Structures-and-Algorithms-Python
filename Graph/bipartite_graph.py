# Leetcode no.785 - Is Graph Bipartite?

class Solution(object):
    def isBipartite(self, graph):
        total_nodes = len(graph)
        visited = [-1] * total_nodes  # -1: uncolored, 0: color A, 1: color B
        for index in range(total_nodes):
            if visited[index] == -1:
                ans = self.dfs(index, 0, graph, visited)
                if ans == False:
                    return False
        return True 
    
    def dfs(self, curr_node, color, graph, visited):
        visited[curr_node] = color
        for adj_node in graph[curr_node]:
            if visited[adj_node] == -1:
                ans = self.dfs(adj_node, 1 - color, graph, visited)
                if ans == False:
                    return False
            elif visited[adj_node] == color:
                return False
        return True
    
# Example usage:
if __name__ == "__main__":
    graph = [[1,3],[0,2],[1,3],[0,2]]
    solution = Solution()
    result = solution.isBipartite(graph)
    print(result)  # Output: True