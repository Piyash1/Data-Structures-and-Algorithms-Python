# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        rowstrack = [0 for _ in range(rows)]
        colstrack = [0 for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rowstrack[i] = -1
                    colstrack[j] = -1
        for i in range(rows):
            for j in range(cols):
                if rowstrack[i] == -1 or colstrack[j] == -1:
                    matrix[i][j] = 0
        return matrix

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    sol.setZeroes(matrix)
    print(matrix)  
    
# # Brute Force Approach
# def markInfinity(matrix: list[list[int]], row: int, col: int) -> None:
#     rows = len(matrix)
#     cols = len(matrix[0])
#     for j in range(cols):
#         if matrix[row][j] != 0:
#             matrix[row][j] = float('inf')
#     for i in range(rows):
#         if matrix[i][col] != 0:
#             matrix[i][col] = float('inf')

# def setZeroes(matrix: list[list[int]]) -> None:
#     rows = len(matrix)
#     cols = len(matrix[0])
#     for i in range(rows):
#         for j in range(cols):
#             if matrix[i][j] == 0:
#                 markInfinity(matrix, i, j)
#     for i in range(rows):
#         for j in range(cols):
#             if matrix[i][j] == float('inf'):
#                 matrix[i][j] = 0
#     return matrix

# # Example usage of brute force approach:
# if __name__ == "__main__":
#     matrix = [[1,1,1],[1,0,1],[1,1,1]]
#     setZeroes(matrix)
#     print(matrix)