# 3364. Minimum Positive Sum Subarray 

from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans = float('inf')

        for i in range(len(nums)):
            total = 0

            for j in range(i, len(nums)):
                total += nums[j]
                
                length = j - i+1

                if length > r:
                    break

                if length >= l and total > 0:
                    ans = min(ans, total)

        return -1 if ans == float('inf') else ans


# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [3, -2, 1, 4]
    l = 2
    r = 3
    print(solution.minimumSumSubarray(nums, l, r))
                
