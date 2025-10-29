# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        min_price = float('inf')
        max_profit = 0
        for i in range(n):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit
    
# Example usage
sol = Solution()
prices = [7,1,5,3,6,4]
result = sol.maxProfit(prices)  
print(result) 


# # Brute force approach
# def maxProfit(prices):
#     n = len(prices)
#     max_profit = 0
#     for i in range(n):
#         for j in range(i+1, n):
#             profit = prices[j] - prices[i]
#             max_profit = max(max_profit, profit)
#     return max_profit

# # Example usage
# prices = [7,1,5,3,6,4]
# result = maxProfit(prices)
# print(result)
    