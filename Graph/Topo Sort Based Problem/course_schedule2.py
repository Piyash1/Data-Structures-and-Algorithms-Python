# Leetcode Problem 210: Course Schedule II

from collections import deque
from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        for u, v in prerequisites:
            adj_list[v].append(u)
            indegree[u] += 1
        
        queue = deque()
        result = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            curr_node = queue.popleft()
            result.append(curr_node)
            for adj_node in adj_list[curr_node]:
                indegree[adj_node] -= 1
                if indegree[adj_node] == 0:
                    queue.append(adj_node)
        if len(result) == numCourses:
            return result
        return []

# Example usage:
if __name__ == "__main__":
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    solution = Solution()
    print(solution.findOrder(numCourses, prerequisites))  # Output: [0,1,2,3] or [0,2,1,3]
        