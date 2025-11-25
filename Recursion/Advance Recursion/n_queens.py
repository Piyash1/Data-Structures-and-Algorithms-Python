# Leetcode no. 51: N-Queens Problem

from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [['.'] * n for _ in range(n)]
        cols = [0] * n
        diag1 = [0] * (2 * n - 1)  # row + col
        diag2 = [0] * (2 * n - 1)  # row - col + (n - 1)
        
        def backtrack(row):
            if row == n:
                result.append([''.join(r) for r in board])
                return
            for col in range(n):
                if cols[col] == 0 and diag1[row + col] == 0 and diag2[row - col + n - 1] == 0:
                    board[row][col] = 'Q'
                    cols[col] = 1
                    diag1[row + col] = 1
                    diag2[row - col + n - 1] = 1
                    
                    backtrack(row + 1)
                    
                    board[row][col] = '.'
                    cols[col] = 0
                    diag1[row + col] = 0
                    diag2[row - col + n - 1] = 0
        backtrack(0)
        return result

# Example usage:
if __name__ == "__main__":
    n = 4
    sol = Solution()
    solutions = sol.solveNQueens(n)
    print(solutions)