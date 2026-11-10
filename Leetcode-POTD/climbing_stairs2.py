# 3693. Climbing Stairs II

from typing import List

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        prev1 = 0
        prev2 = 0
        prev3 = 0

        for i in range(1, n + 1):

            min_cost = float('inf')

            if i - 1 >= 0:
                cost = prev1 + costs[i - 1] + 1
                min_cost = min(min_cost, cost)

            if i - 2 >= 0:
                cost = prev2 + costs[i - 1] + 4
                min_cost = min(min_cost, cost)

            if i - 3 >= 0:
                cost = prev3 + costs[i - 1] + 9
                min_cost = min(min_cost, cost)

            prev3 = prev2
            prev2 = prev1
            prev1 = min_cost

        return prev1


# Example usage
if __name__ == "__main__":
    solution = Solution()
    n = 4
    costs = [1,2,3,4]
    print(solution.climbStairs(n, costs))
