# Leetcode Problem 45: Jump Game II

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        left = 0
        right = 0
        
        while right < n - 1:
            farthest = 0
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
            left = right + 1
            right = farthest
            jumps += 1
        return jumps


sol = Solution()
nums = [2,3,1,1,4]
print(sol.jump(nums))


# Brute Force Approach: Exponential Time Complexity O(n^n)
# class Solution:
#     def solve(self, index, jump, last_index, nums):
#         if index >= last_index:
#             return jump

#         min_jump = float('inf')
#         for i in range(1, nums[index] + 1):
#             min_jump = min(min_jump, self.solve(index + i, jump + 1, last_index, nums))
#         return min_jump
    
#     def jump(self, nums: List[int]) -> int:
#         return self.solve(0, 0, len(nums) - 1, nums)