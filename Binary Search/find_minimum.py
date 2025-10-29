# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

class Solution:
    def findMin(self, nums):
        n = len(nums)
        low = 0
        high = n - 1
        minimum = float('inf')
        while low < high:
            mid = (low + high) // 2
            if nums[mid] <= nums[high]: # right part is sorted
                minimum = min(minimum, nums[mid])
                high = mid - 1
            else: # left part is sorted
                minimum = min(minimum, nums[low])
                low = mid + 1
        return minimum

# Example usage:
if __name__ == "__main__":
    nums = [3,4,5,1,2]
    solution = Solution()
    print(solution.findMin(nums))