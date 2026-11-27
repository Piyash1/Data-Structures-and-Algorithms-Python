# 3946. Maximum Number of Items From Sale I

from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        price = [p for _, p in items]
        min_price = min(price)

        # bonus[i] = free copies we get for buying item i(first time)
        bonus = [0] * n
        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    bonus[i] += 1

        dp = [[0]*(budget+1) for _ in range(n+1)]

        # base case
        for remaining in range(budget+1):
            dp[n][remaining] = remaining // min_price

        # fill the remaining table from bottom to up
        for i in range(n-1, -1, -1):
            gained = 1 + bonus[i]

            for remaining in range(budget+1):
                
                # choice 1: skip
                skip = dp[i+1][remaining]

                # choice 2: take
                take = 0

                if price[i] <= remaining:
                    take = gained + dp[i+1][remaining-price[i]]

                dp[i][remaining] = max(skip, take)

        return dp[0][budget]


# Example usage
if __name__ == "__main__":
    solution = Solution()
    items = [[6, 2], [2, 6], [3, 4]]
    budget = 9
    print(solution.maximumSaleItems(items, budget))



# from functools import lru_cache

# def solution(items, budget):
#     n = len(items)
#     price = [p for _, p in items]
#     min_price = min(price)

#     # bonus[i] = free copies we get for buying item i(first time)
#     bonus = [0] * n
#     for i in range(n):
#         for j in range(n):
#             if i != j and items[j][0] % items[i][0] == 0:
#                 bonus[i] += 1

#     @lru_cache(None)
#     def solve(i, remaining):
#         # base case: all items decided, spend the rest on cheapest item
#         if i == n:
#             return remaining // min_price

#         # choice 1--> skip item i 
#         skip = solve(i+1, remaining)

#         # choice 2--> take item i(only if we can afford it)
#         take = 0
#         if price[i] <= remaining:
#             gained = 1 + bonus[i]
#             take =  gained + solve(i+1, remaining-price[i])
        
#         return max(skip, take)

#     return solve(0, budget)



# items = [[6, 2], [2, 6], [3, 4]]
# budget = 9
# print(solution(items, budget))
