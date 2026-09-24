# 3550. Smallest Index With Digit Sum Equal to Index

from typing import List
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            num = nums[i]
            digit_sum = 0

            while num > 0:
                digit = num % 10
                digit_sum += digit
                num //= 10

            if digit_sum == i:
                return i

        return -1


# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums = [1,3,2]
    print(solution.smallestIndex(nums))
