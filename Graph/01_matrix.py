# Leetcode no.542 - 01 Matrix

from collections import deque
class Solution(object):
    def updateMatrix(self, mat):
        rows = len(mat)
        cols = len(mat[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        distance = [[0 for _ in range(cols)] for _ in range(rows)]
        queue = deque()
        
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append([r, c, 0])
                    visited[r][c] = 1
        
        while queue:
            i, j, d = queue.popleft()
            distance[i][j] = d  
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for x, y in directions:
                new_i = i + x
                new_j = j + y
                if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                    continue
                if visited[new_i][new_j] == 1:
                    continue
                queue.append([new_i, new_j, d + 1])
                visited[new_i][new_j] = 1
        return distance

# Example usage:
if __name__ == "__main__":
    mat = [[0,0,0],[0,1,0],[1,1,1]]
    solution = Solution()
    result = solution.updateMatrix(mat)
    for row in result:
        print(row)
    