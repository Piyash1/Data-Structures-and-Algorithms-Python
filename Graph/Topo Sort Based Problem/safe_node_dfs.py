from typing import List
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)
        visited = [0 for _ in range(V)]
        path_visited = [0 for _ in range(V)]
        is_safe = [0 for _ in range(V)]
        
        for i in range(V):
            if visited[i] == 0:
                self.dfs(i, graph, visited, path_visited, is_safe)
                
        result = []
        for i in range(V):
            if is_safe[i] == 1:
                result.append(i)
        return result
    
    
    def dfs(self, current_node, graph, visited, path_visited, is_safe):
        visited[current_node] = 1
        path_visited[current_node] = 1
        
        for adj_node in graph[current_node]:
            if visited[adj_node] == 0:
                ans = self.dfs(adj_node, graph, visited, path_visited, is_safe)
                if ans == False:
                    return False
            elif path_visited[adj_node] == 1:
                return False
        is_safe[current_node] = 1
        path_visited[current_node] = 0
        return True
                   
        
# Example usage:
if __name__ == "__main__":
    graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    solution = Solution()
    print(solution.eventualSafeNodes(graph))