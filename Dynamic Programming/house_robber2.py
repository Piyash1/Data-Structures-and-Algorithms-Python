# Leetcode no.213 - House Robber II

from typing import List

# Optimized Tabulation Approach
class Solution:
    def solve(self, nums: List[int]) -> int:
        n = len(nums)
        prev = nums[0]
        prev2 = 0
        
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
    
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        ans = self.solve(nums[0:n-1])  # Exclude last house
        ans2 = self.solve(nums[1:n])    # Exclude first house
        return max(ans, ans2)
        


sol = Solution()
nums = [1,2,3,1]
print(sol.rob(nums))


# Tabulation Approach
# class Solution:
#     def solve(self, nums: List[int]) -> int:
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
    
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n == 1:
#             return nums[0]
#         ans = self.solve(nums[0:n-1])  # Exclude last house
#         ans2 = self.solve(nums[1:n])    # Exclude first house
#         return max(ans, ans2)


# Memorization Approach
# class Solution:
#     def solve(self, index, nums, dp):
#         if index == 0:
#             return nums[0]
#         if index == -1:
#             return 0
#         if dp[index] != -1:
#             return dp[index]
        
#         pick = nums[index] + self.solve(index - 2, nums, dp)
#         not_pick = 0 + self.solve(index - 1, nums, dp)
#         dp[index] =  max(pick, not_pick)
#         return dp[index]
    
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n == 1:
#             return nums[0]
#         dp = [-1] * (n-1)
        
#         ans1 = self.solve(n-2, nums[0:n-1], dp)  # Exclude last house
        
#         dp = [-1] * (n-1)
#         ans2 = self.solve(n-2, nums[1:n], dp)    # Exclude
#         return max(ans1, ans2)


# Brute Force Approach
# class Solution:
#     def solve(self, index, nums):
#         if index == 0:
#             return nums[0]
#         if index == -1:
#             return 0
        
#         pick = nums[index] + self.solve(index - 2, nums)
#         not_pick = 0 + self.solve(index - 1, nums)
#         return max(pick, not_pick)
    
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n == 1:
#             return nums[0]
#         ans1 = self.solve(n-2, nums[0:n-1])  # Exclude last house
#         ans2 = self.solve(n-2, nums[1:n])    # Exclude
#         return max(ans1, ans2)
        