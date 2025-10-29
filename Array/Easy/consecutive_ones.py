# Given a binary array nums, return the maximum number of consecutive 1's in the array.

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        n = len(nums)
        count = 0
        max_count = 0
        for i in range(n):
            if nums[i] == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
        return max(max_count, count) # in case the array ends with 1s

# Example usage:
solution = Solution()
nums = [1,1,0,1,1,1]
print(solution.findMaxConsecutiveOnes(nums)) 