# 2567. Minimum Score by Changing Two Elements

from typing import List

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()

        n = len(nums)

        # change two smallest num
        case1 = nums[n-1] - nums[2]

        # change 1 smallest + 1 largest
        case2 = nums[n-2] - nums[1]

        # change two largest
        case3 = nums[n-3] - nums[0]

        return min(case1, case2, case3)


# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 4, 7, 8, 5]
    print(solution.minimizeSum(nums))
