# 453. Minimum Moves to Equal Array Elements

from typing import List

class Solution:
    def minMoves(self, nums: list[int]) -> int:
        minimum = min(nums)

        moves = 0
        for num in nums:
            moves += num - minimum
        
        return moves


# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3]
    print(solution.minMoves(nums))
