# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        # Transpose the matrix
        for i in range(n-1):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # Reverse each row
        for i in range(n):
            matrix[i].reverse()
        return matrix

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    sol.rotate(matrix)
    print(matrix)  

# # Brute Force Approach
# def rotate(matrix: list[list[int]]) -> None:
#     n = len(matrix)
#     result = [[0 for _ in range(n)] for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             result[j][n - 1 - i] = matrix[i][j]
#     return result

# # Example usage of brute force approach:
# if __name__ == "__main__":
#     matrix = [[1,2,3],[4,5,6],[7,8,9]]
#     rotated_matrix = rotate(matrix)
#     print(rotated_matrix)
    