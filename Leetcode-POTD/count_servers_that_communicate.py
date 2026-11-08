# 1267. Count Servers that Communicate

class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        rows_count = [0] * rows
        cols_count = [0] * cols

        # count all the servers in rows and cols
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    rows_count[r] += 1
                    cols_count[c] += 1

        # count servers that can communicate
        result = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    if rows_count[r] > 1 or cols_count[c] > 1:
                        result += 1
        
        return result


# Example usage
if __name__ == "__main__":
    solution = Solution()
    grid = [[1,0],[1,1]]
    print(solution.countServers(grid))
