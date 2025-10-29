# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        
        num_set = set(nums)
        longest_streak = 0
        
        for num in num_set:
            if num - 1 not in num_set:  # Check if it's the start of a sequence
                current_num = num
                current_streak = 1
                
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak

# Example usage:
solution = Solution()
nums = [100, 4, 200, 1, 3, 2]
result = solution.longestConsecutive(nums)
print(result)  # Output: 4 (The longest consecutive elements sequence is [1, 2, 3, 4])


# # Brute Force Approach:
# def longestConsecutive(nums):
#     longest_streak = 0
#     n = len(nums)
#     for i in range(n):
#         num = nums[i]
#         current_streak = 1
#         while num + 1 in nums:
#             num += 1
#             current_streak += 1
#         longest_streak = max(longest_streak, current_streak)
#     return longest_streak
# # Example usage:
# nums = [100, 4, 200, 1, 3, 2]
# result = longestConsecutive(nums)
# print(result)  # Output: 4 (The longest consecutive elements sequence is [1, 2, 3, 4])

# # Better Approach:
# def longestSuccessiveElements(arr):
#     arr.sort()  # Sort the array so consecutive numbers are next to each other
#     last_smaller = float("-inf")  # To keep track of the previous number
#     count = 0  # Current consecutive sequence length
#     longest = 0  # Longest sequence found

#     for num in arr:
#         if num - 1 == last_smaller:  # Check if current is consecutive
#             count += 1
#             last_smaller = num
#         elif num != last_smaller:  # Skip duplicates
#             count = 1
#             last_smaller = num
#         longest = max(longest, count)  # Update the answer

#     return longest
# # Example usage:
# arr = [100, 4, 200, 1, 3, 2]
# result = longestSuccessiveElements(arr)
# print(result)  # Output: 4 (The longest consecutive elements sequence is [1, 2, 3, 4])