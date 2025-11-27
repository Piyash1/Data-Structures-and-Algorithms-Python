# Leetcode no.802. Find Eventual Safe States

from collections import deque
from typing import List
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)
        adj_list = [[] for _ in range(V)]
        in_degree = [0 for _ in range(V)]
        
        # Reversing the graph and calculating in-degrees
        for node in range(V):
            for adj_node in graph[node]:
                adj_list[adj_node].append(node)
                in_degree[node] += 1
        
        queue = deque()
        result = []
        # Finding all nodes with in-degree 0
        for node in range(V):
            if in_degree[node] == 0:
                queue.append(node)
        # Topological Sort
        while queue:
            current_node = queue.popleft()
            result.append(current_node)
            for adj_node in adj_list[current_node]:
                in_degree[adj_node] -= 1
                if in_degree[adj_node] == 0:
                    queue.append(adj_node)
        result.sort()
        return result

# Example usage:
if __name__ == "__main__":
    graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    solution = Solution()
    print(solution.eventualSafeNodes(graph))  # Output: [2,4,5,6]