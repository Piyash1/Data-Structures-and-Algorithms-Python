#  Leetcode no.130 - Surrounded Regions

class Solution(object):
    def solve(self, board):
        rows = len(board)
        cols = len(board[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        # upper rows
        r, c = 0, 0
        for c in range(cols):
            if board[r][c] == 'O':
                if visited[r][c] == 0:
                    self.dfs(r, c, board, visited, rows, cols)
        # last rows
        r, c = rows-1, 0
        for c in range(cols):
            if board[r][c] == 'O':
                if visited[r][c] == 0:
                    self.dfs(r, c, board, visited, rows, cols)
        # first column
        r, c = 0, 0
        for r in range(rows):
            if board[r][c] == 'O':
                if visited[r][c] == 0:
                    self.dfs(r, c, board, visited, rows, cols)
        # last colum
        r, c = 0, cols -1
        for r in range(rows):
            if board[r][c] == 'O':
                if visited[r][c] == 0:
                    self.dfs(r, c, board, visited, rows, cols)


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    if visited[r][c] == 0:
                        board[r][c] = 'X'
    

    def dfs(self, r, c, board, visited, rows, cols):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if board[r][c] == 'X':
            return
        if visited[r][c] == 1:
            return
        visited[r][c] = 1

        self.dfs(r+1, c, board, visited, rows, cols)
        self.dfs(r-1, c, board, visited, rows, cols)
        self.dfs(r, c+1, board, visited, rows, cols)
        self.dfs(r, c-1, board, visited, rows, cols)

# Example usage:
if __name__ == "__main__":
    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']
    ]
    sol = Solution()
    sol.solve(board)
    for row in board:
        print(row)