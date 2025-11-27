# Leetcode Problem 207: Course Schedule

from collections import deque
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        for u, v in prerequisites:
            adj_list[u].append(v)
            indegree[v] += 1
        
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
            return True
        return False

# Example usage:
if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    solution = Solution()
    print(solution.canFinish(numCourses, prerequisites))  # Output: False (since there is a cycle)