# 70. Climbing Stairs
# Optimized Tabulation Approach (Bottom-Up Dynamic Programming with O(1) space)
class Solution:        
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        prev2 = 1  # Ways to reach step 0
        prev = 1   # Ways to reach step 1
        
        for i in range(2, n + 1):
            curr = prev + prev2  # Ways to reach step i
            prev2 = prev         # Slide window: ways to reach step i-2
            prev = curr          # Slide window: ways to reach step i-1
        return prev  # prev now contains ways to reach step n


sol = Solution()
print(sol.climbStairs(3))

# Tabulation Approach (Bottom-Up Dynamic Programming)
# class Solution:        
#     def climbStairs(self, n: int) -> int:
#         dp = [-1] * (n + 1)
#         dp[0] = 1  # 1 way to stay at the ground (do nothing)
#         dp[1] = 1  # 1 way to reach the first step
        
#         for i in range(2, n + 1):
#             dp[i] = dp[i - 1] + dp[i - 2]  # Ways to reach step i
#         return dp[n]

# Memoization Approach (Top-Down Dynamic Programming)

# class Solution:
#     def solve(self, n, dp):
#         # Base cases
#         if n <= 1:
#             return 1
#         # Check if already computed (memoized)
#         if dp[n] != -1:
#             return dp[n]
        
#         dp[n] = self.solve(n - 1, dp) + self.solve(n - 2, dp)
#         return dp[n]
        
#     def climbStairs(self, n: int) -> int:
#         dp = [-1] * (n + 1)
#         return self.solve(n, dp)

# Recursion Approach

# class Solution:
#     def solve(self, n):
#         # Base cases
#         if n <= 1:
#             return 1
        
#         # Recursive calls for the two possible steps
#         return self.solve(n - 1) + self.solve(n - 2)
#     def climbStairs(self, n: int) -> int:
#         return self.solve(n)