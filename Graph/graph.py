class Graph:
    def __init__(self, n, edges):
        self.n = n
        self.edges = edges

    # using matrix
    def graph_matrix(self):
        graph = [[0 for _ in range(self.n+1)] for _ in range(self.n+1)]
        for u, v in self.edges:
            graph[u][v] = 1
            graph[v][u] = 1  # undirected
        return graph

    # using adjacency list
    def graph_adj_list(self):
        adj_list = [[] for _ in range(self.n+1)]
        for u, v in self.edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        return adj_list

    # using dictionary
    def graph_dict(self):
        my_dict = {i: [] for i in range(1, self.n+1)}
        for u, v in self.edges:
            my_dict[u].append(v)
            my_dict[v].append(u)
        return my_dict

    # -----------------------
    # Helper Print Methods
    # -----------------------
    def print_matrix(self):
        matrix = self.graph_matrix()
        for row in matrix:
            print(row)

    def print_adj_list(self):
        adj_list = self.graph_adj_list()
        for i in range(1, len(adj_list)):
            print(f"{i}: {adj_list[i]}")

    def print_dict(self):
        graph_dict = the_dict = self.graph_dict()
        for key, val in graph_dict.items():
            print(f"{key}: {val}")


# -----------------------------
# Example usage
# -----------------------------
n = 5
edges = [[1, 2], [2, 4], [3, 4], [1, 3], [3, 5], [5, 4]]

g = Graph(n, edges)

print("Matrix:")
g.print_matrix()

print("\nAdjacency List:")
g.print_adj_list()

print("\nDictionary:")
g.print_dict()
