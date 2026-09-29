from functools import cache
from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])

        @cache
        def dfs(row, col, balance):
            # Outside the grid
            if row >= rows or col >= cols:
                return False

            # Update balance using current cell
            if grid[row][col] == '(':
                balance += 1
            else:
                balance -= 1

            # Too many closing brackets
            if balance < 0:
                return False

            # Reached destination
            if row == rows - 1 and col == cols - 1:
                return balance == 0

            # Try moving down or right
            return (
                dfs(row + 1, col, balance)
                or
                dfs(row, col + 1, balance)
            )

        return dfs(0, 0, 0)


#Example usage
if __name__ == "__main__":
    solution = Solution()
    grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
    print(solution.hasValidPath(grid))
