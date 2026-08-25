# 3718. Smallest Missing Multiple of K

from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:

        num_set = set(nums)

        multiple = k

        while multiple in num_set:
            multiple += k

        return multiple


# Example usage
if __name__ == "__main__":
    solution = Solution()

    nums = [8, 2, 3, 4, 6]
    k = 2

    print(solution.missingMultiple(nums, k))  # Answer: 10