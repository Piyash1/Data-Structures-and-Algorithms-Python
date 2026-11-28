# 3947. Maximum Number of Items From Sale II

import heapq
from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        # step 1: count frequency of each factor
        freq = [0] * (n+1)
        
        for factor, price in items:
            freq[factor] += 1

        # step 2: calculate free item opportunity
        gain = [0] * (n+1)

        for factor in range(1, n+1):
            count = 0

            for multiple in range(factor, n+1, factor):
                count += freq[multiple]

            gain[factor] = count - 1

        # step 3: find cheapest item
        min_price = min(price for factor, price in items)

        # step 4: build min heap
        heap = []

        for factor, price in items:
            if gain[factor] > 0:
                heapq.heappush(heap, (price, factor, gain[factor]))

        # step 5: buy special items first
        ans = 0

        while heap and budget > 0:
            price, factor, count = heapq.heappop(heap)

            if price >= 2 * min_price:
                break

            buy = min(count, budget // price)

            ans += buy * 2
            budget -= buy * price

        # step 6: buy normal items
        ans += budget // min_price

        return ans


# Example usage
if __name__ == "__main__":
    solution = Solution()
    items = [[2, 8], [1, 10], [6, 6], [4, 12], [5, 20], [5, 17]]
    budget = 35
    print(solution.maximumSaleItems(items, budget))
