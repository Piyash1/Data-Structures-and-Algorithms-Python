# 3978. Unique Middle Element

class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        mid_val = nums[len(nums) // 2]
        return nums.count(mid_val) == 1

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4, 5]
    is_unique = solution.isMiddleElementUnique(nums)
    print(is_unique)  # Output: True