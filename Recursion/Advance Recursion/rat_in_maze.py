# https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1

class Solution:
    def ratInMaze(self, maze):
        n = len(maze)
        result = []
        visited = [[0 for _ in range(n)] for _ in range(n)]
        if maze[0][0] == 1:
            self.findPath(0, 0, maze, n, '', result, visited)
        return result
    
    
    def findPath(self, i, j, maze, n, path, result, visited):
        if i == n - 1 and j == n - 1:
            result.append(path)
            return
        
        # Down
        if i + 1 < n and maze[i + 1][j] == 1 and visited[i + 1][j] == 0:
            visited[i][j] = 1
            self.findPath(i + 1, j, maze, n, path + 'D', result, visited)
            visited[i][j] = 0
        
        # Left
        if j - 1 >= 0 and maze[i][j - 1] == 1 and visited[i][j - 1] == 0:
            visited[i][j] = 1
            self.findPath(i, j - 1, maze, n, path + 'L', result, visited)
            visited[i][j] = 0
        
        # Right
        if j + 1 < n and maze[i][j + 1] == 1 and visited[i][j + 1] == 0:
            visited[i][j] = 1
            self.findPath(i, j + 1, maze, n, path + 'R', result, visited)
            visited[i][j] = 0
        
        # Up
        if i - 1 >= 0 and maze[i - 1][j] == 1 and visited[i - 1][j] == 0:
            visited[i][j] = 1
            self.findPath(i - 1, j, maze, n, path + 'U', result, visited)
            visited[i][j] = 0
            
# Example usage:
if __name__ == "__main__":
    maze = [[1, 0, 0, 0],
            [1, 1, 0, 1],
            [1, 1, 0, 0],
            [0, 1, 1, 1]]
    sol = Solution()
    paths = sol.ratInMaze(maze)
    print(paths)