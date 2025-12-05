# Leetcode no.1319 - Number of Operations to Make Network Connected

from typing import List

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
            return True
        
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
        return False


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        ds = Disjoint(n)
        extra_edges = 0
        for u, v in connections:
            if ds.union(u, v):
                extra_edges += 1
        
        components = 0
        for i in range(n):
            if ds.find(i) == i:
                components += 1

        if extra_edges >= components - 1:
            return components - 1
        return -1


sol = Solution()
n = 4
connections = [[0,1],[0,2],[1,2]]
print(sol.makeConnected(n, connections))