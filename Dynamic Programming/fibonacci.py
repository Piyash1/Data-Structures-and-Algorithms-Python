# Space-Optimized Tabulation (Optimal Approach)

class Solution:
    def nthFibonacci(self, n: int) -> int:
        # Handle base cases
        if n <= 1:
            return n
        
        # Initialize the first two Fibonacci numbers
        prev2 = 0  # F(0)
        prev = 1   # F(1)
        
        # Compute from F(2) to F(n)
        for i in range(2, n + 1):
            curr = prev + prev2  # F(i) = F(i-1) + F(i-2)
            prev2 = prev         # Slide window: F(i-2) becomes F(i-1)
            prev = curr          # Slide window: F(i-1) becomes F(i)
        
        return prev  # prev now contains F(n)

sol = Solution()
print(sol.nthFibonacci(8))

# Tabulation Approach (Bottom-Up Dynamic Programming)

# class Solution:
#     def nthFibonacci(self, n: int) -> int:
#         # Handle base cases
#         if n <= 1:
#             return n
        
#         # Initialize DP array
#         dp = [0] * (n + 1)
#         dp[0] = 0  # F(0) = 0
#         dp[1] = 1  # F(1) = 1
        
#         # Fill array bottom-up
#         for i in range(2, n + 1):
#             dp[i] = dp[i - 1] + dp[i - 2]  # F(i) = F(i-1) + F(i-2)
        
#         return dp[n]

        


# Memoization Approach (Top-Down Dynamic Programming)

# class Solution:
#     def fib(self, num, dp):
#         # Base cases: F(0) = 0, F(1) = 1
#         if num <= 1:
#             return num
        
#         # Check if already computed (memoized)
#         if dp[num] != -1:
#             return dp[num]  # Return cached result
        
#         # Compute and store in cache
#         dp[num] = self.fib(num - 1, dp) + self.fib(num - 2, dp)
#         return dp[num]

#     def nthFibonacci(self, n: int) -> int:
#         # Initialize memoization array with -1 (uncomputed)
#         dp = [-1] * (n + 1)
#         return self.fib(n, dp)




# Brute Force Approach (Pure Recursion)

# class Solution:
#     def nthFibonacci(self, n: int) -> int:
#         if n <= 1:
#             return n
#         return self.nthFibonacci(n-1) + self.nthFibonacci(n-2)


