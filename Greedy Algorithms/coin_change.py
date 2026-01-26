# Minimum number of coins

class Solution:
    def findMin(self, n):
        coins = [1, 2, 5, 10]
        count = 0
       
        for i in range(len(coins)-1, -1, -1):
            while n >= coins[i]:
                n -= coins[i]
                count += 1
        return count
       

sol = Solution()
n = 39
print(sol.findMin(n))