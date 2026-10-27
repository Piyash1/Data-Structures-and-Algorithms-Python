# 3963. Create Grid With Exactly One Path

from typing import List

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        # create grid
        grid = [["#"] * n for _ in range(m)]

        # make first row free
        grid[0] = ["."] * n

        # make last column free
        for i in range(m):
            grid[i][n-1] = "."

        # convert rows into string
        return ["".join(row) for row in grid]


# Example usage
if __name__ == "__main__":
    solution = Solution()
    m = 2
    n = 3
    print(solution.createGrid(m, n))
