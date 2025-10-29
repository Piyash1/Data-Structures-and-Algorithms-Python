# Given an integer array nums, find the subarray with the largest sum, and return its sum.

class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        max_sum = float('-inf')
        total = 0
        for i in range(n):
            total = total + nums[i]
            max_sum = max(max_sum, total)
            if total < 0:
                total = 0
        return max_sum

# Example usage
sol = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
result = sol.maxSubArray(nums)  
print(result)



# # Brute force approach

# def maxSubArray(nums):
#     n = len(nums)
#     max_sum = float('-inf')
#     for i in range(n):
#         total = 0
#         for j in range(i, n):
#             total = total + nums[j]
#             max_sum = max(max_sum, total)
#     return max_sum

# # Example usage
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# result = maxSubArray(nums)
# print(result)