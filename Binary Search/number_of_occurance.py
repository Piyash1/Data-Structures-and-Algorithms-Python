# Given a sorted array, arr[] and a number target, you need to find the number of occurrences of target in arr[]. 

class Solution:
    def countFreq(self, arr, target):
        first_occurrence = self.lower_bound(arr, target)
        if first_occurrence == -1 or arr[first_occurrence] != target:
            return 0
        
        last_occurrence = self.upper_bound(arr, target)
        
        return last_occurrence - first_occurrence
    
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
    arr = [1, 2, 2, 2, 3, 4, 5]
    target = 2
    solution = Solution()
    print(solution.countFreq(arr, target))  