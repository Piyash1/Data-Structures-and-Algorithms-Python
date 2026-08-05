# 3310. Remove Methods From Project

from collections import deque
from typing import List
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # step-1:-> build graph
        graph = [[] for _ in range(n)]

        for u, v in invocations:
            graph[u].append(v)
        
        # Step 2: BFS to find suspicious methods
        suspicious = [False] * n
        queue = deque([k])
        suspicious[k] = True

        while queue:
            node = queue.popleft()
            for neighbour in graph[node]:
                if not suspicious[neighbour]:
                    suspicious[neighbour] = True
                    queue.append(neighbour)
        
        # Step 3: Check if removal is possible
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))
        
        # Step 4: Return remaining methods
        ans = []
        for i in range(n):
            if not suspicious[i]:
                ans.append(i)
        
        return ans

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    n = 4
    k = 1
    invocations = [[1,2],[0,1],[3,2]]
    result = solution.remainingMethods(n, k, invocations)
    print("Remaining methods after removal:", result)