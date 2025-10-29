# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

# Example usage:
solution = Solution()
nums = [3, 0, 1]
print(solution.missingNumber(nums))

# # Better Approach
# def missing_number(nums):
#     n = len(nums)
#     my_dict = {}
#     for i in range(n + 1):
#         my_dict[i] = 0
#     for num in nums:
#         my_dict[num] += 1
#     for key in my_dict:
#         if my_dict[key] == 0:
#             return key
#     return -1  # This line should never be reached if input is valid

# nums = [3, 0, 1]
# print(missing_number(nums))  # Output: 2

# # Brute Force Approach
# def missing_number(nums):
#     n = len(nums)
#     for number in range(n + 1):
#         if number not in nums:
#             return number
#     return -1  # This line should never be reached if input is valid

# nums = [3, 0, 1]
# print(missing_number(nums))  # Output: 2