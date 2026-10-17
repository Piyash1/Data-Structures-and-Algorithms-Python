# 3551. Minimum Swaps to Sort by Digit Sum

from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(num):
            total = 0

            while num > 0:
                total += num % 10
                num //= 10

            return total

        n = len(nums)

        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))

        position = {}
        for i in range(n):
            position[sorted_nums[i]] = i

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i]:
                continue

            j = i
            cycle_size = 0

            while not visited[j]:
                visited[j] = True
                j = position[nums[j]]
                cycle_size += 1

            if cycle_size > 1:
                swaps += cycle_size - 1

        return swaps


# Examle usage
if __name__ == "__main__":
    solution = Solution()
    nums = [18, 43, 34, 16]
    print(solution.minSwaps(nums))
