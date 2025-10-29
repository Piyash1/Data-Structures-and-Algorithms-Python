# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        hashmap = {}
        for i in range(n):
            remaining = target - nums[i]
            if remaining in hashmap:
                return [hashmap[remaining], i]
            hashmap[nums[i]] = i

# Example usage
sol = Solution()
nums = [2,7,11,15]
result = sol.twoSum(nums, 9)
print(result)

            

# # Brute force approach
# def twoSum(nums, target):
#     n = len(nums)
#     for i in range(n):
#         for j in range(i+1, n):
#             if nums[i] + nums[j] == target:
#                 return [i, j]

# nums = [2,7,11,15]
# result = twoSum(nums, 9)
# print(result)