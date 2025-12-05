class DisjointSet:
    def __init__(self, n):
        # parent[i] = parent of node i
        # Initially each node is its own parent (all separate sets)
        self.parent = [i for i in range(n + 1)]

        # rank[i] = approximate height of the tree rooted at i
        self.size = [1] * (n + 1)
    
    def find(self, x):
        """
        Find the ultimate parent (representative) of x.
        Path Compression Optimization:
        Make each node on the path directly point to the root.
        This makes future queries very fast.
        """
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])  # Recursive path compression
        return self.parent[x]
    
    def union(self, u, v):
        """
        Union two sets given by nodes u and v.
        Uses Union By Rank:
        Attach the smaller-ranked tree under the larger-ranked tree.
        """
        pu = self.find(u)  # Find parent of u
        pv = self.find(v)  # Find parent of v
        
        # If both nodes have the same parent, they are already in the same set
        if pu == pv:
            return
        
        # Attach smaller rank tree under bigger rank tree
        if self.size[pu] < self.size[pv]:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        elif self.size[pu] > self.size[pv]:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
        else:
            # Both have same size → choose one as parent and increase its size
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]


# ------------------- TESTING THE DSU -------------------

# Create DSU for elements 1 to 7
ds = DisjointSet(7)

# Perform unions
ds.union(1, 2)
ds.union(2, 3)
ds.union(4, 5)
ds.union(6, 7)
ds.union(5, 6)
ds.union(3, 7)

# Check if 1 and 7 end up in the same connected component
print(ds.find(1))   # Prints representative of set containing 1
print(ds.find(7))   # Prints representative of set containing 7 (must match above)
print(ds.size)
