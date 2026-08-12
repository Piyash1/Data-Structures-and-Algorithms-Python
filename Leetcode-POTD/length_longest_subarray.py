# 2958. Length of Longest Subarray With at Most K Frequency

from typing import List
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = {}
        left = 0
        ans = 0

        for right in range(n):
            # Add nums[right] to the frequency map
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            # Window is invalid
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1

            # Window is valid, update the answer
            ans = max(ans, right - left + 1)

        return ans

# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3,1,2,3,1,2]
    k = 2
    print(solution.maxSubarrayLength(nums, k))  # Output: 6