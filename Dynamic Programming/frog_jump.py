# Given an integer array height[] where height[i] represents the height of the i-th stair, a frog starts from the first stair and wants to reach the last stair. From any stair i, the frog has two options: it can either jump to the (i+1)th stair or the (i+2)th stair. The cost of a jump is the absolute difference in height between the two stairs. Determine the minimum total cost required for the frog to reach the last stair.

# Optimized Tabulation Approach
class Solution:
    def minCost(self, height):
        n = len(height)
        prev2 = 0  # Cost to reach stair 0
        prev = 0   # Cost to reach stair 1
        
        for i in range(1, n):
            jump1 = prev + abs(height[i] - height[i - 1])
            
            if i > 1:
                jump2 = prev2 + abs(height[i] - height[i - 2])
            else:
                jump2 = float('inf')
                
            curr = min(jump1, jump2)
            prev2 = prev  # Slide window: cost to reach stair i-2
            prev = curr   # Slide window: cost to reach stair i-1
        return prev  # prev now contains cost to reach the last stair

sol = Solution()
heights = [20, 30, 40, 20]
print(sol.minCost(heights))

# Tabulation Approach
# class Solution:
#     def minCost(self, height):
#         dp = [-1] * len(height)
#         dp[0] = 0  # Cost to reach the first stair is 0
        
#         for i in range(1, len(height)):
#             jump1 = dp[i - 1] + abs(height[i] - height[i - 1])
            
#             if i > 1:
#                 jump2 = dp[i - 2] + abs(height[i] - height[i - 2])
#             else:
#                 jump2 = float('inf')
                
#             dp[i] = min(jump1, jump2)
#         return dp[-1]


# Memoization Approach
# class Solution:
#     def solve(self, index, height, dp):
#         if index == 0:
#             return 0
#         if dp[index] != -1:
#             return dp[index]
        
#         jump1 = self.solve(index - 1, height, dp) + abs(height[index] - height[index - 1])
        
#         if index > 1:
#             jump2 = self.solve(index - 2, height, dp) + abs(height[index] - height[index - 2])
#         else:
#             jump2 = float('inf')
            
#         dp[index] = min(jump1, jump2)
#         return dp[index]  
    
#     def minCost(self, height):
#         n = len(height)
#         dp = [-1] * n
#         return self.solve(n - 1, height, dp)


# Brute Force Recursion Approach
# class Solution:
#     def solve(self, index, height):
#         if index == 0:
#             return 0
        
#         jump1 = self.solve(index - 1, height) + abs(height[index] - height[index - 1])
        
#         if index > 1:
#             jump2 = self.solve(index - 2, height) + abs(height[index] - height[index - 2])
#         else:
#             jump2 = float('inf')
            
#         return min(jump1, jump2)
    
#     def minCost(self, height):
#         n = len(height)
#         return self.solve(n - 1, height)