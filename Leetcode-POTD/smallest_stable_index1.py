# 3903. Smallest Stable Index I

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        for i in range(n):
            left_max = max(nums[0:i+1])
            right_min = min(nums[i:n])

            score = left_max - right_min

            if score <= k:
                return i
        
        return -1

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums = [5,0,1,4]
    k = 3
    result = solution.firstStableIndex(nums, k)
    print(result)  # Output: 3