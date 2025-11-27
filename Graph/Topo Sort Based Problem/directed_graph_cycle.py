from collections import deque

class Solution:
    def isCyclic(self, V, edges):
        # code here
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
        if len(result) == V:
            return False
        return True
    
# Example usage:
if __name__ == "__main__":
    V = 4
    edges = [[0, 1], [1, 2], [2, 0], [1, 3]]
    solution = Solution()
    print(solution.isCyclic(V, edges))  # Output: True (since there is a cycle: 0 -> 1 -> 2 -> 0)