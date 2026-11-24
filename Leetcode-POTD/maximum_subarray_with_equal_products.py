# 3411. Maximum Subarray With Equal Products

import math
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            product = 1
            gcd = 0
            lcm = 1

            for j in range(i, n):
                product *= nums[j]
                gcd = math.gcd(gcd, nums[j])
                lcm = math.lcm(lcm, nums[j])

                if product == lcm * gcd:
                    length = j-i+1
                    ans = max(ans, length)
        
        return ans

# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 1, 2, 1, 1, 1]
    print(solution.maxLength(nums))
