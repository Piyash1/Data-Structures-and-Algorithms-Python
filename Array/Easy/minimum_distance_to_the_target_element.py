# 1848. Minimum Distance to the Target Element

from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        result = len(nums)

        for i in range(len(nums)):
            if nums[i] == target:
                result = min(result, abs(i - start))
        
        return result

# example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    target = 5
    start = 3
    print(solution.getMinDistance(nums, target, start))  # Output: 1