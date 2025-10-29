# You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

# You should return the array of nums such that the the array follows the given conditions:

# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in nums is preserved.
# The rearranged array begins with a positive integer.
# Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

class Solution:
    def rearrangeArray(self, nums):
        positive_index = 0
        negative_index = 1
        rearranged = [0] * len(nums)
        for num in nums:
            if num > 0:
                rearranged[positive_index] = num
                positive_index += 2
            else:
                rearranged[negative_index] = num
                negative_index += 2
        return rearranged

# Example usage:
solution = Solution()
nums = [3, 1, -2, -5, 2, -4]
result = solution.rearrangeArray(nums)
print(result)


# # Brute Force Approach: 
# def rearrangeArray(nums):
#     positive_nums = []
#     negative_nums = []
    
#     # Separate positive and negative numbers
#     for num in nums:
#         if num > 0:
#             positive_nums.append(num)
#         else:
#             negative_nums.append(num)
    
#     rearranged = []
    
#     # Interleave positive and negative numbers
#     for i in range(len(positive_nums)):
#         rearranged.append(positive_nums[i])
#         rearranged.append(negative_nums[i])
    
#     return rearranged

# # Example usage:
# nums = [3, 1, -2, -5, 2, -4]
# result = rearrangeArray(nums)
# print(result) 