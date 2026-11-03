# 3736. Minimum Moves to Equal Array Elements III

from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maximum = max(nums)

        moves = 0

        for num in nums:
            moves += maximum - num

        return moves

# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [2, 1, 3]
    print(solution.minMoves(nums))
