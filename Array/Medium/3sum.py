# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return result
    
# Example usage:
solution = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(solution.threeSum(nums))


# # Brute Force Approach (for reference, not efficient):

# def threeSum(nums: list[int]) -> list[list[int]]:
#     result = set()
#     n = len(nums)
#     for i in range(n):
#         for j in range(i + 1, n):
#             for k in range(j + 1, n):
#                 if nums[i] + nums[j] + nums[k] == 0:
#                     triplet = [nums[i], nums[j], nums[k]]
#                     triplet.sort()
#                     result.add(tuple(triplet))
#     return [list(triplet) for triplet in result]

# # Example usage of brute force approach:
# nums = [-1, 0, 1, 2, -1, -4]
# print(threeSum(nums))

# # Better Approach Using Hashing (for reference):

# def threeSumHashing(nums: list[int]) -> list[list[int]]:
#     n = len(nums)
#     result = set()
#     for i in range(n):
#         myset = set()
#         for j in range(i + 1, n):
#             third = -(nums[i] + nums[j])
#             if third in myset:
#                 triplet = [nums[i], nums[j], third]
#                 triplet.sort()
#                 result.add(tuple(triplet))
#             myset.add(nums[j])
#     return [list(triplet) for triplet in result]

# nums = [-1, 0, 1, 2, -1, -4]
# print(threeSumHashing(nums))