class Disjoint:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
        
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        
        if pu == pv:
            return
        
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
    
        
class Solution:
    def numProvinces(self, adj, V):
        ds = Disjoint(V)
        
        for i in range(V):
            for j in range(V):
                if adj[i][j] == 1 and i != j:
                    ds.union(i, j)
        
        count = 0
        for i in range(V):
            if ds.find(i) == i:
                count += 1
        return count


sol = Solution()
adj = [
    [1, 1, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 1, 1]
]
print(sol.numProvinces(adj, 4))
