# Leetcode no.62 Unique Paths

#Memorization Approach
class Solution:
  def solve(self, i, j, dp):
    if i == 0 and j == 0:
      return 1
    if i < 0 or j < 0:
      return 0
    
    if dp[i][j] != -1:
      return dp[i][j]
    
    up = self.solve(i-1, j, dp)
    left = self.solve(i, j-1, dp)
    
    dp[i][j] = up+left
    return dp[i][j]
  
  def uniquePaths(self, m: int, n: int) -> int:
    dp = [[-1 for _ in range(n)] for _ in range(m)]
    return self.solve(m-1, n-1, dp)


sol = Solution()
m = 3
n = 7
print(sol.uniquePaths(m, n))


#Memorization Approach
# class Solution:
#   def solve(self, i, j, dp):
#     if i == 0 and j == 0:
#       return 1
#     if i < 0 or j < 0:
#       return 0
    
#     if dp[i][j] != -1:
#       return dp[i][j]
    
#     up = self.solve(i-1, j, dp)
#     left = self.solve(i, j-1, dp)
    
#     dp[i][j] = up+left
#     return dp[i][j]
  
#   def uniquePaths(self, m: int, n: int) -> int:
#     dp = [[-1 for _ in range(n)] for _ in range(m)]
#     return self.solve(m-1, n-1, dp)

# Brute Force Recursion Approach
#Memorization Approach
# class Solution:
#   def solve(self, i, j, dp):
#     if i == 0 and j == 0:
#       return 1
#     if i < 0 or j < 0:
#       return 0

#     up = self.solve(i-1, j, dp)
#     left = self.solve(i, j-1, dp)
    
#     return up+left
  
#   def uniquePaths(self, m: int, n: int) -> int:
#     return self.solve(m-1, n-1)