# Graph Data Structure - Introduction & Basics

## Table of Contents
1. [What is a Graph?](#what-is-a-graph)
2. [Real-World Applications](#real-world-applications)
3. [Basic Terminology](#basic-terminology)
4. [Types of Graphs](#types-of-graphs)
5. [Graph Representation](#graph-representation)
6. [Basic Operations](#basic-operations)
7. [Common Graph Algorithms](#common-graph-algorithms)
8. [Practice Problems](#practice-problems)

---

## What is a Graph?

A **Graph** is a non-linear data structure consisting of **vertices (nodes)** and **edges** that connect these vertices. It's used to represent relationships between different entities.

**Formal Definition**: A graph G is defined as:
```
G = (V, E)
where:
  V = Set of vertices
  E = Set of edges connecting pairs of vertices
```

---

## Real-World Applications

- 🌐 **Social Networks**: Friends connections (Facebook, LinkedIn)
- 🗺️ **Maps & Navigation**: Cities and roads (Google Maps)
- 💻 **Network Routing**: Computers and network connections
- 🎬 **Recommendation Systems**: Product/content recommendations
- 🔗 **Web Crawling**: Web page linking
- 📦 **Dependency Resolution**: Package managers (npm, pip)
- 🧬 **Biology**: Protein interaction networks
- ⚡ **Circuit Design**: Electronic circuit analysis

---

## Basic Terminology

| Term | Definition |
|------|------------|
| **Vertex/Node** | A fundamental unit representing an entity |
| **Edge** | A connection between two vertices |
| **Adjacent Vertices** | Two vertices connected by an edge |
| **Degree** | Number of edges connected to a vertex |
| **In-degree** | Number of incoming edges (directed graphs) |
| **Out-degree** | Number of outgoing edges (directed graphs) |
| **Path** | A sequence of vertices where each consecutive pair is connected |
| **Cycle** | A path that starts and ends at the same vertex |
| **Connected Graph** | A graph where there's a path between every pair of vertices |
| **Disconnected Graph** | A graph with isolated components |
| **Subgraph** | A graph formed from a subset of vertices and edges |

---

## Types of Graphs

### 1. Directed Graph (Digraph)
- Edges have direction (A → B is different from B → A)
- **Example**: Twitter followers, web page links, task dependencies

```
    A ──→ B
    ↓     ↓
    C ←── D
```

### 2. Undirected Graph
- Edges have no direction (A — B means both can reach each other)
- **Example**: Facebook friends, road networks

```
    A ──── B
    |      |
    C ──── D
```

### 3. Weighted Graph
- Edges have weights/costs associated with them
- **Example**: Distance between cities, network latency, cost of travel

```
    A ──5── B
    |       |
    3       2
    |       |
    C ──4── D
```

### 4. Unweighted Graph
- All edges are considered equal (no weights)

### 5. Cyclic Graph
- Contains at least one cycle
- **Example**: A → B → C → A

### 6. Acyclic Graph
- Contains no cycles
- **DAG (Directed Acyclic Graph)**: Important for task scheduling, build systems

### 7. Complete Graph
- Every vertex is connected to every other vertex
- For n vertices: **n(n-1)/2** edges

### 8. Bipartite Graph
- Vertices can be divided into two disjoint sets
- Edges only connect vertices from different sets
- **Example**: Job matching, student-course assignments

### 9. Tree
- Special case: Connected acyclic undirected graph
- **n vertices, n-1 edges**

---

## Graph Representation

### 1. Adjacency Matrix

A 2D array where `matrix[i][j] = 1` (or weight) if there's an edge from vertex i to j

**Advantages:**
- ✅ Quick edge lookup: O(1)
- ✅ Good for dense graphs
- ✅ Simple to implement

**Disadvantages:**
- ❌ Space complexity: O(V²)
- ❌ Inefficient for sparse graphs
- ❌ Adding/removing vertices is expensive

**Example:**
```
Graph: 0-1, 0-2, 1-2

Adjacency Matrix:
    0  1  2
0 [ 0  1  1 ]
1 [ 1  0  1 ]
2 [ 1  1  0 ]
```

**Code Implementation:**
```python
# Python
class GraphMatrix:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]
    
    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1  # For undirected graph
```

```java
// Java
class GraphMatrix {
    private int[][] adjMatrix;
    private int vertices;
    
    public GraphMatrix(int v) {
        vertices = v;
        adjMatrix = new int[v][v];
    }
    
    public void addEdge(int u, int v) {
        adjMatrix[u][v] = 1;
        adjMatrix[v][u] = 1; // For undirected graph
    }
}
```

---

### 2. Adjacency List

An array of lists where `list[i]` contains all vertices adjacent to vertex i

**Advantages:**
- ✅ Space efficient: O(V + E)
- ✅ Good for sparse graphs
- ✅ Efficient for iteration
- ✅ Easy to add vertices

**Disadvantages:**
- ❌ Edge lookup: O(V) in worst case
- ❌ Slightly complex implementation

**Example:**
```
Graph: 0-1, 0-2, 1-2

Adjacency List:
0 → [1, 2]
1 → [0, 2]
2 → [0, 1]
```

**Code Implementation:**
```python
# Python
from collections import defaultdict

class GraphList:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph
```

```java
// Java
import java.util.*;

class GraphList {
    private Map<Integer, List<Integer>> adjList;
    
    public GraphList() {
        adjList = new HashMap<>();
    }
    
    public void addEdge(int u, int v) {
        adjList.computeIfAbsent(u, k -> new ArrayList<>()).add(v);
        adjList.computeIfAbsent(v, k -> new ArrayList<>()).add(u); // Undirected
    }
}
```

```cpp
// C++
#include <vector>
#include <list>
using namespace std;

class GraphList {
    int V;
    vector<list<int>> adjList;
    
public:
    GraphList(int v) : V(v), adjList(v) {}
    
    void addEdge(int u, int v) {
        adjList[u].push_back(v);
        adjList[v].push_back(u); // For undirected graph
    }
};
```

---

### 3. Edge List

Simply a list of all edges (pairs of vertices)

**Example:**
```
[(0, 1), (0, 2), (1, 2)]
```

**Best for:** Algorithms like Kruskal's MST that process edges

---

### Comparison Table

| Operation | Adjacency Matrix | Adjacency List |
|-----------|-----------------|----------------|
| **Space** | O(V²) | O(V + E) |
| **Add Edge** | O(1) | O(1) |
| **Check Edge** | O(1) | O(V) |
| **Get All Neighbors** | O(V) | O(degree) |
| **Remove Edge** | O(1) | O(V) |
| **Add Vertex** | O(V²) | O(1) |

---

## Basic Operations

### Time Complexity Summary

| Operation | Adjacency Matrix | Adjacency List |
|-----------|-----------------|----------------|
| Add Vertex | O(V²) | O(1) |
| Add Edge | O(1) | O(1) |
| Remove Vertex | O(V²) | O(V + E) |
| Remove Edge | O(1) | O(V) |
| Check if Edge Exists | O(1) | O(V) |
| Find All Adjacent | O(V) | O(degree) |

---

## Common Graph Algorithms

### 1. Graph Traversal
- **BFS (Breadth-First Search)**: Level-order traversal, shortest path in unweighted graphs
- **DFS (Depth-First Search)**: Explore as far as possible, cycle detection

### 2. Shortest Path Algorithms
- **Dijkstra's Algorithm**: Single source shortest path (non-negative weights)
- **Bellman-Ford**: Single source (handles negative weights)
- **Floyd-Warshall**: All pairs shortest path
- **A* Algorithm**: Heuristic-based shortest path

### 3. Minimum Spanning Tree (MST)
- **Kruskal's Algorithm**: Sort edges, use Union-Find
- **Prim's Algorithm**: Greedy approach, start from a vertex

### 4. Cycle Detection
- **For Undirected**: DFS with parent tracking
- **For Directed**: DFS with recursion stack

### 5. Topological Sorting
- **DFS-based**: For DAGs only
- **Kahn's Algorithm**: BFS-based using in-degree

### 6. Connectivity
- **Connected Components**: DFS/BFS
- **Strongly Connected Components**: Kosaraju's, Tarjan's

### 7. Advanced Algorithms
- **Bridges and Articulation Points**: Tarjan's Algorithm
- **Maximum Flow**: Ford-Fulkerson, Edmonds-Karp
- **Graph Coloring**: Greedy, backtracking

---

## Practice Problems

### Beginner Level
1. Implement graph using adjacency list and matrix
2. Count number of vertices and edges
3. Find all neighbors of a given vertex
4. Check if graph is connected
5. Print all paths between two vertices

### Intermediate Level
1. Number of Islands (LeetCode 200)
2. Clone Graph (LeetCode 133)
3. Course Schedule (LeetCode 207)
4. Pacific Atlantic Water Flow (LeetCode 417)
5. Network Delay Time (LeetCode 743)

### Advanced Level
1. Word Ladder (LeetCode 127)
2. Minimum Spanning Tree
3. Dijkstra's Shortest Path
4. Alien Dictionary (LeetCode 269)
5. Cheapest Flights Within K Stops (LeetCode 787)

---

## Key Takeaways

1. **Choose the right representation**: Adjacency list for sparse graphs, matrix for dense graphs
2. **Most interview problems use adjacency list** due to space efficiency
3. **Master BFS and DFS first**: They're the foundation for all graph algorithms
4. **Understand directed vs undirected**: Many algorithms behave differently
5. **Practice visualization**: Draw graphs while solving problems
6. **Track visited nodes**: Essential to avoid infinite loops
7. **Time complexity matters**: Know when to use which algorithm

---

## Learning Path

```
Week 1: Graph Basics & Representation
  ├── Adjacency Matrix/List Implementation
  ├── Basic Operations (Add, Remove, Check)
  └── Graph Input/Output

Week 2: Graph Traversal
  ├── BFS (Iterative with Queue)
  ├── DFS (Recursive & Iterative)
  └── Applications (Connected Components, Path Finding)

Week 3: Shortest Path
  ├── BFS for Unweighted Graphs
  ├── Dijkstra's Algorithm
  └── Bellman-Ford

Week 4: Advanced Topics
  ├── Topological Sort
  ├── Cycle Detection
  ├── Minimum Spanning Tree
  └── Union-Find (Disjoint Set)
```

---

## Resources

- **Books**: 
  - "Introduction to Algorithms" (CLRS)
  - "Algorithms" by Robert Sedgewick
  
- **Online**:
  - LeetCode Graph Problems
  - GeeksforGeeks Graph Section
  - Visualgo.net (Graph Visualizations)

---

**Happy Learning! 🚀**

*Start with implementing basic graph structures and BFS/DFS. Everything else builds on these fundamentals!*