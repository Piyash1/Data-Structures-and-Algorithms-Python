from typing import List

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False

        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
        return True

class Solution:
    def spanningTree(self, V: int, adj: List[List[List[int]]]):
        """
        V: number of vertices
        adj: adjacency list where adj[u] = [[v1, w1], [v2, w2], ...]
             meaning edge from u to v1 with weight w1, etc.
        """
        edges = []
        seen = set()
        
        # Extract all unique edges from adjacency list
        for u in range(V):
            for neighbour in adj[u]:
                v, w = neighbour
                # Use tuple to avoid duplicates (undirected graph)
                if (min(u, v), max(u, v)) not in seen:
                    seen.add((min(u, v), max(u, v)))
                    edges.append((w, u, v))
        
        # Sort edges by weight
        edges.sort()
        
        dsu = DisjointSet(V)
        mst_weight = 0
        
        # Process edges in increasing order of weight
        for w, u, v in edges:
            if dsu.union(u, v):
                mst_weight += w  # Add weight, not 1
        
        return mst_weight


# Example 1: Simple graph
print("Example 1:")
print("Graph: 0---1 (weight=2)")
print("       |   |")
print("       5   3")
print("       |   |")
print("       2---3 (weight=4)")
V1 = 4
adj1 = [
    [[1, 2], [2, 5]],      # Node 0: edges to 1(w=2), 2(w=5)
    [[0, 2], [3, 3]],      # Node 1: edges to 0(w=2), 3(w=3)
    [[0, 5], [3, 4]],      # Node 2: edges to 0(w=5), 3(w=4)
    [[1, 3], [2, 4]]       # Node 3: edges to 1(w=3), 2(w=4)
]
sol = Solution()
result1 = sol.spanningTree(V1, adj1)
print(f"MST Weight: {result1}")  # Should be 9 (edges: 0-1=2, 1-3=3, 2-3=4)
print()

# Example 2: More complex graph
print("Example 2:")
print("Graph with 5 vertices:")
V2 = 5
adj2 = [
    [[1, 2], [3, 6]],           # 0 -> 1(2), 3(6)
    [[0, 2], [2, 3], [3, 8], [4, 5]],  # 1 -> 0(2), 2(3), 3(8), 4(5)
    [[1, 3], [4, 7]],           # 2 -> 1(3), 4(7)
    [[0, 6], [1, 8], [4, 9]],   # 3 -> 0(6), 1(8), 4(9)
    [[1, 5], [2, 7], [3, 9]]    # 4 -> 1(5), 2(7), 3(9)
]
result2 = sol.spanningTree(V2, adj2)
print(f"MST Weight: {result2}")  # Should be 16 (edges: 0-1=2, 1-2=3, 1-4=5, 0-3=6)
print()

# Example 3: Triangle
print("Example 3: Triangle")
print("  0")
print(" /|\\")
print("1-2")
V3 = 3
adj3 = [
    [[1, 1], [2, 2]],      # 0 -> 1(1), 2(2)
    [[0, 1], [2, 3]],      # 1 -> 0(1), 2(3)
    [[0, 2], [1, 3]]       # 2 -> 0(2), 1(3)
]
result3 = sol.spanningTree(V3, adj3)
print(f"MST Weight: {result3}")  # Should be 3 (edges: 0-1=1, 0-2=2)