# 3471. Find the Largest Almost Missing Integer

from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        subarray_count = {}
        n = len(nums)

        for i in range(n-k+1):
            subarray = nums[i:i+k]
            seen = set(subarray)
            for num in seen:
                subarray_count[num] = subarray_count.get(num, 0) + 1

        candidate = []
        for num, count in subarray_count.items():
            if count == 1:
                candidate.append(num)

        if len(candidate) == 0:
            return -1
        else:
            return max(candidate)

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    k = 3
    result = solution.largestInteger(nums, k)
    print(result)  # Output: 5