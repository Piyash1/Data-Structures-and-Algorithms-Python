# Leetcode no.198 - House Robber

from typing import List

# Optimized Tabulation Approach
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        prev2 = 0
        prev = nums[0]
        
        for index in range(1, n):
            if index > 1:
                pick = nums[index] + prev2
            else:
                pick = nums[index]

            not_pick = 0 + prev
            curr = max(pick, not_pick)
            prev2 = prev
            prev = curr
        
        return prev
    

sol = Solution()
nums = [2,7,9,3,1]
print(sol.rob(nums))

# Tabulation Approach
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = [-1] * n
        
#         dp[0] = nums[0]
        
#         for index in range(1, n):
#             if index > 1:
#                 pick = nums[index] + dp[index - 2]
#             else:
#                 pick = nums[index]

#             not_pick = 0 + dp[index - 1]
#             dp[index] = max(pick, not_pick)
        
#         return dp[n-1]

# Memorization Approach
# class Solution:
#     def solve(self, index, nums, dp):
#         if index == 0:
#             return nums[0]
#         if index == -1:
#             return 0
        
#         if dp[index] != -1:
#             return dp[index]
        
#         pick = nums[index] + self.solve(index-2, nums, dp)
#         not_pick = 0 + self.solve(index-1, nums, dp)
        
#         dp[index] = max(pick, not_pick)
#         return dp[index]
    
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = [-1] * n
#         return self.solve(n-1, nums, dp)
    


# Brute Force Approach
# class Solution:
#     def solve(self, index, nums):
#         if index == 0:
#             return nums[0]
#         if index == -1:
#             return 0
        
#         pick = nums[index] + self.solve(index-2, nums)
#         not_pick = 0 + self.solve(index-1, nums)
        
#         return max(pick, not_pick)
    
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         return self.solve(n-1, nums)