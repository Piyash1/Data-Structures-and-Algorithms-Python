# 3789. Minimum Cost to Acquire Required Items

class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        common = min(need1, need2)

        # Cost of satisfying common requirements
        total_cost = common * min(costBoth, cost1 + cost2)

        # Remaining type 1 requirement
        remaining1 = need1 - common

        # Remaining type 2 requirement
        remaining2 = need2 - common

        # Buy the cheapest option for remaining units
        total_cost += remaining1 * min(cost1, costBoth)
        total_cost += remaining2 * min(cost2, costBoth)

        return total_cost


# Example usage
if __name__ == "__main__":
    solution = Solution()
    cost1 = 5
    cost2 = 4
    costBoth = 15
    need1 = 2
    need2 = 3
    print(solution.minimumCost(cost1, cost2, costBoth, need1, need2))
