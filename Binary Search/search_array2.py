# Leetcode no. 81 - Search in Rotated Sorted Array II

class Solution(object):
    def search(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        while low <= high:
            mid = (low+high) // 2
            if nums[mid] == target:
                return True
            if nums[low] == nums[mid] == nums[high]: # when duplicates are present
                low += 1
                high -= 1
                continue
            if nums[low] <= nums[mid]: # check if left part is sorted
                if nums[low] <= target <= nums[mid]: # check if target is in sorted part
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False

# Example usage:
if __name__ == "__main__":
    nums = [2,5,6,0,0,1,2]
    target = 3
    solution = Solution()
    print(solution.search(nums, target))