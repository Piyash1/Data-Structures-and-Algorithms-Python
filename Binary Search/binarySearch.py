# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

class solution:
    def binarySearch(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return -1

# Example usage:
if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9
    sol = solution()
    result = sol.binarySearch(nums, target)
    print(f"Index of target {target} in nums: {result}") 