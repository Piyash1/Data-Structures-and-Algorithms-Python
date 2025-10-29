# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # In case k is greater than n

        # Helper function to reverse a portion of the array
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Step 1: Reverse the last k elements
        reverse(n - k, n - 1)
        # Step 2: Reverse the rest of the array
        reverse(0, n - k - 1)
        # Step 3: Reverse the whole array
        reverse(0, n - 1)
    
# Example usage:
sol = Solution()
arr = [1,2,3,4,5,6,7]
sol.rotate(arr, 3)
print(arr)  




# # Brute Force Approach
# def rotate(arr, k):
#     n = len(arr)
#     k = k % n  # In case k is greater than n
#     for _ in range(k):
#         e = arr.pop()
#         arr.insert(0, e)
#     return arr

# arr = [1,2,3,4,5,6,7]
# print(rotate(arr, 2))

# # Better Approach(Using slicing)
# def rotate(arr, k):
#     n = len(arr)
#     k = k % n  # In case k is greater than n
#     return arr[-k:] + arr[:-k]
# arr = [1,2,3,4,5,6,7]
# print(rotate(arr, 2))

# # Given an integer array nums, rotate the array to the left by k steps, where k is non-negative.

# class Solution:
#     def rotate(self, nums: list[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         k = k % n  # In case k is greater than n

#         # Helper function to reverse a portion of the array
#         def reverse(start, end):
#             while start < end:
#                 nums[start], nums[end] = nums[end], nums[start]
#                 start += 1
#                 end -= 1

#         # Step 1: Reverse the last k elements
#         reverse(0, k-1)
#         # Step 2: Reverse the rest of the array
#         reverse(k, n - 1)
#         # Step 3: Reverse the whole array
#         reverse(0, n - 1)
    
# # Example usage:
# sol = Solution()
# arr = [1,2,3,4,5,6,7]
# sol.rotate(arr, 3)
# print(arr)  