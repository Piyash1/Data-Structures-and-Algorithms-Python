# Leetcode no.733 - Flood Fill

from copy import deepcopy
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        if image[sr][sc] == color:
            return image
        image_copy = deepcopy(image)
        rows = len(image)
        cols = len(image[0])
        initial_color = image[sr][sc]
        
        self.dfs(sr, sc, color, initial_color, image_copy, rows, cols)
        return image_copy
    
    def dfs(self, i, j, new_color, initial_color, image_copy, rows, cols):
        if i < 0 or i >= rows or j < 0 or j >= cols:
            return
        if image_copy[i][j] != initial_color:
            return
        if image_copy[i][j] == new_color:
            return
        image_copy[i][j] = new_color
        
        self.dfs(i + 1, j, new_color, initial_color, image_copy, rows, cols)
        self.dfs(i, j + 1, new_color, initial_color, image_copy, rows, cols)
        self.dfs(i - 1, j, new_color, initial_color, image_copy, rows, cols)
        self.dfs(i, j - 1, new_color, initial_color, image_copy, rows, cols)

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    color = 2
    result = solution.floodFill(image, sr, sc, color)
    print(result)  # Output: [[2,2,2],[2,2,0],[2,0,1]]


# Breadth-First Search (BFS) Approach
from collections import deque
def floodFillBFS(image, sr, sc, color):
    if image[sr][sc] == color:
        return image
    image_copy = deepcopy(image)
    rows = len(image_copy)
    cols = len(image_copy[0])
    initial_color = image_copy[sr][sc]
    queue = deque()
    queue.append((sr, sc))
    
    while len(queue) != 0:
        i, j = queue.popleft()
        image_copy[i][j] = color
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        for x , y in directions:
            new_i = i + x
            new_j = j + y
            if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                continue
            if image_copy[new_i][new_j] != initial_color:
                continue
            queue.append((new_i, new_j))
    return image_copy