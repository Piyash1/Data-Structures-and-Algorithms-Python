from collections import deque

class GraphTraversal:
    def bfs(self, adj, start):
        n = len(adj)
        result = []
        visited = [0] * n  
        
        queue = deque([start])
        visited[start] = 1
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = 1
                    queue.append(neighbor)
        return result

    def dfs(self, adj, start):
        n = len(adj)
        result = []
        visited = [0] * n  

        def dfs_helper(node):
            visited[node] = 1
            result.append(node)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs_helper(neighbor)

        dfs_helper(start)
        return result

# Example usage:
if __name__ == "__main__":
    graph = GraphTraversal()
    adj = [
        [2, 3, 1],
        [0],
        [0, 4],
        [0],
        [2]
    ]
    start = 0
    bfs = graph.bfs(adj, start)
    dfs = graph.dfs(adj, start)
    print("BFS:", bfs)
    print("DFS:", dfs)