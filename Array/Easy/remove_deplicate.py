# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

class Solution(object):
    def removeDuplicates(self, nums):
        n = len(nums)
        if n == 1:
            return 1
        
        i = 0
        j = i + 1
        while j < n:
            if nums[j] != nums[i]:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
            j += 1
        return i + 1

# Example usage:
solution = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
length = solution.removeDuplicates(nums)
print(length)  
print(nums[:length]) 




# # Brute Force Approach
# def remove_duplicates(nums):
#     n = len(nums)
#     my_dict = {}
#     for i in range(n):
#         my_dict[nums[i]] = 0
#     j = 0
#     for k in my_dict:
#         nums[j] = k
#         j += 1
#     return j

# nums = [0,0,1,1,1,2,2,3,3,4]
# print(remove_duplicates(nums))