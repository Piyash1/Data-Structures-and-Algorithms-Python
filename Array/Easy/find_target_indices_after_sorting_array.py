# 2089. Find Target Indices After Sorting Array

from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        nums.sort()

        result = []

        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)

        return result


# Example usage
if __name__ == "__main__":
    solution = Solution()

    nums = [1, 2, 5, 2, 3]
    target = 2

    print(solution.targetIndices(nums, target))  # Answer: [1, 2]