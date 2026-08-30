# 2091. Removing Minimum and Maximum From Array

from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        # Find minimum and maximum values
        minimum = min(nums)
        maximum = max(nums)

        # Find their indexes
        min_index = nums.index(minimum)
        max_index = nums.index(maximum)

        # Make min_index the smaller index
        if min_index > max_index:
            min_index, max_index = max_index, min_index

        # Option 1: Remove both from front
        from_front = max_index + 1

        # Option 2: Remove both from back
        from_back = n - min_index

        # Option 3: Remove one from front and one from back
        both_sides = (min_index + 1) + (n - max_index)

        return min(from_front, from_back, both_sides)

# example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [2, 10, 7, 5, 4, 1, 8, 6]
    print(solution.minimumDeletions(nums))  # Output: 5