# 2996. Smallest Missing Integer Greater Than Sequential Prefix Sum

from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        sequential_sum = nums[0]

        for i in range(1 , len(nums)):
            if nums[i] == nums[i-1] + 1:
                sequential_sum += nums[i]
            else:
                break

        numset = set(nums)
        while sequential_sum in numset:
            sequential_sum += 1

        return sequential_sum



# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3,2,5]
    print(solution.missingInteger(nums))  # Answer: 6