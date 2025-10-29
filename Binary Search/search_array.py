# Leetcode no. 33 - Search in Rotated Sorted Array

class Solution:
    def search(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        while low <= high:
            mid = (low+high) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] <= nums[high]: #identify the sorted part
                if nums[mid] <= target <= nums[high]: # check if target is in sorted part
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1

# Example usage:
if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    solution = Solution()
    print(solution.search(nums, target))


# # Brute Force Approach
# def search(nums, target):
#   n = len(nums)
#   low = 0
#   for i in range(n):
#     if nums[i] == target:
#       return i
#   return -1

# nums = [4,5,6,7,0,1,2]
# target = 0
# print(search(nums, target))