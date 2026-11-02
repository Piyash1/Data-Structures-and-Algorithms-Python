# 462. Minimum Moves to Equal Array Elements II

from typing import List

class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()

        median = nums[len(nums)//2]

        moves = 0
        for num in nums:
            moves += abs(num-median)
        
        return moves


# Example usage
if __name__ == "__main__":
  solution = Solution()
  nums = [1, 2, 3]
  print(solution.minMoves2(nums))
