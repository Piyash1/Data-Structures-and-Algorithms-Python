# https://www.geeksforgeeks.org/problems/count-number-of-edges-in-an-undirected-graph/1

class Solution:
    def countEdges(self, adj: list[list[int]]) -> int:
        total = 0

        for i in range(len(adj)):
            total += len(adj[i])  # Count all connections

        # Undirected edges are counted twice, so divide by 2
        return total // 2


solution = Solution()
adj = [[1, 2], [0, 2], [0, 1, 3], [2]]
print(solution.countEdges(adj))
