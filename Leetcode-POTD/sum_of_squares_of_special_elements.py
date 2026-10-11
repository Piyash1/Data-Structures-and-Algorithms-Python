# 2778. Sum of Squares of Special Elements 

from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0

        for i in range(1, n+1):
            if n % i == 0:
                result += nums[i-1] * nums[i-1]
        
        return result


# Example usage
if __name__ == "__main__":
    solution = Solution()

    nums = [1, 2, 3, 4]
    print(solution.sumOfSquares(nums))