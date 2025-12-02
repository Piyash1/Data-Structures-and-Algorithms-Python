import heapq
import sys


def shortest_path(n, m, edges):
    # 1. Build undirected adjacency list
    adj_list = [[] for _ in range(n + 1)]
    for u, v, wt in edges:
        adj_list[u].append([v, wt])
        adj_list[v].append([u, wt])

    # 2. Dijkstra initialisation
    distance = [sys.maxsize] * (n + 1)
    distance[1] = 0                          # source vertex

    parent = [i for i in range(n + 1)]       # parent[i] = predecessor of i

    pq = []                                  # min-heap of (dist, node)
    heapq.heappush(pq, (0, 1))

    # 3. Main loop
    while pq:
        dist, node = heapq.heappop(pq)

        if dist != distance[node]:           # ignore stale heap entries
            continue

        for adjNode, wt in adj_list[node]:
            new_dist = dist + wt
            if new_dist < distance[adjNode]:  # relaxation succeeds
                distance[adjNode] = new_dist
                heapq.heappush(pq, (new_dist, adjNode))
                parent[adjNode] = node        # record the path

    # 4. Reconstruct path or report unreachable
    if distance[n] == sys.maxsize:
        return [-1]

    path = []
    node = n
    while parent[node] != node:              # follow parents back to 1
        path.append(node)
        node = parent[node]
    path.append(1)
    path.reverse()
    return path


# ----- demo run -----
n = 5
m = 6
edges = [
    [1, 2, 2], [2, 5, 5],
    [2, 3, 4], [1, 4, 1],
    [4, 3, 3], [3, 5, 1]
]
print(shortest_path(n, m, edges))            # ➜ [1, 4, 3, 5]