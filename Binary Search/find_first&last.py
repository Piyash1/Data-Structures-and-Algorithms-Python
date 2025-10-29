# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

class Solution:
    def searchRange(self, nums, target):
        first = self.lower_bound(nums, target)
        last = self.upper_bound(nums, target)
        
        if first == -1 or last == -1:
            return [-1, -1]
        
        # Check if the target is actually present
        if nums[first] != target:
            return [-1, -1]
        
        return [first, last - 1]
    
    def lower_bound(self, nums, target):
        low = 0
        high = len(nums) - 1
        lb = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1
        return lb
    
    def upper_bound(self, nums, target):
        low = 0
        high = len(nums) - 1
        ub = len(nums)
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                ub = mid
                high = mid - 1
            else:
                low = mid + 1
        return ub
        
# Example usage:
if __name__ == "__main__":
    nums = [1]
    target = 1
    solution = Solution()
    result = solution.searchRange(nums, target)
    print("First and Last Position of", target, "is:", result)





# # Bruteforce Approach: Linear Search
# def searchRange(nums, target):
#   n = len(nums)
#   first = -1
#   last = -1
#   for i in range(0, n):
#     if nums[i] == target:
#       if first == -1:
#         first = i
#       last = i
#   return [first, last]

# nums = [5,7,7,8,8,10]
# target = 8
# print(searchRange(nums, target))