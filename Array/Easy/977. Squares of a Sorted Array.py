# 977. Squares of a Sorted Array

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        n = len(nums)

        result = [0] * n

        left = 0
        right = n - 1

        # Fill the result from right to left
        for i in range(n - 1, -1, -1):

            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]

            if left_square > right_square:
                result[i] = left_square
                left += 1
            else:
                result[i] = right_square
                right -= 1

        return result


# Example usage
if __name__ == "__main__":
    solution = Solution()

    nums = [-4, -1, 0, 3, 10]

    print(solution.sortedSquares(nums))  # Answer: [0, 1, 9, 16, 100]