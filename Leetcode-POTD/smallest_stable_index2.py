# 3904. Smallest Stable Index II

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        suffix_min = [0] * n
        suffix_min[n-1] = nums[n-1]

        for i in range(n-2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i+1])
        
        prefix_max = nums[0]
        for i in range(n):
            prefix_max = max(prefix_max, nums[i])

            if prefix_max - suffix_min[i] <= k:
                return i
        return -1


# example usage:
if __name__ == "__main__":
    solution = Solution()
    nums = [5,0,1,4]
    k = 3
    result = solution.firstStableIndex(nums, k)
    print(result)  # Output: 3